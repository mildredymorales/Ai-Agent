from crewai import Task
from Source_Code.tools import MathTools
pre_process_tool = MathTools.pre_process
cosine_sim_tool = MathTools.cosine_sim

class BiologicalAnalysisTask():
    def term(self, agent, genes, term):
        return Task(
            description = f"""Your task is to conduct a comprehensive biological analysis of the {genes} based on your expertise. Gather detailed information on the role of each gene in each of 
            the biological process included in each of these terms: {term}, how these genes interact with each other, the pathways or mechanisms they are involved in, and relevant research findings and studies that 
            highlight their functions and interactions.""",
            agent = agent,
            expected_output = "a couple of paragraphs",
        )
    def immune_response(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in immune response,
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the immune response information on the genes",
        )
    def metabolic_process(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in metabolic process, how these genes interact with each other, 
            the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the metabolic process information on the genes",
        )
    def cell_cycle(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise."\
            Gather detailed information on the role of each gene in the cell cycle, 
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.
            Be original, don't take the same information given by the previous scientists.
            Gather information on {genes} by yourself.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the cell cycle information on the genes",
        )
    def cell_comm(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            "your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in cell communication, 
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the cell communication information on the genes",
        )
    def signal_trans(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in signal transduction, 
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the signal transduction information on the genes",
        )
    def apop(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in apoptosis, 
            how these genes interact with each other, the pathways or mechanisms they are involved in,
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the apoptosis information on the genes",
        )
    def develop(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in development, 
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the development information on the genes",
        )
    def repro(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in reproduction,
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the reproduction information on the genes",
        )
    def transport(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in transport,
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the gene transport information on the genes",
        )
    def reg_biop(self, agent, genes):
        return Task(
            description = f"""I will provide you with {genes}.
            your task is to conduct a comprehensive biological analysis based on your expertise.
            Gather detailed information on the role of each gene in regulation of biological processes, 
            how these genes interact with each other, the pathways or mechanisms they are involved in, 
            and relevant research findings and studies that highlight their functions and interactions.""",
            agent = agent,
            expected_output = "500 word count of biological information based on the regulation of biological processes information on the genes",
        )
    def tf_idf(self, agent, task):
        return Task(
            description = f"""Your task is to employ TF-IDF and cosine similarity. Beginning with 
            data preprocessing to standardize text and enhance relevance through TF-IDF weighting, you'll transform each agent response into a numerical vector. 
            By calculating cosine similarity between these vectors, you'll measure the similarity of the responses. The input of the tools is the {task}.""",
            agent = agent,
            expected_output = "a list of cosine similarity values for each agent response",
            tools=[pre_process_tool(task), cosine_sim_tool(task)],
            context = {task}
            # or try callback
        )