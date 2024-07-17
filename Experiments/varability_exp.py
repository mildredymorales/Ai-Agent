import sys
from io import StringIO
from crewai import Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

"""
This file is to look at the variability of an answer of an agent for one task with 10 iterations, 
eventually going through all the 10 tasks and agents
"""

sys.path.insert(0, '/Users/mildredmorales-paredes/Ai-Agent')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

# genes = input("Insert the genes to be analyzed as a list?\n")
# term = input("What are the the biological terms you want it to specifically analyze as? Enter the list with double quotes separated by commas. \n")
agent = input("What are the the biological agents you want it to specifically analyze as? Enter the list with double quotes separated by commas. \n")
task = input("What are the the biological terms you want it to specifically analyze as? Enter the list with double quotes separated by commas. \n")

# biological_terms = [term.strip() for term in term.split(',')]

# converting list into a dictionary 
# term = {f"term {i+1}": term for i, term in enumerate(biological_terms)}

# Printing the resulting dictionary
# print(term)


print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

# term = {
#     "Immune response": "Immune response",
#     "Metabolic process": "Metabolic process",
#     "Cell cycle": "Cell cycle",
#     "Cell communication": "Cell communication",
#     "Signal transduction": "Signal transduction",
#     "Apoptosis": "Apoptosis",
#     "Development": "Development",
#     "Reproduction": "Reproduction",
#     "Transport": "Transport",
#     "Regulation of biological processes": "Regulation of biological processes"
# }

# make list of agents and tasks to loop over 
agent_names = [
    "cellular_biologist", "computational_biologist", "cell_cyc", "drug_dev",
    "epigenetics_biologist", "genereg_expert", "molecular_biologist", 
    "onco_res", "oncologist_physician", "systems_biologist"
]

agents_list = [agents.__getattribute__(name)() for name in agent_names]

task_names = [
    "apop", "cell_comm", "cell_cycle", "develop", "immune_response", 
    "metabolic_process", "reg_biop", "repo", "signal_trans", "transport"
]

# Define your tasks here
tasks_list = [tasks.__getattribute__(name)() for name in task_names]

for task in tasks_list:
    for agent in agents_list:
        tasks_list.append(tasks(agent, genes))


crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    verbose=True,
    output_log_file='/Users/mildredmorales-paredes/Ai-Agent/Results/var_log.txt', # or could just say true 
)


result = crew.kickoff()
print(result)


# Accessing the task output
# task_output = tasks_list[1].output

# print(f"Task Description: {task_output.description}")
# print(f"Task Summary: {task_output.summary}")
# print(f"Raw Output: {task_output.raw}")

    