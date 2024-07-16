import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

sys.path.insert(0, '/Users/mildredmorales-paredes/Ai-Agent')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

# Define your custom agents and tasks here
cell_bio_agent = agents.cellular_biologist()
comp_bio_agent = agents.computational_biologist()
cell_cyc_agent = agents.cell_cyc()
drug_dev_agent = agents.drug_dev()
epig_bio_agent = agents.epigenetics_biologist()
gene_reg_agent = agents.genereg_expert()
molec_bio_agent = agents.molecular_biologist()
onco_res_agent = agents.onco_res()
onco_phy_agent = agents.oncologist_physician()
sys_bio_agent = agents.systems_biologist()

analytical_agent = agents.compare_agent()




# Custom tasks include agent name and variables as input

# get information of genes first 
cell_bio_info_task = tasks.info_dump(
    cell_bio_agent, genes,
)
comp_bio_info_task = tasks.info_dump(
    comp_bio_agent, genes,
)
cell_cyc_info_task = tasks.info_dump(
    cell_cyc_agent, genes,
)
drug_dev_info_task = tasks.info_dump(
    drug_dev_agent, genes,
)
epig_bio_info_task = tasks.info_dump(
    epig_bio_agent, genes,
)
gene_reg_info_task = tasks.info_dump(
    gene_reg_agent, genes,
)
molec_bio_info_task = tasks.info_dump(
    molec_bio_agent, genes,
)
onco_res_info_task = tasks.info_dump(
    onco_res_agent, genes,
)
onco_phys_info_task = tasks.info_dump(
    onco_phy_agent, genes,
)
sys_bio_info_task = tasks.info_dump(
    sys_bio_agent, genes,
)

# hypothesize 

cell_bio_hyp_task = tasks.hypothesize(
    cell_bio_agent, genes,
)
comp_bio_hyp_task = tasks.hypothesize(
    comp_bio_agent, genes,
)
cell_cyc_hyp_task = tasks.hypothesize(
    cell_cyc_agent, genes,
)
drug_dev_hyp_task = tasks.hypothesize(
    drug_dev_agent, genes,
)
epig_bio_hyp_task = tasks.hypothesize(
    epig_bio_agent, genes,
)
gene_reg_hyp_task = tasks.hypothesize(
    gene_reg_agent, genes,
)
molec_bio_hyp_task = tasks.hypothesize(
    molec_bio_agent, genes,
)
onco_res_hyp_task = tasks.hypothesize(
    onco_res_agent, genes,
)
onco_phy_hyp_task = tasks.hypothesize(
    onco_phy_agent, genes,
)
sys_bio_hyp_task = tasks.hypothesize(
    sys_bio_agent, genes,
)


# compare agents 

ana_comp_task = tasks.compare_findings(
    analytical_agent,
)

# summary



# Define your custom crew here
crew = Crew(
        agents=[
            cell_bio_agent, comp_bio_agent, cell_cyc_agent, drug_dev_agent, epig_bio_agent, gene_reg_agent, molec_bio_agent, onco_res_agent,
            onco_phy_agent, sys_bio_agent, analytical_agent, 
            ],
        tasks=[
            cell_bio_info_task, cell_bio_hyp_task, comp_bio_info_task, comp_bio_hyp_task, cell_cyc_info_task, cell_cyc_hyp_task, drug_dev_info_task, drug_dev_hyp_task, epig_bio_info_task,
            epig_bio_hyp_task, gene_reg_info_task, gene_reg_hyp_task, molec_bio_info_task, molec_bio_hyp_task, onco_res_info_task, onco_res_hyp_task, onco_phys_info_task, onco_phy_hyp_task, sys_bio_info_task,
            sys_bio_hyp_task, ana_comp_task
            ],
        verbose=True,
        process = Process.sequential,
        output_log_file=True,
)



result = crew.kickoff()
print(result)