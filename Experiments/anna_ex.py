import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

verbose_output = StringIO()
sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

term = 'immune response'

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

custom_task_1 = tasks.term(
    custom_agent_1, genes, term
)

custom_task_2 = tasks.compare_findings(
    custom_agent_11
)



# Define your custom crew here
crew = Crew(
        agents=[
            custom_agent_1, custom_agent_2, custom_agent_3,custom_agent_3,custom_agent_5,custom_agent_6,custom_agent_7,custom_agent_8,
            custom_agent_9,custom_agent_10, custom_agent_11, 
            ],
        tasks=[
            custom_task_1, custom_task_2
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