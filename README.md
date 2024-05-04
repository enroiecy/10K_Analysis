**Why would a user care about sentiment analysis?**

    - Typically, the 10-k form is analyzed by the numbers and loosely by the auditing remarks. Being able to see the sentiment analysis of a company's 10-k forms through a certain period can reveal trends that might otherwise be overlooked. It is an additional insight that can reveal extra information to the performance of a company. In this project, the two control companies can be compared and then applied to the experiment company for predictive analysis. Given more time, other factors should be included and the correlation of these variables can give further intuition.

**Tech Stack:**

    - Flask
        - Easy to set up and run
    - Plain HTML/CSS/JS
        - Plotly for its added functionality such as being able to save the plot as a png for the user

**Project Info**

Downloaded 10-k filings from three companies from 1995-01-01 to 2023-01-01:

    Kodak ($KODK)

    Alphabet Inc. ($GOOGL)

    Tesla Inc. ($TSLA)

$KODK: control variable to use as company that faced bankruptcy

$GOOGL: control variable to use as company that is still doing well

$TSLA: experiment variable to see if it follows the patterns of either $KODK or $GOOGL to predict future performance

Model:

    Distilbert-base-uncased-finetuned-sst-2-english

        - This model is a fine-tune checkpoint of DistilBERT-base-uncased, fine-tuned on SST-2. 

        - The authors use the following Stanford Sentiment Treebank(sst2) corpora for the model.

        - Use case: sentiment analysis (recommended by HuggingFace Inference API Docs)

Visualizations:

    - Sentiment Analysis

    - Topic Modeling (LDA or NMF)

    - WordCloud

Future Work:

    - BETTER PREPROCESSING

        - Create a dataset with the various sections of the 10-K form. Then, perform analysis on each section individually.

        - Time series plot of revenue, net income, or cash flow over the entire periods

        - Correlation heatmap of different variables (revenue, expenses, assets, etc.)

        - Sentiment Analysis plot for *each* section of a 10-K form

    - MORE VISUALIZATIONS/INSIGHTS (wordcloud, LDA, etc.)

    - ADD COMPANY FINANCIAL PERFORMANCE FOR EACH YEAR TO SEE THE IMPACT OF INSIGHTS
    
    - CLEANER USER INTERFACE