# 10K Form LLM Analysis Program

## Why would a user care about sentiment analysis?

Typically, the 10-k form receives thorough scrutiny primarily for its financial numerical data, while the auditing remarks are often briefly reviewed as well. However, incorporating sentiment analysis of a company's 10-k forms over a specific timeframe can unveil overlooked trends. This additional insight can shed light on a company's performance. In this project, comparing two control companies and then applying the findings to the experimental company allows for predictive analysis. Given additional time, other factors should be considered, and examining the correlation between these variables can provide deeper insights.

## Tech Stack:
* __Flask__: 
    * lightweight, ease of use, rapid prototyping
    * serves HTML templates and static files
    * handles HTTP requests and responses
* __HTML/CSS/JS__
    * core frontend technologies

## Overview

Downloaded 10-k filings of three companies from 1995-01-01 to 2023-01-01:
* __Kodak ($KODK)__
    * Control variable representing a company that faced bankruptcy
* __Alphabet Inc. ($GOOGL)__
    * Control variable representing a company that is still performing well
* __Tesla Inc. ($TSLA)__
    * Experimental variable used to analyze whether it follows the patterns of either $KODK or $GOOGL to predict future performance

## Model

* __Distilbert-base-uncased-finetuned-sst-2-english__
    * A fine-tuned checkpoint of DistilBERT-base-uncased, trained on SST-2
    * Utilized Stanford Sentiment Treebank (sst2) corpora
    * Use case: sentiment analysis (recommended by HuggingFace Inference API Docs)

## Visualizations

* __Sentiment Analysis__
* __Topic Modeling (LDA, NMF)__
* __WordCloud__

## Ongoing Work
* __Improved Preprocessing__
    * Create a dataset with various sections of the 10-k form for individual analysis
    * Time series plot of revenue, net income, or cash flow over the entire period
    * Correlation heatmap of different variables (revenue, expenses, assets, etc.)
    * Sentiment analysis plot for _each_ section of the 10-k form
* __Additional Visualizations/Insights__
    * Wordclouds, LDA, etc.
* __Incorporate Company Financial Performance__
    * Include financial performance data for each year to assess the impact of insights
* __Enhanced User Interface__
    * Improve the user interface for a cleaner and more intuitive experience