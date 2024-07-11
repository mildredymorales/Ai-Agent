from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama
model = Ollama(model= 'llama3')

from textwrap import dedent
from agents import BiologicalAgents
from tasks import BiologicalAnalysisTask


class BiologicalAnalysisCrew:
    def __init__(self, list1):
        self.var1 = list1
        # self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = BiologicalAgents()
        tasks = BiologicalAnalysisTask()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.agent_1_name()
        custom_agent_2 = agents.agent_2_name()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.var1,
            # self.var2,
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
            self.var1,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2],
            tasks=[custom_task_1, custom_task_2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    list1 = input(dedent("""Enter list of genes 1: """))
    # var2 = input(dedent("""Enter variable 2: """))

    custom_crew = BiologicalAnalysisCrew(list1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
