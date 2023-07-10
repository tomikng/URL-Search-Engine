import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def rank_documents(query_vector, tfidf_matrix, k=10):
    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Sort the documents by their cosine similarity and get the indices
    top_k_doc_indices = np.argsort(cosine_similarities)[::-1][:k]

    return top_k_doc_indices
