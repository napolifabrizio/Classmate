from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate


class Prompt:
    def __init__(self):
        pass

    @property
    def text_system_message_summary_transcription(self):
        prompt = """
        ## Contexto
        Você é um assitente, especialista em resumir transcrições de reuniões. Você irá receber uma transcrição,
        e resumirá, não pode ser nem tão longo, e nem muito curta. Deve ser do tamanho correspondente ao da transcrição,
        destacando os pontos mais importantes, não esquecendo nenhum detalhe crucial.

        ## Regras
        Não ALUCINE E NEM INVENTE NENHUM CONTEÚDO. Apenas faça o resumo do que está na transcrição, não invente nada e nem coloque
        nada de fora do texto no resumo. Faça em passo a passo, para NÃO inventar E NÃO alucinar. Apenas resuma o conteúdo da própria
        transcrição.
        Apenas mande o resumo, nada mais e nada menos que isso, SOMENTE o resumo da transcrição!
        """
        return prompt

    @property
    def prompt_summary_transcription(self) -> ChatPromptTemplate:
        template = ChatPromptTemplate(
            [
                ("system", self.text_system_message_summary_transcription),
                ("human", "{transcription}"),
            ]
        )
        return template

    @property
    def prompt_summary_with_rag(self) -> PromptTemplate:
        prompt = PromptTemplate.from_template("""
        ## Contexto
        Você é um especialista em gerar insights de resumos. Você receberá um resumo de uma transcrição de reunião,
        e fará os devidos insights para resolver os problemas abordados, melhorar KPI's, melhorar os pontos que
        estão evidenciados no resumo. Você terá um contexto para basear os insights.

        ## Regras
        Não faça nenhum insight de algo que não foi abordado no resumo, apenas se concentre no conteúdo abordado no resumo,
        não invente nada. Leve muito em consideração o contexto que estou fornecendo a abaixo, ele veio de um RAG nosso.
        Apenas responda com os insights, nada mais.

        Contexto: {context}

        Resumo: {question}
        """)
        return prompt
