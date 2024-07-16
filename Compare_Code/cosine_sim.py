"""
compute cosine similairty using tf idf vectorization.
pre process first 
input is a document where each new line is its own response
outputs the values of each response compared to another from 1-10
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import re

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')


# Sample documents
# doc1 = "Natural language processing is a field of computer science."
# doc2 = "Computer science deals with artificial intelligence."

def read_responses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        responses = file.readlines()
    
    # sep docs from whole output file, not needed if we input a diff way
    # Split content by "## Welcome to the Biology Crew"
    # responses_raw = re.split(r'## Welcome to the Biology Crew', responses)
    # # Initialize list to store individual responses
    # responses = []
    # for response_raw in responses_raw:
    #     responses = re.split(r'Task output:', response_raw, flags=re.IGNORECASE)

    return responses

# Text preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and white space

    # text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()


    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
     # Stemming = Transforming words into their base form
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    stemmed_text = [ps.stem(word) for word in tokens]

    # Reconstruct document from processed tokens
    processed_text = ' '.join(stemmed_text)
    return processed_text

# Preprocess documents
# processed_doc1 = preprocess_text(doc1)
# processed_doc2 = preprocess_text(doc2)


# Read all responses from file, each new line is a response
responses = read_responses('data.txt')
# Preprocess all responses
processed_responses = [preprocess_text(response) for response in responses]

# Step 1: Create TfidfVectorizer instance
vectorizer = TfidfVectorizer()

# Step 2: Fit and transform the vectorizer on the processed documents
tfidf_matrix = vectorizer.fit_transform(processed_responses)
# tfidf_matrix = vectorizer.fit_transform([processed_doc1, processed_doc2])

# Step 3: Calculate cosine similarity
num_responses = len(processed_responses)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
# cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# Print the cosine similarity
print("Cosine Similarities:")
for i in range(num_responses):
    for j in range(i + 1, num_responses):
        print(f"Row {i+1} vs Row {j+1}: {cosine_similarities[i][j]}")
# print("Cosine Similarity:", cosine_sim[0][0])
