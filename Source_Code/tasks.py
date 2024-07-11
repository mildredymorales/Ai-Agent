from crewai import Task

class BiologicalAnalysisTask():
    def research(self, agent, genes):
        return Task(
            description = f"Research the '{genes}' and make a hypothesis based on biological                      evidence",
            agent = agent,
            expected_output = "1000 word count of biological information based on the genes",
        )

    def summary(self, agent, genes): 
        return Task(
            description = f"write a summary that explains the gene's relationship and function to                 each other based on the research '{genes}'",
            agent = agent,
            expected_output = "500 words",
        )

    def review_summary(self, agent, genes):
        return Task(
            description = f"review, edit, and fact-check the summary that explains the gene's                     relationship and function to each other based on the research '{genes}'. structure the                summary in an efficient way. make sure there is enough context for biologists of all                  backgrounds. include author and date for the information gathered",
            agent = agent,
            expected_output = "300 words",
        )
