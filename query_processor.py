import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.preprocessing import normalize

nltk.download('punkt')
nltk.download('stopwords')


def process_query(query, vectorizer):
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # Tokenize the query
    tokens = nltk.word_tokenize(query)

    # Remove stop words and perform stemming
    processed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    processed_query = ' '.join(processed_tokens)

    # Vectorize the query using the TF-IDF weights calculated for the documents
    query_vector = vectorizer.transform([processed_query])

    # Normalize the query vector
    normalized_query_vector = normalize(query_vector)

    return normalized_query_vector
