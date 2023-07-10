import os
import shutil

from data.preprocessing.preprocessor import preprocess_urls
from data.crawler.crawler import get_all_website_links, save_links_to_file
from tfidf_vectorizer import get_tfidf_matrix
from query_processor import process_query
from rank_documents import rank_documents


def main():
    # Specify the URLs to crawl
    urls = ["https://edition.cnn.com", "https://www.bbc.com"]

    # Clear the data directories before each run
    clear_directory('data/urls')
    clear_directory('data/data')

    # Crawl the URLs and save the links
    for url in urls:
        links = get_all_website_links(url)
        save_links_to_file(url, links, 'data/urls/')

    # Preprocess the URLs
    base_dir = 'data/urls/'
    preprocess_urls(base_dir)

    # Create the tf-idf matrix
    directory = "data/data/"
    tfidf_matrix, vectorizer, file_names = get_tfidf_matrix(directory)
    print("TFIDF Matrix Shape:", tfidf_matrix.shape)

    while True:
        query = input("Please enter your query (or 'exit' to stop): ")
        if query.lower() == 'exit':
            break

        normalized_query_vector = process_query(query, vectorizer)

        k = 10
        top_k_doc_indices = rank_documents(normalized_query_vector, tfidf_matrix, k)

        print(f"Top {k} documents for your query are:")
        for index in top_k_doc_indices:
            print(file_names[index].replace(';', '://').replace('@', '/').replace('.txt', ''))


def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


if __name__ == "__main__":
    main()
