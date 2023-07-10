# Text Search Engine

## Overview
This project is a text search engine that allows users to crawl web pages, preprocess the data, create a TF-IDF matrix, and perform queries to retrieve the most relevant documents based on the search query. The search engine is implemented using Python and various libraries such as BeautifulSoup, NLTK, and scikit-learn.

## Features
- Web crawler to collect web pages from specified domains.
- Preprocessing of web page content including tokenization, stop word removal, and stemming.
- Creation of a TF-IDF matrix to represent the documents.
- Query processing to transform user queries into vectors and retrieve relevant documents.
- Ranking of documents based on cosine similarity.
- Command line interface for interacting with the search engine.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`

## Scripts

### crawler.py
The `crawler.py` script implements a web crawler that collects web pages from specified domains. It uses the requests library to retrieve web pages and BeautifulSoup to parse the HTML content. The collected URLs are saved to separate files for each domain.

### preprocessor.py
The `preprocessor.py` script performs preprocessing on the collected web page data. It tokenizes the content, removes stop words, and performs stemming. The preprocessed tokens are saved to separate files for each web page.

### tfidf_vectorizer.py
The `tfidf_vectorizer.py` script creates a TF-IDF matrix based on the preprocessed web page data. It uses the TfidfVectorizer from scikit-learn to calculate the TF-IDF weights. The resulting matrix is saved as a NumPy array.

### query_processor.py
The `query_processor.py` script handles the processing of user queries. It tokenizes the query, removes stop words, performs stemming, and represents the query as a TF-IDF weighted vector using the same vectorizer as used for the documents.

### rank_documents.py
The `rank_documents.py` script ranks the documents based on cosine similarity between the query vector and the document vectors. It uses the cosine_similarity function from scikit-learn to calculate the cosine similarities. The top-k most relevant documents are returned.

### main.py
The `main.py` script is the entry point of the application. It orchestrates the execution of the different scripts based on user commands. It provides command-line interface options to crawl, preprocess, create the TF-IDF matrix, and perform query searches.

## GUI (Work in Progress)
A graphical user interface (GUI) is currently being developed to provide a more user-friendly way to interact with the text search engine. Stay tuned for updates on the GUI development.

