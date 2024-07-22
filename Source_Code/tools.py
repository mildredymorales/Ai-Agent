# from crewai import tools
from langchain.tools import tool
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

class MathTools():

    @tool("Preprocess the responses to prepare for analysis")
    def pre_process(text):
        """This performs the preprocessing on the agents response
        """
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
    
    @tool("Use TF-IDF to calculate cosine similarity when comparing agents' responses")
    def cosine_sim(response):
        """This computes cosine similarity through tf-idf
        """
        # Step 1: Create TfidfVectorizer instance
        vectorizer = TfidfVectorizer()

        # Step 2: Fit and transform the vectorizer on the processed documents
        tfidf_matrix = vectorizer.fit_transform(response)
        # tfidf_matrix = vectorizer.fit_transform([processed_doc1, processed_doc2])

        # Step 3: Calculate cosine similarity
        num_responses = len(response)
        cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
        # cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

        # Print the cosine similarity
        print("Cosine Similarities:")
        for i in range(num_responses):
            for j in range(i + 1, num_responses):
                return(f"Row {i+1} vs Row {j+1}: {cosine_similarities[i][j]}")
    
    # def tools():
    #     return [MathTools.pre_process, MathTools.cosine_sim]
 