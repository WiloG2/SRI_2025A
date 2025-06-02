from sklearn.datasets import fetch_20newsgroups

newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
newsgroupsdocs = newsgroups.data

import contractions
import re

# Expande las contracciones en todos los documentos
expanded_docs = [contractions.fix(doc) for doc in newsgroupsdocs]

# Tokeniza separando palabras por cualquier carácter no alfanumérico (elimina guiones)
tokenized_docs = [re.findall(r"\b\w+\b", doc.lower()) for doc in expanded_docs]

print("Tokens (primer doc):", tokenized_docs[0][:20])

# Parte 2: Normalización (solo letras, elimina números y símbolos)
normalized_docs = [
    [token for token in doc if token.isalpha()]
    for doc in tokenized_docs
]

print("Normalizados (primer doc):", normalized_docs[0][:20])

# Parte 3: Eliminación de Stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

filtered_docs = [
    [token for token in doc if token not in stop_words]
    for doc in normalized_docs
]

print("Sin stopwords (primer doc):", filtered_docs[0][:20])

# Parte 4: Stemming y Lematización
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer, WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_docs = [
    [stemmer.stem(token) for token in doc]
    for doc in filtered_docs
]

lemmatized_docs = [
    [lemmatizer.lemmatize(token) for token in doc]
    for doc in filtered_docs
]

print("Stemming (primer doc):", stemmed_docs[0][:20])
print("Lematización (primer doc):", lemmatized_docs[0][:20])