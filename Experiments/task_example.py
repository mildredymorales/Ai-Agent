from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process



model = Ollama(model= 'llama3')
 
genes = 'INSM1, HES1, STK17B, TRIB1, HS3ST1, DSC2, SLC12A1, HECTD2, OPRM1, NEUROD6'

 
research_agent = Agent(
    role = 'researcher',
    goal = "based on the list of genes, provide the significance of the gene's relationship and function to each other based on researched biological data",
    backstory = 'You are an confident biologist scientist who studies human genes and disease. You are yo analyze sets of genes. ',
    allow_delegation = False,
    llm = model
)

bad_task = Task(
    description = f"""Analyze a bunch of '{genes}' and figure out if they are important. Try to see if they are related to each other somehow. 
    Write a summary of what you discovered about the genes and their connections.""",
    agent = research_agent,
    expected_output = "a couple of paragraphs",
)

good_task = Task(
    description = f"""The objective of this task is to conduct a comprehensive analysis of a specified '{genes}' to elucidate its biological significance and identify potential 
    relationships within the context of a given biological framework. Perform functional enrichment analyses to interpret the biological roles of the genes. 
    This includes Gene Ontology (GO) enrichment to ascertain which biological processes, molecular functions, and cellular components are overrepresented. Additionally, 
    conduct pathway analysis using databases like KEGG or Reactome to map the DEGs to known biological pathways, thereby elucidating their potential roles in specific 
    biological processes or diseases. Inteigrate these findngs to explore the relationships between the genes, looking at how they interact within the pathways and processes identified.
    The final deliverable should provide a thorough understanding of the gene set's biological relevance and its implications for further research or clinical applications.""",
    agent = research_agent,
    expected_output = "a report with multiple pages",
)


 
crew = Crew(
    agents = [research_agent],
    tasks = [good_task],
    verbose = True,
    process = Process.sequential, 
    output_log_file=True,
)
 
output = crew.kickoff()
print(output)



