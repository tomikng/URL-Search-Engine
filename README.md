# Text Search Engine

## Overview
This project is a text search engine that employs various techniques to search web content efficiently. The tool is built with Python and uses a variety of libraries including BeautifulSoup, NLTK, and scikit-learn. It crawls web pages, preprocesses data, creates a TF-IDF matrix, and processes queries to find the most relevant documents related to a search query.

## Terminology
Before delving into the features, here are explanations of some terms that are essential to understanding how the search engine works:

- **Web Crawling:** This is the process of programmatically browsing the internet to collect web page data. It's like sending out a robot to visit web pages, read their content, and bring the data back.

- **Tokenization:** This is the process of breaking down text into individual words or terms, known as tokens. For example, the sentence "This is a sentence" would be tokenized into ["This", "is", "a", "sentence"].

- **Stop Words:** These are commonly used words in a language (like 'is', 'an', 'the', 'and' in English) that are typically filtered out during text processing since they don't provide significant meaning on their own.

- **Stemming:** This is the process of reducing a word to its base or root form. For example, "running", "runs", and "ran" all stem from the root word "run". This helps in understanding the semantic meaning of texts.

- **TF-IDF Matrix:** TF-IDF stands for Term Frequency-Inverse Document Frequency. It's a statistical measure used to evaluate the importance of a word to a document in a collection or corpus. The TF-IDF value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, helping to adjust for the fact that some words appear more frequently in general.

- **Cosine Similarity:** This is a measure used to determine how similar two documents are to each other. It's calculated by taking the cosine of the angle between two vectors. In the context of this search engine, each document and query is transformed into a vector in multi-dimensional space, and the cosine similarity is calculated to determine how closely related a document is to a given query.

## Features
- **Web Crawling:** Collects web pages from specified domains.
- **Data Preprocessing:** Performs tokenization, stop word removal, and stemming on the crawled web page data.
- **TF-IDF Matrix Creation:** Uses the preprocessed data to create a TF-IDF matrix, which gives a numerical representation of the importance of different words in the documents.
- **Query Processing:** Transforms user queries into vectors similar to those used to represent the documents, and retrieves relevant documents based on this.
- **Document Ranking:** Ranks the documents based on cosine similarity to the query vector, which gives a measure of how relevant a document is to the query.

## How it works
- **Web Crawling**: The engine starts by using a web crawler to browse the internet and collect web page data. The web pages to be crawled are defined by the user.
- **Data Preprocessing**: The collected web page data is then preprocessed. This involves breaking down the text content into individual words or tokens (tokenization), removing commonly used words that don't provide much semantic meaning (stop words), and reducing words to their base or root form (stemming).

- **TF-IDF Matrix Creation**: After preprocessing, the data is used to create a TF-IDF matrix. The TF-IDF (Term Frequency-Inverse Document Frequency) matrix represents the importance of different words in the documents. Each document is represented as a vector, and each unique word is a dimension in this multi-dimensional space. The TF-IDF score of each word (which reflects its importance in the document relative to the entire corpus of documents) is the value in the corresponding dimension.

- **Query Processing**: When a user inputs a search query, the engine processes this query similarly to the documents - it tokenizes the query, removes stop words, performs stemming, and transforms it into a vector in the same multi-dimensional space as the documents.

- **Document Ranking**: The engine then computes the cosine similarity between the query vector and each document vector. The cosine similarity is a measure of how closely related two vectors (in this case, the search query and a document) are. The documents are ranked based on their cosine similarity to the query vector, and the most relevant documents (i.e., those with the highest cosine similarity scores) are returned as the search results.
### Used libraries
- requests: This is a Python library used for making HTTP requests. It abstracts the complexities of making requests behind a simple API, allowing you to send HTTP/1.1 requests. In the context of this project, requests is used to send HTTP requests to the URLs specified for web crawling.

- beautifulsoup4: BeautifulSoup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner. In this project, it is used to parse the HTML content of the web pages collected by the crawler.

- nltk (Natural Language Toolkit): NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning. In this project, it's used for tokenizing the text (breaking it down into individual words), removing stop words, and stemming (reducing words to their root form).

- scikit-learn: Scikit-learn is a free software machine learning library for Python. It features various classification, regression, and clustering algorithms, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. In this project, scikit-learn is used to compute the TF-IDF matrix from the preprocessed text data and calculate cosine similarity between the query vector and document vectors for ranking.

- numpy: NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It's used in this project for efficient computations with arrays when calculating TF-IDF scores and cosine similarities.

- tkinter: Tkinter is the standard GUI toolkit for Python. It is the most commonly used method for creating graphic user interfaces that allows the user to interact with the application. In this project, tkinter is used to create the GUI for the search engine, which includes areas to input URLs for the web pages to search, a place to input a search query, and a search button to start the search.

## Installation
1. Clone the repository: `git clone https://github.com/tomikng/URL-Search-Engine`
2. Navigate to the project directory: `cd your-repo`

## GUI
This application has a graphical user interface (GUI) built with a Python library called Tkinter, which makes it easier to use. After starting the program, you'll see areas to input URLs for the web pages you want to search, a place to input a search query, and a search button to start the search.

## Scripts
The different functionalities of this application are implemented in separate Python scripts. Here's a brief overview of what each script does:

- **crawler.py:** Implements a web crawler that visits web pages and collects their data.
- **preprocessor.py:** Preprocesses the collected web page data by tokenizing the content, removing stop words, and performing stemming.
- **tfidf_vectorizer.py:** Creates a TF-IDF matrix from the preprocessed web page data.
- **query_processor.py:** Handles the transformation of user queries into vectors, using the same method used for the documents.
- **rank_documents.py:** Ranks the documents based on their cosine similarity to the query vector.
- **main.py:** The main script that you run to use the application. It controls the other scripts and provides a graphical interface for user interaction.


## Usage
To use the text search engine, follow these steps:
1. Clone the repository.
2. Run `python main.py` from the terminal.

## Dependencies
Make sure that the following Python libraries are installed on your machine:
- `requests`
- `beautifulsoup4`
- `nltk`
- `scikit-learn`
- `numpy`
- `tkinter`
