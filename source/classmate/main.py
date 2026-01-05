from langchain.prompts import PromptTemplate

from classmate.backend.chains.chain_summary import ChainSummary, transcription_example
from classmate.backend.RAG.example_rag import RAG

chain_summary = ChainSummary()
prompt_summary = chain_summary.generate_summary(transcription_example)

# path = "source/classmate/data/training.md"
rag = RAG()
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

res = rag.chat_retriver(prompt).invoke({"query": prompt_summary})
print(res)
