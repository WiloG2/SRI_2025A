from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi
from sklearn.metrics.pairwise import cosine_similarity
import contractions
import re
import nltk

# Descargas necesarias
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ========== FUNCIONES DE PREPROCESAMIENTO ==========
def preprocess_docs(docs):
    expanded_docs = [contractions.fix(doc) for doc in docs]
    tokenized_docs = [re.findall(r"\b\w+\b", doc.lower()) for doc in expanded_docs]
    normalized_docs = [
        [token for token in doc if token.isalpha()] for doc in tokenized_docs
    ]
    stop_words = set(stopwords.words('english'))
    filtered_docs = [
        [token for token in doc if token not in stop_words]
        for doc in normalized_docs
    ]
    lemmatizer = WordNetLemmatizer()
    lemmatized_docs = [
        [lemmatizer.lemmatize(token) for token in doc]
        for doc in filtered_docs
    ]
    return lemmatized_docs

# ========== CARGA Y PROCESAMIENTO DE DATOS ==========
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
raw_docs = newsgroups.data
tokenized_docs = preprocess_docs(raw_docs)
text_docs = [" ".join(doc) for doc in tokenized_docs]  # para TF-IDF

# ========== MODELOS ==========
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(text_docs)

bm25 = BM25Okapi(tokenized_docs)

# ========== BÚSQUEDAS ==========
def search_tfidf(query, top_k=5):
    query_tokens = preprocess_docs([query])
    query_text = " ".join(query_tokens[0])
    query_vector = vectorizer.transform([query_text])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    results = [raw_docs[i][:300] for i in top_indices]
    return results

def search_bm25(query, top_k=5):
    query_tokens = preprocess_docs([query])[0]
    scores = bm25.get_scores(query_tokens)
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:top_k]
    results = [raw_docs[i][:300] for i in top_indices]
    return results
