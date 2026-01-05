from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


class VectorDB:
    def __init__(self):
        self._openAIEmbedding = OpenAIEmbeddings()

    @property
    def vector_db(self) -> Chroma:
        directory = "source/classmate/data/vector_db"
        vectorstore = Chroma(
            embedding_function=self._openAIEmbedding,
            persist_directory=directory,
        )
        return vectorstore

    def add_to_vector_db(self, documents) -> bool:
        self.vector_db.add_documents(documents=documents)
        return True

    def delete_vectors_by_name_and_area(self, name: str, area: str) -> bool:
        self.vector_db.delete(
            where={
                "$and": [
                    {"name": {"$eq": name}},
                    {"area": {"$eq": area}}
                ]
            }
        )
        return True

if __name__ == "__main__":
    from classmate.backend.infrastructure.environs import Environs
    environs = Environs()

    vector_db = VectorDB()
    works = vector_db.delete_vectors_by_name(name="test")
    print(works)
