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
cell_biol = agents.cellular_biologist()
comp_biol = agents.computational_biologist()
cell_exp = agents.cell_cyc()
drug_devo = agents.drug_dev()
epi_biol = agents.epigenetics_biologist()
genereg_expe = agents.genereg_expert()
mol_biol = agents.molecular_biologist()
onco_rese = agents.onco_res()
onco_phys = agents.oncologist_physician()
systems_biol = agents.systems_biologist()


custom_agents = [
    cell_biol, comp_biol, cell_exp,drug_devo,epi_biol,genereg_expe,mol_biol,onco_rese, onco_phys,systems_biol
]

# Define your custom tasks here
imm_resp = tasks10.immune_response(
    custom_agents, genes,
)
meta_proc = tasks10.metabolic_process(
    custom_agents, genes,
)
cell_cycl = tasks10.cell_cycle(
    custom_agents, genes,
)
cell_commu = tasks10.cell_comm(
    custom_agents, genes,
)
sig_trans = tasks10.signal_trans(
    custom_agents, genes,
)
apopt = tasks10.apop(
    custom_agents, genes,
)
devel = tasks10.develop(
    custom_agents, genes,
)
reprod = tasks10.repro(
    custom_agents, genes,
)
transp = tasks10.transport(
    custom_agents, genes,
)
regu_biop = tasks10.reg_biop(
    custom_agents, genes,
)

task_definitions = [ imm_resp, meta_proc, cell_cycl, cell_commu, sig_trans, apopt, devel, reprod, transp, regu_biop
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
