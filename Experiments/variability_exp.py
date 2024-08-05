import sys
import os
from crewai import Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

"""
This file is to look at the variability of an answer of an agent for one task with 10 iterations, 
eventually going through all the 10 tasks and agents
Once it is ran it will ask for input, e.g cell_cyc for agent and cell_cycle for task
"""

sys.path.insert(0, '/Users/mildredmorales-paredes/Ai-Agent')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask
# from Source_Code.tools import MathTools

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()
# tools = MathTools()

# approach of human input 
print("## Welcome to the Biology Crew")
print('-------------------------------')

user_path = input("Enter path for log file.\n")
agent_name = input("What is the the biological agent you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name.\n")
task_name = input("What is the the biological term you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name\n")

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'


agent = agents.__getattribute__(agent_name)()
task = getattr(tasks, task_name)(agent, genes)

# this doesn't use the tool properly, never does actual math, could try call back or a diff crew one using task_out.raw
# compare_agent = agents.data_scientist_agent()
# compare_task = tasks.tf_idf(compare_agent, task)

# log directory for full name 
directory_path = f"{user_path}/{task_name}"
log_filename = f"{task_name}_task_{agent_name}_agent_log.txt"
log_path = os.path.join(directory_path, log_filename)

# the output_log_file doesn't allow other print statements only what the agent's final answer is 
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    output_log_file=log_path, # or could just say true 
    # task_callback= MathTools.callback_function
)

# do 10 iterations 

# print("This log file looks at the cell cycle task done by the cellular bio agent")
for x in range(10):
    # print("NEW ITERATION STARTS HERE")
    result = crew.kickoff()
    print(result)


