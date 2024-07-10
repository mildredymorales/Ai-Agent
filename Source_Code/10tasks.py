from crewai import Task

class BiologicalAnalysisTask10():
    def immune_response(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in immune response, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def metabolic_process(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in metabolic process, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def cell_cycle(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in the cell cycle, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def cell_comm(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in cell communication, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def signal_trans(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in signal transduction, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def apop(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in apoptosis, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def develop(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in development, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def repro(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in reproduction, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def transport(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in transport, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )
    def reg_biop(self, agent, genes):
        return Task(
            description = f"I will provide you with {genes}."
            "your task is to conduct a comprehensive biological analysis based on your expertise."
            "Gather detailed information on the role of each gene in regulation of biological processes, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that highlight their functions and interactions.",
            agent = agent,
            expected_output = "500 word count of biological information based on the genes",
        )