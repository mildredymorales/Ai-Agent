from crewai import Task

class BiologicalAnalysisTask():
    def summary(self, agent, genes): 
        return Task(
            description = f"write a summary based on the biologicl analysis done on the '{genes}, write a paragraph for each gene in the list.'",
            agent = agent,
            expected_output = "a couple of paragraphs words",
        )

    def review_summary(self, agent, genes):
        return Task(
            description = f"review, edit, and fact-check the summary that explains the gene's relationship and function to each other based on the research '{genes}'. structure the summary in an efficient way. make sure there is enough context for biologists of all backgrounds. include author and date for the information gathered",
            agent = agent,
            expected_output = "300 words",
        )
    
    def hypothesize(self, agent, genes):
        return Task(
            description = f"your mission is to conduct biological analysis of the '{genes}' based on the information already given to you. Create a hypothesis of these genes as a whole clade in regards to the cell cycle and other context if a gene isn't relevant to the cell cycle. Hypothesize their relationship, interaction, significance, context  within your respective fields. Give a biological mechanism for this clade.",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
    
    def info_dump(self, agent, genes):
        return Task(
            description = f"your mission is to gather all the biological, enrichment, context dependent information on the '{genes}' that can be found. Give the author, date, and other references for where the information is given. Even if there is no information on the gene, keep exploring and note the limited information.",
            agent = agent,
            expected_output = "1000 words",
        )
    
    def compare_findings(self, agent):
        return Task(
            description = f"Your mission is to analyze and compare the conclusions drawn by each of the 10 biological agents that previously analyzed the clade of genes. Based on their analysis of the genetic data use the cosine similarity between TF-IDF vectors to calculate.",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
    
    def term(self, agent, genes, term):
        return Task(
            description = f"Your task is to conduct a comprehensive biological analysis based on your expertise. Gather detailed information on the role of each gene in the biological process of {term}, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
