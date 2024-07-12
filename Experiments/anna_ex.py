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

# genes = input("Insert the genes to be analyzed as a list?\n")
# term = input("What is the the biological term you want it to specifically analyze as?\n")

verbose_output = StringIO()
sys.stdout = verbose_output

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

term = {
    "Immune response": "Immune response",
    "Metabolic process": "Metabolic process",
    "Cell cycle": "Cell cycle",
    "Cell communication": "Cell communication",
    "Signal transduction": "Signal transduction",
    "Apoptosis": "Apoptosis",
    "Development": "Development",
    "Reproduction": "Reproduction",
    "Transport": "Transport",
    "Regulation of biological processes": "Regulation of biological processes"
}

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

# analytical_agent = agents.compare_agent()

# cell_bio_task = tasks.term(
#     cell_bio_agent, genes, term
# )
# comp_bio_task = tasks.term(
#     comp_bio_agent, genes, term
# )
# cell_cyc_task = tasks.term(
#     cell_cyc_agent, genes, term
# )
# drug_dev_task = tasks.term(
#     drug_dev_agent, genes, term
# )
# epig_bio_task = tasks.term(
#     epig_bio_agent, genes, term
# )
# gene_reg_task = tasks.term(
#     gene_reg_agent, genes, term
# )
# mol_bio_task = tasks.term(
#     molec_bio_agent, genes, term
# )
# onco_res_task = tasks.term(
#     onco_res_agent, genes, term
# )
# onco_phy_task = tasks.term(
#     onco_phy_agent, genes, term
# )
# sys_bio_task = tasks.term(
#     sys_bio_agent, genes, term
# )

analytical_agent = agents.compare_agent()
manager = agents.manager()

agent_names = [
    "cellular_biologist", "computational_biologist", "cell_cyc", "drug_dev",
    "epigenetics_biologist", "genereg_expert", "molecular_biologist", 
    "onco_res", "oncologist_physician", "systems_biologist"
]


agents_list = [agents.__getattribute__(name)() for name in agent_names]

# Define your tasks here
tasks_list = []
for agent in agents_list:
    tasks_list.append(tasks.term(agent, genes, term))

compare_task = tasks.compare_findings(analytical_agent)


compare_task = tasks.compare_findings(
    analytical_agent
)

# Define your custom crew here
# crew = Crew(
#         agents=[
#             cell_bio_agent, comp_bio_agent, cell_cyc_agent, drug_dev_agent, epig_bio_agent, gene_reg_agent, molec_bio_agent, onco_res_agent,
#             onco_phy_agent, sys_bio_agent, analytical_agent, 
#             ],
#         tasks=[
#             cell_bio_task, comp_bio_task, cell_cyc_task, drug_dev_task, epig_bio_task, gene_reg_task, mol_bio_task, onco_res_task, onco_phy_task, onco_phy_task, sys_bio_task, compare_task,
#             ],
#         verbose=True,
#         process = Process.sequential
# )

crew = Crew(
    agents=agents_list + [analytical_agent],
    tasks=tasks_list + [compare_task],
    verbose=True,
    manager_agent=None,
    process=Process.hierarchical
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