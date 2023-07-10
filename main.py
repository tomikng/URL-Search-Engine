import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from data.preprocessing.preprocessor import preprocess_urls
from data.crawler.crawler import get_all_website_links, save_links_to_file
from tfidf_vectorizer import get_tfidf_matrix
from query_processor import process_query
from rank_documents import rank_documents
import threading
import logging
import webbrowser
import shutil
import os


def crawl_and_tokenize():
    # Clear the directories if they exist
    if os.path.exists('data/urls/'):
        shutil.rmtree('data/urls/')
    if os.path.exists('data/data/'):
        shutil.rmtree('data/data/')

    # Create the directories
    os.makedirs('data/urls/', exist_ok=True)
    os.makedirs('data/data/', exist_ok=True)

    # Get user input
    input_urls = url_entry.get().strip()

    if not input_urls:
        messagebox.showwarning("Empty Input", "Please enter URLs.")
        return

    urls = input_urls.split(", ")

    # Create a thread for crawling and tokenization
    thread = threading.Thread(target=crawl_and_tokenize_thread, args=(urls,))
    thread.start()


def crawl_and_tokenize_thread(urls):
    # Update GUI with animation
    crawl_button.config(state=tk.DISABLED)
    query_entry.config(state=tk.DISABLED)
    search_button.config(state=tk.DISABLED)
    result_listbox.delete(0, tk.END)
    result_listbox.insert(tk.END, "Crawling and Tokenizing...\n")

    for i, url in enumerate(urls):
        links = get_all_website_links(url)
        save_links_to_file(url, links, 'data/urls/')
        logging.info(f"Crawling complete for URL: {url}")

    # Preprocess the URLs
    base_dir = 'data/urls/'
    preprocess_urls(base_dir)
    logging.info("Tokenization complete")

    # Display completion message
    messagebox.showinfo("Crawling and Tokenization", "Crawling and Tokenization completed successfully!")

    # Enable GUI elements
    crawl_button.config(state=tk.NORMAL)
    query_entry.config(state=tk.NORMAL)
    search_button.config(state=tk.NORMAL)


def open_url(event):
    widget = event.widget
    selection = widget.curselection()
    if selection:
        index = selection[0]
        url = widget.get(index)
        webbrowser.open_new(url)


def search_query():
    # Get user input
    query = query_entry.get().strip()

    if not query:
        messagebox.showwarning("Empty Input", "Please enter a query.")
        return

    # Create the tf-idf matrix
    directory = "data/data/"
    tfidf_matrix, vectorizer, file_names = get_tfidf_matrix(directory)

    # Process the query
    normalized_query_vector = process_query(query, vectorizer)

    # Rank documents
    k = 10
    top_k_doc_indices = rank_documents(normalized_query_vector, tfidf_matrix, k)

    # Display results
    result_listbox.delete(0, tk.END)
    for index in top_k_doc_indices:
        url = file_names[index].replace(';', '://').replace('@', '/').replace('.txt', '')
        result_listbox.insert(tk.END, url)


# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the main window
window = tk.Tk()
window.title("Text Search Engine")
window.geometry("500x400")

# URL input
url_label = tk.Label(window, text="Enter URLs (comma separated):")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Crawling button
crawl_button = tk.Button(window, text="Crawl and Tokenize", command=crawl_and_tokenize)
crawl_button.pack()

# Query input
query_label = tk.Label(window, text="Enter Query:")
query_label.pack()
query_entry = tk.Entry(window, width=50)
query_entry.pack()

# Search button
search_button = tk.Button(window, text="Search", command=search_query)
search_button.pack()

# Result listbox
result_label = tk.Label(window, text="Search Results:")
result_label.pack()
result_listbox = tk.Listbox(window, width=60, height=10)
result_listbox.pack()
result_listbox.bind('<<ListboxSelect>>', open_url)

# Run the GUI
window.mainloop()
