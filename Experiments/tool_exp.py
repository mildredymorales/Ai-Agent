import sys
from crewai import Agent, Task, Crew
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')
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

def pre_process(text: str) ->str:
        """This tool will clean and preprocess the text by structuring it for data analysis. The input is the agent response
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


def test_agent_execution_with_specific_tools():
	from langchain.tools import tool

	@tool
	def multiplier(numbers) -> float:
			"""Useful for when you need to multiply two numbers together.
			The input to this tool should be a comma separated list of numbers of
			length two, representing the two numbers you want to multiply together.
			For example, `1,2` would be the input if you wanted to multiply 1 by 2."""
			a, b = numbers.split(',')
			return int(a) * int(b)

	agent = Agent(
		role="test role",
		goal="test goal",
		backstory="test backstory",
		allow_delegation=False
	)

	output = agent.execute_task(
		task="What is 3 times 4",
		tools=[multiplier]
	)

"""
This file is just trying to play around for how tool implementation may work.
"""

sys.path.insert(0, '/Users/mildredmorales-paredes/Ai-Agent')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask
from Source_Code.tools import MathTools

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()
tools = MathTools()

# approach of human input 
print("## Welcome to the Biology Crew")
print('-------------------------------')



genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'


# agent = agents.__getattribute__(agent_name)()
# task = getattr(tasks, task_name)(agent, genes)

agent1 = Agent(
    role = 'storyteller',
    goal = "create original children stories",
    backstory = """ You are an experienced children storyteller.
    """,
    verbose = True,
    allow_delegation = False,
    llm = model
)

agent2 = Agent(
    role = 'Tool User',
    goal = "Use the tool",
    backstory = """ You are an experienced tool user.
    """,
    verbose = True,
    allow_delegation = False,
    llm = model
)

coding_agent = Agent(
    role="Senior Python Developer",
    goal="Craft well-designed and thought-out code",
    backstory="You are a senior Python developer with extensive experience in software architecture and best practices.",
    allow_code_execution=True,
    verbose = True,
    allow_delegation = False,
    llm = model
)

task1 = Task(
    description = f"create a unique children story that is fantasy and has great lessons",
    agent = agent1,
    expected_output = "500 words",
)

task2 = Task(
    description = f"create a unique children story that is fantasy and has great lessons",
    agent = agent1,
    expected_output = "500 words",
)

task3 = Task(
    description = f"preprocess the agent's response",
    agent = agent2,
    expected_output = "words",
    context = [task1],
    tools =[]
)

task4 = Task(
    description = f"Create code that calculates cosine similarity using tf-idf approach. Make sure to preprocess the text. Use the last agent's stories to compare as text similarity. Execute the code and compute the cosine similarity values",
    agent = coding_agent,
    expected_output = "code analysis",
    context = [task1, task2],
    # tools =[MathTools.pre_process]
)



# the output_log_file doesn't allow other print statements only what the agent's final answer is 
crew = Crew(
    agents=[agent1],
    tasks=[task1, task3],
    verbose=True,
    # output_log_file=log_path, # or could just say true 
    # task_callback= MathTools.callback_function
)


result = crew.kickoff()
print(result)
