from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
doc1 = "Natural language processing is a field of computer science."
doc2 = "Computer science deals with artificial intelligence."

# Step 1: Create TfidfVectorizer instance
vectorizer = TfidfVectorizer()

# Step 2: Fit and transform the vectorizer on the documents
tfidf_matrix = vectorizer.fit_transform([doc1, doc2])

# Step 3: Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# Print the cosine similarity
print("Cosine Similarity:", cosine_sim[0][0])
