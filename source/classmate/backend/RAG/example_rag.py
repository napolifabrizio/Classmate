from classmate.backend.infrastructure.environs import Environs

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA, BaseRetrievalQA

environs = Environs()

path = "source/classmate/data/training.md"

class RAG:
    def __init__(self, path: str = None):
        self._source = path
        self._chat = ChatOpenAI(model="gpt-3.5-turbo-0125")

    @property
    def text_loader(self) -> TextLoader:
        return TextLoader(self._source, encoding="utf-8")

    @property
    def load_text_loader(self):
        documents = self.text_loader.load()
        return documents

    def markdown_spliter(self) -> MarkdownHeaderTextSplitter:
        header_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        markdown_spliter = MarkdownHeaderTextSplitter(headers_to_split_on=header_to_split_on)
        return markdown_spliter

    def formater_splited_documents(self, documents):
        for i, doc in enumerate(documents):
            doc.metadata['source'] = ""
            doc.metadata['doc_id'] = i
        return documents

    @property
    def vector_db(self) -> Chroma:
        directory = "source/classmate/infrastructure/vector_db"
        embedding_model = OpenAIEmbeddings()
        vectorstore = Chroma(
            embedding_function=embedding_model,
            persist_directory=directory,
        )
        return vectorstore

    def add_to_vector_db(self, documents) -> None:
        self.vector_db.add_documents(documents=documents)

    def chat_retriver(self, prompt = None) -> BaseRetrievalQA:
        retriever = self.vector_db.as_retriever(search_type='mmr', search_kwargs={"k": 3, "fetch_k": 10})
        if prompt:
            chat_chain = RetrievalQA.from_chain_type(
                llm=self._chat,
                retriever=retriever,
                chain_type_kwargs={"prompt": prompt},
            )
        else:
            chat_chain = RetrievalQA.from_chain_type(
                llm=self._chat,
                retriever=retriever,
            )
        return chat_chain

if __name__ == "__main__":
    rag = RAG(path=path)

    # Adicionar um documento á tabela

    # documents = rag.load_text_loader
    # spliter = rag.markdown_spliter()

    # splited_documents = spliter.split_text(documents[0].page_content)
    # splited_documents = rag.formater_splited_documents(splited_documents)
    # rag.add_to_vector_db(splited_documents)
