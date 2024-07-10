import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from agents import BiologicalAgents
from tasks import BiologicalAnalysisTask10

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

verbose_output = StringIO()
sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'C9orf152, PRR15L, FAM83E, JMJD1C-AS1, SSTR5-AS1, OTOGL, DOC2B, SLC17A1, SLC17A3, SLC51B, SLC5A9, PDZD3, SLC39A5, ANKS4B, MYO7B, FUT3'

# Define your custom agents and tasks here
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

custom_agent_11 = agents.compare_agent()


# Custom tasks include agent name and variables as input

# get information of genes first 
custom_task_1 = tasks.immune_response(
    custom_agent_1, genes,
)
custom_task_2 = tasks.metabolic_process(
    custom_agent_2, genes,
)
custom_task_3 = tasks.cell_cycle(
    custom_agent_3, genes,
)
custom_task_4 = tasks.cell_comm(
    custom_agent_4, genes,
)
custom_task_5 = tasks.signal_trans(
    custom_agent_5, genes,
)
custom_task_6 = tasks.apop(
    custom_agent_6, genes,
)
custom_task_7 = tasks.develop(
    custom_agent_7, genes,
)
custom_task_8 = tasks.repro(
    custom_agent_8, genes,
)
custom_task_9 = tasks.transport(
    custom_agent_9, genes,
)
custom_task_10 = tasks.reg_biop(
    custom_agent_10, genes,
)


# compare agents 

custom_task_21 = tasks.compare_findings(
    custom_agent_11, genes,
)

# Define your custom crew here
crew = Crew(
        agents= custom_agent_1,
        tasks=[
            custom_task_1, custom_task_2,custom_task_3,custom_task_4,custom_task_5,custom_task_6, custom_task_7,custom_task_8,custom_task_9,
            custom_task_10
            ],
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
with open('clade2log.txt', 'a') as verbose_file:
    verbose_file.write(verbose_output_content)