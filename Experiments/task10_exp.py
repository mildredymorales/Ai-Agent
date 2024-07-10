import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from agents import BiologicalAgents
from tasks10 import Task10Analysis

agents = BiologicalAgents()
tasks10 = Task10Analysis()

verbose_output = StringIO()
sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GPR153, TMEM100, FRMPD1, ANKRD22, TMEM86A, UNC80, CLIC2, STEAP4, TROAP, DLGAP5, KIF20A, KIF18B, KIF14,  PRSS12, RNASE1, RNASE4, TFPI2, GBP5, OASL, AGR2, CFAP70, METRNL, MANSC4'

# Define your custom agents here
custom_agents = [
    agents.cellular_biologist(),
    agents.computational_biologist(),
    agents.cell_cyc(),
    agents.drug_dev(),
    agents.epigenetics_biologist(),
    agents.genereg_expert(),
    agents.molecular_biologist(),
    agents.onco_res(),
    agents.oncologist_physician(),
    agents.systems_biologist()
]

# Define your custom tasks here
task_definitions = [
    tasks10.immune_response,
    tasks10.metabolic_process,
    tasks10.cell_cycle,
    tasks10.cell_comm,
    tasks10.signal_trans,
    tasks10.apop,
    tasks10.develop,
    tasks10.repro,
    tasks10.transport,
    tasks10.reg_biop
]

# Create a list of task instances for each agent
task_instances = [[task(agent, genes) for task in task_definitions] for agent in custom_agents]

# Define your custom crew here
crew = Crew(
    agents=custom_agents,
    tasks=task_instances,
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print(result)

# automatically log
sys.stdout = sys.__stdout__
verbose_output.seek(0)
verbose_output_content = verbose_output.read()
print(verbose_output_content)
with open('10taskslog.txt', 'a') as verbose_file:
    verbose_file.write(verbose_output_content)
