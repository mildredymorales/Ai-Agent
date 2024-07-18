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

# approach of human input 
print("## Welcome to the Biology Crew")
print('-------------------------------')


agent_name = input("What is the the biological agent you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name.\n")
task_name = input("What is the the biological term you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name\n")

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'


# Define your custom agents and tasks here
# cell_bio_agent = agents.cellular_biologist()
# comp_bio_agent = agents.computational_biologist()
# cell_cyc_agent = agents.cell_cyc()
# drug_dev_agent = agents.drug_dev()
# epig_bio_agent = agents.epigenetics_biologist()
# gene_reg_agent = agents.genereg_expert()
# molec_bio_agent = agents.molecular_biologist()
# onco_res_agent = agents.onco_res()
# onco_phy_agent = agents.oncologist_physician()
# sys_bio_agent = agents.systems_biologist()


# cell_cyc_task = tasks.cell_cycle(
#     agent, genes, 
# )
# print(cell_cyc_task)
# cell_com_task = tasks.cell_comm(
#     agent, genes,
# )
# apop_task = tasks.apop(
#     agent, genes, 
# )
# dev_task = tasks.develop(
#     agent, genes, 
# )
# immune_res_task = tasks.immune_response(
#     agent, genes, 
# )
# meta_pro_task = tasks.metabolic_process(
#     agent, genes,
# )
# reg_bio_task = tasks.reg_biop(
#     agent, genes, 
# )
# repro_task = tasks.repro(
#     agent, genes, 
# )
# sig_tans_task = tasks.signal_trans(
#     agent, genes, 
# )
# transport_task = tasks.transport(
#     agent, genes,
# )

agent = agents.__getattribute__(agent_name)()
print(agent)

task = getattr(tasks, task_name)(agent, genes)



# do 10 iterations 

# the output_log_file doesn't allow other print statements only what the agent's final answer is 


crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    output_log_file='/Users/mildredmorales-paredes/Ai-Agent/Results/{task_name}_task_{agent}_agent_log.txt', # or could just say true 
)

# print("This log file looks at the cell cycle task done by the cellular bio agent")
for x in range(10):
    # print("NEW ITERATION STARTS HERE")
    result = crew.kickoff()
    print(result)



# Accessing the task output
# task_output = tasks_list[1].output

# print(f"Task Description: {task_output.description}")
# print(f"Task Summary: {task_output.summary}")
# print(f"Raw Output: {task_output.raw}")

    