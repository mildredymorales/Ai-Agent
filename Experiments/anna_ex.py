import sys
from io import StringIO
from crewai import Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

sys.path.insert(0, '/Users/mildredmorales-paredes/Ai-Agent')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()


print("## Welcome to the Biology Crew")
print('-------------------------------')



genes = input("Insert the genes to be analyzed as a list?\n")

term = input("What is the the biological term you want it to specifically analyze as?\n")

verbose_output = StringIO()
sys.stdout = verbose_output

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
custom_task_2 = tasks.term(
    custom_agent_2, genes, term
)
custom_task_3 = tasks.term(
    custom_agent_3, genes, term
)
custom_task_4 = tasks.term(
    custom_agent_4, genes, term
)
custom_task_5 = tasks.term(
    custom_agent_5, genes, term
)
custom_task_6 = tasks.term(
    custom_agent_6, genes, term
)
custom_task_7 = tasks.term(
    custom_agent_7, genes, term
)
custom_task_8 = tasks.term(
    custom_agent_8, genes, term
)
custom_task_9 = tasks.term(
    custom_agent_9, genes, term
)
custom_task_10 = tasks.term(
    custom_agent_10, genes, term
)


custom_task_11 = tasks.compare_findings(
    custom_agent_11
)

# Define your custom crew here
crew = Crew(
        agents=[
            custom_agent_1, custom_agent_2, custom_agent_3,custom_agent_3,custom_agent_5,custom_agent_6,custom_agent_7,custom_agent_8,
            custom_agent_9,custom_agent_10, custom_agent_11, 
            ],
        tasks=[
            custom_task_1, custom_task_2, custom_task_3, custom_task_4, custom_task_5, custom_task_6, custom_task_7, custom_task_8, custom_task_9, custom_task_10, custom_task_11,
            ],
        verbose=True,
        process = Process.sequential
)



result = crew.kickoff()
print(result)

results_dir = '/Users/mildredmorales-paredes/Ai-Agent/Results/term.txt'

# automatically log
sys.stdout = sys.__stdout__
verbose_output.seek(0)
verbose_output_content = verbose_output.read()
print(verbose_output_content)
with open(results_dir, 'a') as verbose_file:
    verbose_file.write(verbose_output_content)