# CrewAI Agent Repository

# Source Code 
This repository contains the necessary files to deploy and manage CrewAI Agents for biological analysis tasks. The source code directory includes classes for tasks and agents, facilitating tailored biological analyses. Additionally, a main template file is provided within this repository.

# Branch Overview
This branch is specialized for running cell cycle experiments. This branch focuses on testing to assess its variability and accuracy in executing tasks.

# Experiments
Within the experiments directory, an example file demonstrates clade analysis in relation to the cell cycle. There will be experiments with analyzing tasks with different parameters to see its effect on outputs. The task : term, is where this happens as the parameter for a terms is inputted there.

# Results
Results from conducted experiments are stored in the results folder, where log files are saved.

# Environment Setup

To set up the CrewAI environment using Conda, follow these steps:

bash
Copy code
conda create -n crewai python=3.12.3
conda activate crewai
pip install crewai
conda install -c conda-forge langchain-community

# Dependency Considerations
Previous challenges with charset-normalizer and pydantic versions have been resolved with specific versions:

charset-normalizer==3.3.2
pydantic==2.7.2

# Installing Ollama
Ollama can be downloaded and installed locally from GitHub.
