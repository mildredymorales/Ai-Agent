from crewai import Crew, Task, Agent, Process
from langchain_community.llms import Ollama

model = Ollama(model='llama3')

genes = 'GBP5, OASL, ANKRD22, AGR2, LGALS4, KIF14, KIF20A, KIF18B, DLGAP5, TROAP, DEPDC1, PRR11'

farmer = Agent(
    role ="Humble Farmer",
    goal= "To keep your crops healthy and do business",
    backstory = f"""You are a humble farmer living in a valley. You have no education other than elementary school, and have very basic knowledge in biology.
    Your are mostly interested in weather forecasts and how it affects your crop gain. You meet a biology scientist one day that asks you questions about biology,
    in which you decide to answer him earnestly.""",
    verbose=True,
    allow_delegation=False,
    llm= model
)

cellular_biologist = Agent(
    role= "Cellular Biologist",
    goal= "To understand the connection between the {genes} in the sense of the pathway they are connected in",
    backstory= """You are an esteemed cellular biologist renowned for your extensive expertise in cellular pathways.
    With a Ph.D. in Cell Biology and decades of research experience, you have significantly contributed to understanding intricate cellular mechanisms.
    Your work encompasses a comprehensive analysis of signal transduction, metabolic pathways, and cellular responses to environmental stimuli.
    You are adept at utilizing advanced techniques such as single-cell RNA sequencing to uncover the dynamic processes within cells.
    Your research has led to groundbreaking discoveries in cell communication, intracellular trafficking, and regulatory networks, making you a leading authority in the field.
    You are also a prolific author, having published numerous high-impact papers and reviews, and are a sought-after speaker at international conferences.
    Your dedication to mentoring the next generation of scientists and your collaborative approach to research further underscore your status as a master in cellular biology.""",
    verbose = True,
    allow_delegation = False,
    llm = model

)

research1 = Task(
    description = f"Research the '{genes}' and make a hypothesis based on biological evidence",
    agent = farmer,
    expected_output = "50 word count of biological information based on the genes",
)

research2 = Task(
    description = f"Research the '{genes}' and make a hypothesis based on biological evidence",
    agent = cellular_biologist,
    expected_output = "50 word count of biological information based on the genes",
)

crew = Crew(
    agents = [farmer, cellular_biologist],
    tasks = [research1, research2],
    verbose = 0,
    process = Process.sequential
)

# Kick off the tasks
result = crew.kickoff()
print(result)