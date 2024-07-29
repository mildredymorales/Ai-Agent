import os
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Function to separate responses from each file based on a given phrase
def separate_responses(file_path, phrase):
    with open(file_path, 'r') as file:
        content = file.read()

    # Use regular expression to split based on the phrase
    responses = re.split(r'(?<!\n)\b' + re.escape(phrase) + r'\b', content)

    # The first item will be everything before the first occurrence of the phrase
    # if the file starts with a response, otherwise it will be an empty string
    if responses[0] == '':
        responses = responses[1:]

    # Strip leading and trailing whitespace from each response
    responses = [response.strip() for response in responses]

    # Filter out any empty responses
    responses = [response for response in responses if response]

    return responses

# Function to preprocess text (lowercase, remove punctuation, stopwords, and stem)
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation and white space
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip()

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Stemming
    ps = PorterStemmer()
    stemmed_text = [ps.stem(word) for word in tokens]

    # Reconstruct document from processed tokens
    processed_text = ' '.join(stemmed_text)

    return processed_text

# Function to calculate cosine similarities and write results to file for all responses in all subfolders
def calculate_cosine_similarity(parent_folder_path, phrase, output_file):
    all_responses = []

    # Walk through all subfolders and files
    for root, dirs, files in os.walk(parent_folder_path):
        for file_name in files:
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)

                # Process responses from the current file
                responses = separate_responses(file_path, phrase)
                processed_responses = [preprocess_text(response) for response in responses]
                all_responses.extend(processed_responses)

    # Proceed if there are any processed responses
    if all_responses:
        # Step 1: Create TfidfVectorizer instance
        vectorizer = TfidfVectorizer()

        # Step 2: Fit and transform the vectorizer on the combined documents
        tfidf_matrix = vectorizer.fit_transform(all_responses)

        # Step 3: Calculate cosine similarity
        num_responses = len(all_responses)
        cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # Extract the upper triangle of the similarity matrix (excluding the diagonal)
        upper_triangle_indices = np.triu_indices(num_responses, k=1)
        upper_triangle_similarities = cosine_similarities[upper_triangle_indices]

        # Calculate average, max, and min cosine similarities
        average_similarity = np.mean(upper_triangle_similarities)
        max_similarity = np.max(upper_triangle_similarities)
        min_similarity = np.min(upper_triangle_similarities)

        # Write results to file
        with open(output_file, 'w') as f:
            f.write("Cosine Similarities Across All Responses:\n")
            for i in range(num_responses):
                for j in range(i + 1, num_responses):
                    f.write(f"Row {i+1} vs Row {j+1}: {cosine_similarities[i][j]}\n")
            f.write(f"\nAverage Cosine Similarity: {average_similarity}\n")
            f.write(f"Maximum Cosine Similarity: {max_similarity}\n")
            f.write(f"Minimum Cosine Similarity: {min_similarity}\n")

# Main code to run the analysis
if __name__ == "__main__":
    # Input parent folder path and phrase
    parent_folder_path = input("Please input the parent folder path: ")
    phrase = input("Please enter the phrase that appears right before the start of a new response: ")
    output_file = input("Please input the output file name (e.g., output.txt): ")

    # Calculate cosine similarities and write results to file for all responses in all subfolders
    calculate_cosine_similarity(parent_folder_path, phrase, output_file)

    print(f"Results have been written to {output_file}.")
