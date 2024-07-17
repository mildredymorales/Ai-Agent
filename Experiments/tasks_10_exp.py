import sys
from io import StringIO
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model='llama3')

from agents import BiologicalAgents
from tasks10 import Task10Analysis

agents = BiologicalAgents()
tasks10 = Task10Analysis()

print("## Welcome to the Biology Crew")
print('-------------------------------')

genes = 'GPR153, TMEM100, FRMPD1, ANKRD22, TMEM86A, UNC80, CLIC2, STEAP4, TROAP, DLGAP5, KIF20A, KIF18B, KIF14, PRSS12, RNASE1, RNASE4, TFPI2, GBP5, OASL, AGR2, CFAP70, METRNL, MANSC4'


# # Define your custom agents here
# cell_biol = agents.cellular_biologist()
# comp_biol = agents.computational_biologist()
# cell_exp = agents.cell_cyc()
# drug_devo = agents.drug_dev()
# epi_biol = agents.epigenetics_biologist()
# genereg_expe = agents.genereg_expert()
# mol_biol = agents.molecular_biologist()
# onco_rese = agents.onco_res()
# onco_phys = agents.oncologist_physician()
# systems_biol = agents.systems_biologist()

# custom_agents = [
#     cell_biol, comp_biol, cell_exp, drug_devo, epi_biol, genereg_expe, mol_biol, onco_rese, onco_phys, systems_biol
# ]

# # Define your custom tasks here
# imm_resp = tasks10.immune_response(
#     cell_biol, genes,
# )
# meta_proc = tasks10.metabolic_process(
#     cell_biol, genes,
# )
# cell_cycl = tasks10.cell_cycle(
#     cell_biol, genes,
# )
# cell_commu = tasks10.cell_comm(
#     cell_biol, genes,
# )
# sig_trans = tasks10.signal_trans(
#    cell_biol, genes,
# )
# apopt = tasks10.apop(
#     cell_biol, genes,
# )
# devel = tasks10.develop(
#     cell_biol, genes,
# )
# reprod = tasks10.repro(
#     cell_biol, genes,
# )
# transp = tasks10.transport(
#     cell_biol, genes,
# )
# regu_biop = tasks10.reg_biop(
#     cell_biol, genes,
# )

# task_definitions = [
#     imm_resp, meta_proc, cell_cycl, cell_commu, sig_trans, apopt, devel, reprod, transp, regu_biop
# ]

agent_names = [
    "cellular_biologist", "computational_biologist", "cell_cyc", "drug_dev",
    "epigenetics_biologist", "genereg_expert", "molecular_biologist", 
    "onco_res", "oncologist_physician", "systems_biologist"
]

agents_list = [agents.__getattribute__(name)() for name in agent_names]

task_names = [
    "apop", "cell_comm", "cell_cycle", "develop", "immune_response", 
    "metabolic_process", "reg_biop", "repro", "signal_trans", "transport"
]

tasks_list = [getattr(tasks10, task)(agent, genes) for agent, task in zip(agents_list, task_names)]

crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    verbose=True,
     process=Process.sequential,
    output_log_file='True', # or could write path
)

result = crew.kickoff()
print(result)


