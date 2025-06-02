#!pip install nltk

import nltk
nltk.download('movie_reviews')  # Solo se necesita una vez

from nltk.corpus import movie_reviews

# Obtener los IDs de los archivos
file_ids = movie_reviews.fileids()

# Ver cuántos documentos hay
print("Número total de documentos:", len(file_ids))

# Ejemplo de etiquetas (pos/neg)
print("Etiquetas posibles:", movie_reviews.categories())

# Ejemplo: Obtener las palabras del primer documento
print("Primeras palabras del primer documento:")
print(movie_reviews.words(file_ids[0])[:50])

# Obtener el texto completo como una sola cadena
texto = " ".join(movie_reviews.words(file_ids[0]))
print("\nPrimeros 300 caracteres del texto:")
print(texto[:300])