import os
import re
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Define a function to preprocess text
def clean_text(text):
    # Remove HTML tags and non-alphanumeric characters
    clean_text = re.sub(r'<[^>]*>', '', text)
    # clean_text = re.sub(r',', '', clean_text)
    clean_text = re.sub(r'[^a-zA-Z0-9\s.]', '', clean_text)

    # Tokenize the text
    tokens = word_tokenize(clean_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the text
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)

# Preprocess each 10-k filing and save it to a new file
def preprocess_10k_filings(folders, input_dir, output_dir):
    for folder in folders:
        for root, _, files in os.walk(input_dir+folder):
            for file in files:
                if file.endswith('.html'):
                    # Extract ticker symbol and year from file path
                    ticker_symbol = folder

                    # Read HTML file
                    with open(os.path.join(root, file), 'r') as html_file:
                        html_content = html_file.read()
                    
                    # Parse HTML using BeautifulSoup
                    soup = BeautifulSoup(html_content, 'html.parser')
                    text = soup.get_text()

                    # Extract fiscal year from text and skip if not found
                    match = re.search(r'fiscal\s+year\s+ended\s+((?:.|\n)+?)(?:\d{4})', text, re.IGNORECASE)
                    if match:
                        year = match.group()[-4:]
                    else:
                        print(f"Failed to extract fiscal year for {ticker_symbol}")
                        continue

                    # Preprocess text
                    preprocessed_text = clean_text(text)

                    # Save preprocessed text to a new file
                    output_filename = f"10k_{ticker_symbol}_{year}.txt"
                    if not os.path.exists(output_dir+ticker_symbol):
                        os.makedirs(output_dir+ticker_symbol)
                    output_filepath = os.path.join(output_dir+ticker_symbol, output_filename)
                    with open(output_filepath, 'w', encoding='utf-8') as output_file:
                        output_file.write(preprocessed_text)

if __name__ == '__main__':
    # Download NLTK pre-trained model for tokenizing
    nltk.download('punkt')
    # Download NLTK pre-trained model for lexical database of English words
    nltk.download('wordnet')

    # Get folder names of downloaded 10-k filings
    folders = os.listdir('data/10-k_filings/sec-edgar-filings')

    # Define input and output directories
    input_dir = 'data/10-k_filings/sec-edgar-filings/'
    output_dir = 'data/10-k_filings/preprocessed_data/'

    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Preprocess 10-K filings
    preprocess_10k_filings(folders, input_dir, output_dir)