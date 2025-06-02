#!pip install nltk
#!pip install rank_bm25
#!pip install scikit-learn
#!pip install pandas


import nltk
import pandas as pd
import numpy as np


nltk.download('movie_reviews')  # Solo se necesita una vez

from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi


# Cargar documentos como texto plano
docs = [" ".join(movie_reviews.words(fileid)) for fileid in movie_reviews.fileids()]

# Obtener los IDs de los archivos
file_ids = movie_reviews.fileids()

# Ver cuántos documentos hay
print("Número total de documentos:", len(file_ids))

# Ejemplo de etiquetas (pos/neg)
print("Etiquetas posibles:", movie_reviews.categories())


# Vectorizar los documentos
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(docs)

# Consulta
consulta = ["chicken"]
consulta_tfidf = vectorizer.transform(consulta)

# Calcular similitudes
similitudes = cosine_similarity(consulta_tfidf, X_tfidf).flatten()
ranking_indices = similitudes.argsort()[::-1]

# Mostrar resultados
top_n = 5
resultados = pd.DataFrame({
    'Indice Documento': ranking_indices[:top_n],
    'Similitud': similitudes[ranking_indices[:top_n]],
    'Contenido': [docs[i][:200].replace('\n', ' ') + "..." for i in ranking_indices[:top_n]]
})

print(resultados)


# Tokenizar el corpus
tokenized_docs = [doc.lower().split() for doc in docs]

# Crear el modelo BM25
bm25 = BM25Okapi(tokenized_docs)

# Consulta
consulta = ["chicken"]

# Calcular scores BM25
bm25_scores = bm25.get_scores(consulta)
ranking_bm25 = np.argsort(bm25_scores)[::-1]  # Ojo: era `np.argsort10`, que no existe

# Mostrar resultados
top_n = 5
resultados_bm25 = pd.DataFrame({
    'Indice Documento': ranking_bm25[:top_n],
    'Score': bm25_scores[ranking_bm25[:top_n]],
    'Contenido': [docs[i][:200].replace('\n', ' ') + "..." for i in ranking_bm25[:top_n]]
})

print(resultados_bm25)

modelo = "tfidf"  # Cambia a "bm25" para probar el otro

if modelo == "tfidf":
    print("Usando TF-IDF + Cosine Similarity:")
    print(resultados)
else:
    print("Usando BM25:")
    print(resultados_bm25)

