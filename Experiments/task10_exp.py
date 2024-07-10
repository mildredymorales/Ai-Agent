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
custom_agent_1 = agents.cellular_biologist()
custom_agent_2 = agents.computational_biologist()
custom_agent_3 = agents.cell_cyc()
custom_agent_4 = agents.drug_dev()
custom_agent_5 = agents.epigenetics_biologist()
custom_agent_6 = agents.genereg_expert()
custom_agent_7 = agents.molecular_biologist()
custom_agent_8 = agents.onco_res()
custom_agent_9 = agents.oncologist_physician()
custom_agent_10 = agents.systems_biologist()


custom_agents = [
    custom_agent_1, custom_agent_2, custom_agent_3,custom_agent_3,custom_agent_5,custom_agent_6,custom_agent_7,custom_agent_8, custom_agent_9,custom_agent_10
]

# Define your custom tasks here
custom_task_1 = tasks10.immune_response(
    custom_agents, genes,
)
custom_task_2 = tasks10.metabolic_process(
    custom_agents, genes,
)
custom_task_3 = tasks10.cell_cycle(
    custom_agents, genes,
)
custom_task_4 = tasks10.cell_comm(
    custom_agents, genes,
)
custom_task_5 = tasks10.signal_trans(
    custom_agents, genes,
)
custom_task_6 = tasks10.apop(
    custom_agents, genes,
)
custom_task_7 = tasks10.develop(
    custom_agents, genes,
)
custom_task_8 = tasks10.repro(
    custom_agents, genes,
)
custom_task_9 = tasks10.transport(
    custom_agents, genes,
)
custom_task_10 = tasks10.reg_biop(
    custom_agents, genes,
)

task_definitions = [ custom_task_1, custom_task_2, custom_task_3, custom_task_4, custom_task_5, custom_task_6, custom_task_7, custom_task_8, custom_task_9, custom_task_10
]

crew = Crew(
        agents= custom_agents,
        tasks= task_definitions,
        verbose=True,
        process = Process.sequential
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
