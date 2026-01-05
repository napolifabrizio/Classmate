from langchain_text_splitters import MarkdownHeaderTextSplitter


class Spliter:
    def __init__(self):
        pass

    @property
    def markdown_spliter(self) -> MarkdownHeaderTextSplitter:
        header_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        markdown_spliter = MarkdownHeaderTextSplitter(headers_to_split_on=header_to_split_on)
        return markdown_spliter

    def formater_splited_documents(self, documents, extra_metadado: dict):
        for i, doc in enumerate(documents):
            doc.metadata['doc_id'] = i
            doc.metadata = doc.metadata | extra_metadado
        return documents
