from langchain_community.document_loaders import TextLoader
from langchain.schema import Document


class Loader:
    def __init__(self):
        pass

    @staticmethod
    def make_document(page_content: str, name: str):
        document = Document(page_content=page_content, metadata={"name": name})
        return document

    def load_text_loader_from_path(self, path: str):
        loader = TextLoader(file_path=path, encoding="utf-8")
        documents = loader.load()
        return documents


if __name__ == "__main__":
    loader = Loader()
    document = loader.load_text_loader_from_path("source/classmate/RAG/data/training.md")
    print(document)
