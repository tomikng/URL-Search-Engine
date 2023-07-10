import os
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))


def process_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tokens = word_tokenize(soup.get_text())
        tokens = [word for word in tokens if word.isalpha()]
        tokens = [word.lower() for word in tokens]
        tokens = [word for word in tokens if word not in stop_words]
        return tokens
    except Exception as e:
        print(f'Error processing URL: {url}\n{str(e)}')
        return []


def write_tokens(tokens, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(token + "\n")


def preprocess_urls(base_dir):
    for url_file in os.listdir(base_dir):
        if url_file.endswith("_urls.txt"):
            domain = url_file.split('_')[0]
            print(f"Processing domain: {domain}")

            with open(base_dir + url_file, 'r') as f:
                urls = f.read().splitlines()
                for url in urls[:100]:
                    tokens = process_url(url)
                    filename = url.replace('://', ';').replace('/', '@') + '.txt'
                    write_tokens(tokens, f'data/data/{filename}')



