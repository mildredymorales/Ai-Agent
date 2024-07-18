from crewai import Crew, Process, Agent
from langchain_community.llms import Ollama
model = Ollama(model='llama3')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

# Initialize the agents and tasks
agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

# term = input("What is the the biological term you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name\n")

# Define the list of genes
genes = """DLGAP5, DEPDC1, KIF20A, TROAP, KIF18B, KIF2C, RRM2, CDC25C, CCNB2, KIF14, CENPF, PRR11, UBE2C, 
PIMREG, PTTG1, NEK2, HMMR, PLK1, AURKA, MND1, LGALS4, DEFB1, OASL""" # cell cycle genes

# List of agent names
agent_names = [
    "cellular_biologist", "computational_biologist", "cell_cyc", "drug_dev",
    "epigenetics_biologist", "genereg_expert", "molecular_biologist", 
    "onco_res", "oncologist_physician", "systems_biologist"
]

# Create instances of the agents
agents_list = [getattr(agents, name)() for name in agent_names]

# Define the task
tasks_list = []

# could change the actual tasks to the term task for human input 
# Append tasks for each agent
for agent in agents_list:
    tasks_list.append(tasks.cell_cycle(agent, genes))

# Create the Crew
crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    verbose=True,
    output_log_file='/Users/n4k/Ai-Agent/Results/one_it_log.txt', # or could just say true 
)

# Kick off the tasks
result = crew.kickoff()
print(result)


