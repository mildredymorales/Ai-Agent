# CrewAI Agent Repository

# Source Code
This repository contains the necessary files to deploy and manage CrewAI Agents for biological analysis on a set of genes. The source code directory includes classes for tasks, agents, and tools. Additionally, a main template file is provided within this repository. The agents.py file contains 10 biological scientists along with a reviewer agent and a data scientist. There are also 10 tasks focused on different biological signficant terms to analyze the genes in respect to. The tools file is a copy of the TF-IDF Code mentioned down below. 

# Branch Overview
This is the iterations branch which focuses on running and saving experiments that have multiple iterations to analyze variability of ai agents' responses to see how efficient and precise they are.

# Experiments
Within the experiments directory, there are two experiments. The variability_exp.py focuses on an experiment of running one task and one agent at a time for 10 iterations. The one_teration_ex.py focuses on an experiment of one task with all 10 agents at once for only one iteration. The former file has input parameters once run. You must enter which agent you want to analyze and what task. An example:
> % python3 variability_exp.py
## Welcome to the Biology Crew
-------------------------------
What is the the biological agent you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name.
> drug_dev
What is the the biological term you want it to specifically analyze as? Please enter with NO quotes. For now it is sensitive so enter the exact function name
> cell_comm

# Results
Results from conducted experiments are stored in the results folder automatically from the experiment files. There are folders for each task, which contains the multiple runs for each agent using variability_exp.py

# TF IDF Analysis
To analyze the agents' responses we are taking an TF-IDF approach to compute cosine similarities. The cosine_sim.py contains the code for a simple experiment for text similarity. To run the code it expects a file that includes all the responses, in which it will then separate the responses by using a phrase. Then it will preprocess all of the responses, and using TF-IDF vectorization it calculates cosine similarity values for every response against each other. 

# Environment Setup
To set up the CrewAI environment using Conda, follow these steps:

bash Copy code conda create -n crewai python=3.12.3 conda activate crewai pip install crewai conda install -c conda-forge langchain-community

# Dependency Considerations
Previous challenges with charset-normalizer and pydantic versions have been resolved with specific versions:

charset-normalizer==3.3.2 pydantic==2.7.2

# Installing Ollama
Ollama can be downloaded and installed locally from GitHub.
