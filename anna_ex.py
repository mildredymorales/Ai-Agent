import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from agents import BiologicalAgents
from tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

verbose_output = StringIO()
sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

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

# custom_agent_12 = agents.molgen_writer()



# Custom tasks include agent name and variables as input

# get information of genes first 
custom_task_1 = tasks.info_dump(
    custom_agent_1, genes,
)
custom_task_2 = tasks.info_dump(
    custom_agent_2, genes,
)
custom_task_3 = tasks.info_dump(
    custom_agent_3, genes,
)
custom_task_4 = tasks.info_dump(
    custom_agent_4, genes,
)
custom_task_5 = tasks.info_dump(
    custom_agent_5, genes,
)
custom_task_6 = tasks.info_dump(
    custom_agent_6, genes,
)
custom_task_7 = tasks.info_dump(
    custom_agent_7, genes,
)
custom_task_8 = tasks.info_dump(
    custom_agent_8, genes,
)
custom_task_9 = tasks.info_dump(
    custom_agent_9, genes,
)
custom_task_10 = tasks.info_dump(
    custom_agent_10, genes,
)

# hypothesize 

custom_task_11 = tasks.hypothesize(
    custom_agent_1, genes,
)
custom_task_12 = tasks.hypothesize(
    custom_agent_2, genes,
)
custom_task_13 = tasks.hypothesize(
    custom_agent_3, genes,
)
custom_task_14 = tasks.hypothesize(
    custom_agent_4, genes,
)
custom_task_15 = tasks.hypothesize(
    custom_agent_5, genes,
)
custom_task_16 = tasks.hypothesize(
    custom_agent_6, genes,
)
custom_task_17 = tasks.hypothesize(
    custom_agent_7, genes,
)
custom_task_18 = tasks.hypothesize(
    custom_agent_8, genes,
)
custom_task_19 = tasks.hypothesize(
    custom_agent_9, genes,
)
custom_task_20 = tasks.hypothesize(
    custom_agent_10, genes,
)


# compare agents 

custom_task_21 = tasks.compare_findings(
    custom_agent_11,
)

# summary
# custom_task_22 = tasks.summary(
#     custom_agent_12, genes,
# )



# Define your custom crew here
crew = Crew(
        agents=[
            custom_agent_1, custom_agent_2, custom_agent_3,custom_agent_3,custom_agent_5,custom_agent_6,custom_agent_7,custom_agent_8,
            custom_agent_9,custom_agent_10, custom_agent_11, 
            ],
        tasks=[
            custom_task_1, custom_task_11,custom_task_2,custom_task_12,custom_task_3,custom_task_13, custom_task_4,custom_task_14,custom_task_5,
            custom_task_15,custom_task_6, custom_task_16,custom_task_7,custom_task_17,custom_task_8,custom_task_18, custom_task_9,custom_task_19,custom_task_10,
            custom_task_20, custom_task_21
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