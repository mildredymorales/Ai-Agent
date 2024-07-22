import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Download NLTK resources (if not already downloaded)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


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


file_path = 'Results/cell_comm/cell_comm_task_cell_cyc_agent_log.txt'
# use phrase that appears right before start of a new response
# think about cutting out some of the agent task description 
phrase = 'status=completed'
responses = separate_responses(file_path, phrase)

# Now responses is a list where each element is a separate response
# for idx, response in enumerate(responses):
#     print(f"Response {idx+1}:")
#     print(response)
#     print()

# def remove_phrases(response):
#     start_marker = 'agent='
#     end_marker = 'status=started'
    
#     start_idx = response.find(start_marker)
#     end_idx = response.find(end_marker)
    
#     if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
#         # Remove header and footer
#         cleaned_response = response[end_idx + len(end_marker):].strip()
#     else:
#         cleaned_response = response  # Return original response if markers are not found
    
#     return cleaned_response

# cleaned_responses = [remove_phrases(response) for response in responses]
# # Print processed responses
# for idx, response in enumerate(cleaned_responses):
#     print(f"Processed Response {idx + 1}:")
#     print(response)
#     print()


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
    # print(processed_text)
    return processed_text



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

output_file = "TF_IDF_Analysis/task_agent_cosine_sim.txt"

with open(output_file, 'w') as f:
    # Print the cosine similarity
    f.write(f"Cosine Similarities:\n")
    f.write(f"File: {file_path}\n")
    for i in range(num_responses):
        for j in range(i + 1, num_responses):
            f.write(f"Row {i+1} vs Row {j+1}: {cosine_similarities[i][j]}\n")
    # print("Cosine Similarity:", cosine_sim[0][0])