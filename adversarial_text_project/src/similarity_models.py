import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load model once globally
model = SentenceTransformer('all-MiniLM-L6-v2')

def jaccard_similarity(text1, text2, n=3):
    vectorizer = CountVectorizer(ngram_range=(n, n), binary=True)
    X = vectorizer.fit_transform([text1, text2]).toarray()
    
    intersection = np.logical_and(X[0], X[1]).sum()
    union = np.logical_or(X[0], X[1]).sum()
    
    return intersection / union if union != 0 else 0

def tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]

def embedding_similarity(text1, text2):
    emb1 = model.encode(text1)
    emb2 = model.encode(text2)
    return cosine_similarity([emb1], [emb2])[0][0]