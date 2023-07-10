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

## Future Work
We are currently in the process of developing a more user-friendly GUI for the application, so stay tuned for updates!

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