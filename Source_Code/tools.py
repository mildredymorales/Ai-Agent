# from crewai import tools
from langchain.tools import tool
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Download NLTK resources (if not already downloaded)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class MathTools():
    @tool("Separate all files into individual responses")
    # phrase might not always appear for sure 
    def separate_responses(text: str, phrase: str) -> str:
        """this reads all the agents' responses and is able
        to separate them for calculations
        """
        # Use regular expression to split based on the phrase
        responses = re.split(r'(?<!\n)\b' + re.escape(phrase) + r'\b', text)

        # The first item will be everything before the first occurrence of the phrase
        # if the file starts with a response, otherwise it will be an empty string
        if responses[0] == '':
            responses = responses[1:]

        # Strip leading and trailing whitespace from each response
        responses = [response.strip() for response in responses]
        
        # Filter out any empty responses
        responses = [response for response in responses if response]

        return responses

    @tool("Preprocess Agents text")
    def pre_process(text: str) ->str:
        """This tool will clean and preprocess the text by structuring it for data analysis 
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
    def cosine_sim(text: str) -> float:
        """This computes cosine similarity through tf-idf
        """
        # Step 1: Create TfidfVectorizer instance
        vectorizer = TfidfVectorizer()

        # Step 2: Fit and transform the vectorizer on the processed documents
        tfidf_matrix = vectorizer.fit_transform(text)

        # Step 3: Calculate cosine similarity
        num_responses = len(text)
        cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # print("Cosine Similarities:")
        for i in range(num_responses):
            for j in range(i + 1, num_responses):
                return(f"Row {i+1} vs Row {j+1}: {cosine_similarities[i][j]}")
            
    # @tool("this is the call back mechanism")
    # def callback_function(output):
    #     """this is the callback mechanism to start the tf-idf
    #     """
    #     # text = MathTools.separate_responses(output, phrase)
    #     response = MathTools.pre_process(output)
    #     values = MathTools.cosine_sim(response)
    #     return values 
       
    
    # def tools():
    #     return [MathTools.pre_process, MathTools.cosine_sim]
 