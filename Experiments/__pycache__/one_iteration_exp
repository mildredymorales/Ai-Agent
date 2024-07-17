import sys
from io import StringIO
from crewai import Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from Source_Code.agents import BiologicalAgents
from Source_Code.tasks import BiologicalAnalysisTask

agents = BiologicalAgents()
tasks = BiologicalAnalysisTask()

genes= """DLGAP5, DEPDC1, KIF20A, TROAP, KIF18B, KIF2C, RRM2, CDC25C, CCNB2, KIF14, CENPF, PRR11, UBE2C, 
PIMREG, PTTG1, NEK2, HMMR, PLK1, AURKA, MND1, LGALS4, DEFB1, OASL""" #cell cycle genes

agent_names = [
    "cellular_biologist", "computational_biologist", "cell_cyc", "drug_dev",
    "epigenetics_biologist", "genereg_expert", "molecular_biologist", 
    "onco_res", "oncologist_physician", "systems_biologist"
]

crew = Crew(
    agents= agent_names,
    tasks= tasks.cell_cycle,
    verbose=True,
    output_log_file='/Users/mildredmorales-paredes/Ai-Agent/Results/one_iteration.txt', # or could just say true 
    # memory=True,
    # manager_agent=manager,
    # process=Process.hierarchical
)
result = crew.kickoff()
print(result)
