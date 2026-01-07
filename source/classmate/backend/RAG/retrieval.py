from langchain.chains.retrieval_qa.base import RetrievalQA, BaseRetrievalQA
from classmate.backend.RAG import VectorDB

from langchain_openai import ChatOpenAI

class Retrieval:
    def __init__(self):
        self._vectorDB = VectorDB()
        self._chat = ChatOpenAI(model="gpt-4o-mini")

    def filter_area_metadata(self, area: str):
        retriever_filter = {'area': {'$in': [area]}}

        return retriever_filter

    def chat_retriver_own_prompt(self, prompt: str, area: str) -> BaseRetrievalQA:
        area_filter = self.filter_area_metadata(area)
        retriever = self._vectorDB.vector_db.as_retriever(search_type='mmr', search_kwargs={"k": 10, "fetch_k": 20, "filter": area_filter})
        chat_chain = RetrievalQA.from_chain_type(
            llm=self._chat,
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt},
        )
        return chat_chain

    def chat_retriver(self, area: str) -> BaseRetrievalQA:
        area_filter = self.filter_area_metadata(area)
        retriever = self.vector_db.as_retriever(search_type='mmr', search_kwargs={"k": 3, "fetch_k": 10, "filter": area_filter})
        chat_chain = RetrievalQA.from_chain_type(
            llm=self._chat,
            retriever=retriever,
        )
        return chat_chain
