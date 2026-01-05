from classmate.backend.RAG import Loader, Spliter, VectorDB, Retrieval
from classmate.backend.models import UserInputRag
from classmate.backend.prompts.prompt import Prompt
from classmate.backend.chains.chain_summary import ChainSummary

class Rag:
    def __init__(self):
        self._loader = Loader()
        self._spliter = Spliter()
        self._vectorDb = VectorDB()
        self._retrieval = Retrieval()
        self._prompt = Prompt()
        self._chainSummary = ChainSummary()

    def default_save_txt_file(self, input_rag: UserInputRag):
        """
        Função default para salvar arquivos txt. \n
        Com split e formatação dos vetores já predefinido, sem customização. \n
        Apenas passe o conteúdo e nome de identificação.
        """
        try:
            extra_metadado = {"name": input_rag.Name, "area": input_rag.Area}
            splited = self._spliter.markdown_spliter.split_text(input_rag.Content)
            formatted_splited = self._spliter.formater_splited_documents(splited, extra_metadado)
            self._vectorDb.add_to_vector_db(formatted_splited)
            return True
        except Exception as err:
            raise Exception(f"Erro desconhecido: {err}")

    def default_delete_vector(self, file_name: str, area: str) -> bool:
        self._vectorDb.delete_vectors_by_name_and_area(name=file_name, area=area)
        return True

    def chat_retriever(self, transcription: str, area: str):
        retriever = self._retrieval.chat_retriver_own_prompt(self._prompt.prompt_summary_with_rag, area)
        summary = self._chainSummary.generate_summary(transcription)
        res = retriever.invoke({"query": summary})
        return res

if __name__ == "__main__":
    rag = Rag()
    markdown_example = '''# Título do Markdown de exemplo
## Capítulo 1
Texto capítulo 1 e mais e mais texto.
Continuamos no capítulo 1!
## Capítulo 2
Texto capítulo 2 e mais e mais texto.
Continuamos no capítulo 2!
## Capítulo 3
### Seção 3.1
Texto capítulo 3 e mais e mais texto.
Continuamos no capítulo 3!
'''
    works = rag.default_save_txt_file(markdown_example, "test")
    print(works)
