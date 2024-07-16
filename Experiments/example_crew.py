import sys
from io import StringIO
from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process


# verbose_output = StringIO()
# sys.stdout = verbose_output

model = Ollama(model= 'llama3')
 
genes = 'INSM1, HES1, STK17B, TRIB1, HS3ST1, DSC2, SLC12A1, HECTD2, OPRM1, NEUROD6'

 
research_agent = Agent(
    role = 'researcher',
    goal = "based on the list of genes, provide the significance if the gene's relationship and function to each other based on researched biological data",
    backstory = 'You are an unconfident biologist scientist who studies human genes and disease.You are unprepared and have impsoter syndrome, who is tasked to analyze clades.',
    allow_delegation = False,
    llm = model
)
 
reviewer_agent = Agent(
    role = 'reviewer',
    goal = "based on the summary, review, edit, and fact-check so it is biologically significant",
    backstory = """You are an esteemed senior biological scientist specializing in the study of human genes and diseases. With years of dedicated research experience, you possess a 
    profound understanding of genetic mechanisms and their implications in various diseases. Your expertise extends to critically analyzing and interpreting scientific publications, 
    ensuring accuracy, coherence, and relevance in complex biological contexts. As an editor and reviewer, you excel in meticulously fact-checking and enhancing scientific manuscripts, 
    adept at distilling intricate scientific findings into clear and concise summaries. Your role involves not only ensuring the scientific integrity of publications but also making them 
    accessible to a broader audience by simplifying complex biological concepts without compromising accuracy.""",
    verbose = True,
    allow_delegation = False,
    llm = model
)


read_genes = Task(
    description = f"Research the '{genes}' and make a hypothesis based on biological evidence",
    agent = research_agent,
    expected_output = "1000 word count of biological information based on the genes",
)

write_summary = Task(
    description = f"write a summary that explains the gene's relationship and function to each other based on the research '{genes}'",
    agent = research_agent,
    expected_output = "500 words",
)

review_summary = Task(
    description = f"review, edit, and fact-check the summary that explains the gene's relationship and function to each other based on the research '{genes}'. 
    structure the summary in an efficient way. make sure there is enough context for biologists of all backgrounds. include author and date for the information gathered",
    agent = reviewer_agent,
    expected_output = "300 words",
)

 
crew = Crew(
    agents = [research_agent, reviewer_agent],
    tasks = [read_genes, write_summary, review_summary],
    verbose = 0,
    process = Process.sequential, 
    output_log_file=True,
)
 
output = crew.kickoff()
print(output)

# # automatically log
# sys.stdout = sys.__stdout__
# verbose_output.seek(0)
# verbose_output_content = verbose_output.read()
# print(verbose_output_content)
# with open('verbose.txt', 'a') as verbose_file:
#     verbose_file.write(verbose_output_content)

# # only output
# with open('output.txt', 'a') as output_file:
#     output_file.write(output)




