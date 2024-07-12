"""
There are two codes in this file, the first one that is commented out is a simpler approach and takes in just strings. 
the second approach can take it a whole doc and has more deligent preprocessing and computation, but i need to fix it since it only does csv currently.
the data file incudes each of the agents responses from the last run using all of the terms
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Sample documents
# doc1 = "Natural language processing is a field of computer science."
# doc2 = "Computer science deals with artificial intelligence."

def read_responses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        responses = file.readlines()
    return responses

# Text preprocessing function
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Reconstruct document from processed tokens
    processed_text = ' '.join(tokens)
    return processed_text

# Preprocess documents
# processed_doc1 = preprocess_text(doc1)
# processed_doc2 = preprocess_text(doc2)


# Read all responses from file, each new line is a response
responses = read_responses('data.txt' )
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
        print(f"Response {i+1} vs Response {j+1}: {cosine_similarities[i][j]}")
# print("Cosine Similarity:", cosine_sim[0][0])


"SECOND APPROACH"

# import multiprocessing as mp
# import numpy as np
# import pandas as pd
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import re 
# nltk.download('stopwords', quiet=True)


# data = pd.read_csv('data.csv', delimiter=';', encoding='latin', dtype=str)

# # check data 
# # print(data.head()) 

# # data

# # drop NAN
# data.dropna(subset=['Document'], inplace=True)


# def preprocess_text(text):
#     """
#     Preprocesses a single text document by performing the following steps:
#     1. Lowercases the text.
#     2. Removes punctuation marks.
#     3. Tokenizes the text into individual words.
#     4. Removes English stop words.
#     5. Stems each word to its base form using Porter Stemmer.
    
#     Returns a pandas DataFrame containing various stages of preprocessing for the input text.
#     Columns:
#     - 'DOCUMENT': Original text document.
#     - 'LOWERCASE': Text converted to lowercase.
#     - 'CLEANING': Text after punctuation removal and white space stripping.
#     - 'TOKENIZATION': List of tokens (words) extracted from the text.
#     - 'STOP-WORDS': Tokens with English stop words removed.
#     - 'STEMMING': Tokens stemmed to their base forms.
#     """
#     # Check if text is empty
#     # if text.strip():  # If text is not empty after stripping whitespace
#         # lowercasing
#     lowercased_text = text.lower()

#     # cleaning 
#     remove_punctuation = re.sub(r'[^\w\s]', '', lowercased_text)
#     remove_white_space = remove_punctuation.strip()

#     # Tokenization = Breaking down each sentence into an array
#     tokenized_text = word_tokenize(remove_white_space)

#     # Stop Words/filtering = Removing irrelevant words
#     stopwords_set = set(stopwords.words('english'))
#     stopwords_removed = [word for word in tokenized_text if word not in stopwords_set]

#     # Stemming = Transforming words into their base form
#     ps = PorterStemmer()
#     stemmed_text = [ps.stem(word) for word in stopwords_removed]
    
#     # Putting all the results into a dataframe.
#     df = pd.DataFrame({
#         'DOCUMENT': [text],
#         'LOWERCASE' : [lowercased_text],
#         'CLEANING': [remove_white_space],
#         'TOKENIZATION': [tokenized_text],
#         'STOP-WORDS': [stopwords_removed],
#         'STEMMING': [stemmed_text]
#     })
#     # else:
#     #     # Return an empty DataFrame if text is empty
#     #     df = pd.DataFrame(columns=['DOCUMENT', 'LOWERCASE', 'CLEANING', 'TOKENIZATION', 'STOP-WORDS', 'STEMMING'])

#     return df

# # 

# def preprocessing(corpus):
#     """
#     Preprocesses a corpus of text documents using the preprocess_text function.
    
#     Args:
#     - corpus: DataFrame with a column 'DOCUMENT' containing text documents to preprocess.
    
#     Returns:
#     - DataFrame: Contains all documents from corpus with columns showing each preprocessing step.
#       Each row corresponds to a document in the corpus.
#     """
#     # Create an empty DataFrame
#     df = pd.DataFrame(columns=['Document'])

#     # Running preprocessing one by one
#     for doc in corpus['Document']:
#         # Call the preprocess_text function
#         result_df = preprocess_text(doc)
        
#         # Concatenate the result of preprocessing to the main DataFrame
#         df = pd.concat([df, result_df], ignore_index=True)
        
#     return df

# result_preprocessing = preprocessing(data)
# result_preprocessing

# def calculate_tfidf(corpus):
#     # Call the preprocessing result
#     df = preprocessing(corpus)
        
#     # Make each array row from stopwords_removed to be a sentence
#     stemming = corpus['STEMMING'].apply(' '.join)
    
#     # Count TF-IDF
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(stemming)
    
#     # Get words from stopwords array to use as headers
#     feature_names = vectorizer.get_feature_names_out()

#     # Combine header titles and weights
#     df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)
#     df_tfidf = pd.concat([df, df_tfidf], axis=1)

#     return df_tfidf

# result_tfidf = calculate_tfidf(result_preprocessing)
# result_tfidf

# def cosineSimilarity(corpus):
#     # Call the TF-IDF result
#     df_tfidf = calculate_tfidf(corpus)
    
#     # Get the TF-IDF vector for the first item (index 0)
#     vector1 = df_tfidf.iloc[0, 6:].values.reshape(1, -1)

#     # Get the TF-IDF vector for all items except the first item
#     vectors = df_tfidf.iloc[:, 6:].values
    
#     # Calculate cosine similarity between the first item and all other items
#     cosim = cosine_similarity(vector1, vectors)
#     cosim = pd.DataFrame(cosim)
    
#     # Convert the DataFrame into a one-dimensional array
#     cosim = cosim.values.flatten()

#     # Convert the cosine similarity result into a DataFrame
#     df_cosim = pd.DataFrame(cosim, columns=['COSIM'])

#     # Combine the TF-IDF array with the cosine similarity result
#     df_cosim = pd.concat([df_tfidf, df_cosim], axis=1)

#     return df_cosim

# cosim_result = cosineSimilarity(result_tfidf)
# cosim_result