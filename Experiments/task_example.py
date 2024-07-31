from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process



model = Ollama(model= 'llama3')
 
genes = 'INSM1, HES1, STK17B, TRIB1, HS3ST1, DSC2, SLC12A1, HECTD2, OPRM1, NEUROD6'

 
research_agent = Agent(
    role = 'researcher',
    goal = """based on the list of genes, provide the significance of the gene's relationship 
    and function to each other based on researched biological data.""",
    backstory = """You are an confident biologist scientist who studies human genes and disease. 
    You are to analyze sets of genes.""",
    allow_delegation = False,
    llm = model
)
short_task = Task(
    description = f"""Analyze a bunch of '{genes}' and figure out if they are important. 
    Try to see if they are related to each other somehow.""",
    agent = research_agent,
    expected_output = "a couple of paragraphs",
)
long_task = Task(
    description = f"""The objective of this task is to perform a detailed analysis of the 
    {genes}`to uncover its biological significance and identify potential relationships 
    within a defined biological framework. This involves examining specific gene interactions, 
    mapping these genes to relevant biological pathways, and exploring their roles in cellular 
    processes. Additionally, the analysis should include hypotheses about less understood or 
    novel interactions. The final deliverable should be a comprehensive report that 
    integrates these findings, providing a thorough understanding of the genes biological 
    relevance""",
    agent = research_agent,
    expected_output = "a couple of paragraphs",
)


 
crew = Crew(
    agents = [research_agent],
    tasks = [long_task],
    verbose = True,
    process = Process.sequential, 
    output_log_file=True,
)
 
output = crew.kickoff()
print(output)



