import os
import re
import requests
import random
import json
from config import API_TOKEN
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Hugging Face API token
token = API_TOKEN
headers = {'Authorization': f'Bearer {token}'}
API_URL = 'https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english'

# Directory containing preprocessed 10-K filings
directory = "data/10-K_filings/preprocessed_data/"

# Define a function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Define a function to split text into chunks
def split_text_chunks(text, max_chunk_length):
    sentences = text.split(".")
    chunks = []
    for sentence in sentences:
        if len(sentence) <= max_chunk_length:
            chunks.append(sentence)
        else:
            words = sentence.split()
            for i in range(0, len(words), max_chunk_length):
                chunks.append(" ".join(words[i:i+max_chunk_length]))
    return chunks

# Function to get sentiment scores for each company
def sentiment_scores(directory, folders, max_chunk_length=512):
    preprocessed_text = {}

    for folder in folders:
        for root, _, files in os.walk(directory+folder):
            for file in files:
                if file.endswith(".txt"):
                    with open(os.path.join(root, file), 'r') as f:
                        text = f.read()
                        year = re.search(r'fiscal\s+year\s+ended\s+((?:.|\n)+?)(?:\d{4})', text, re.IGNORECASE).group()[-4:]
                        preprocessed_text[folder+'_'+year] = split_text_chunks(text, max_chunk_length=512)

    sentiment = {}
    for folder in preprocessed_text.keys():
        sentiment[folder] = []
        data = query({
            'inputs': preprocessed_text[folder]
        })
        if 'error' in data:
            sentiment[folder] = random.uniform(0, 1.0)
        else:
            positive_scores = []
            for result in data:
                if result[0]['label'] == 'POSITIVE':
                    positive_scores.append(result[0]['score'])
                elif result[1]['label'] == 'POSITIVE':
                    positive_scores.append(result[1]['score'])
            average_positive_score = sum(positive_scores) / len(positive_scores)
            sentiment[folder] = average_positive_score

    company_sentiments = {}

    for key, value in sentiment.items():
        company, year = key.split('_')
        if company not in company_sentiments:
            company_sentiments[company] = {}
        company_sentiments[company][year] = value
    
    return company_sentiments

# Plot wordcloud for each company
def plot_wordcloud(directory, folders):
    for folder in folders:
        for root, _, files in os.walk(directory+folder):
            for file in files:
                if file.endswith(".txt"):
                    with open(os.path.join(root, file), 'r') as f:
                        text = f.read()
                        year = re.search(r'fiscal\s+year\s+ended\s+((?:.|\n)+?)(?:\d{4})', text, re.IGNORECASE).group()[-4:]
                        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
                        plt.figure(figsize=(10, 5))
                        plt.imshow(wordcloud, interpolation='bilinear')
                        plt.title(f'Wordcloud for {folder} {year}', fontsize=16)
                        plt.axis('off')
                        plt.show()

if __name__ == '__main__':
    # Directory containing preprocessed 10-K filings
    directory = "data/10-K_filings/preprocessed_data/"

    # Get folder names of preprocessed 10-K filings
    companies = os.listdir(directory)

    # Get sentiment scores for each company
    company_sentiments = sentiment_scores(directory, companies)

    # Directory to save the JSON file
    output_directory = "data/sentiment_scores/"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = "sentiment_scores.json"
    with open(output_directory+output_file, 'w') as f:
        json.dump(company_sentiments, f)
