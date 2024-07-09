from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from agents import BiologicalAgents
from tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

genes = input("What is the list of genes you want to analyze?\n")

# Define your custom agents and tasks here
custom_agent_1 = agents.agent_1_name()
custom_agent_2 = agents.agent_2_name()

# Custom tasks include agent name and variables as input
custom_task_1 = tasks.task_1_name(
    custom_agent_1, genes,
)

custom_task_2 = tasks.task_2_name(
    custom_agent_2, genes,
)

# Define your custom crew here
crew = Crew(
        agents=[custom_agent_1, custom_agent_2],
        tasks=[custom_task_1, custom_task_2],
        verbose=True,
)

result = crew.kickoff()
print(result)
