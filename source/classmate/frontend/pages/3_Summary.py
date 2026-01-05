import streamlit as st

from classmate.backend.infrastructure.environs import Environs
from classmate.backend.RAG.rag import Rag
from classmate.frontend.constants import ALLOWED_FILE_TYPES

environs = Environs()
rag = Rag()

FILE = None

st.title("Carregue a transcrição aqui!")
file_type = st.selectbox('Selecione o tipo de arquivo', ALLOWED_FILE_TYPES)
area = st.text_input("Qual a área?")
if file_type == 'txt':
    FILE = st.file_uploader('Faça o upload do arquivo txt', type=['.txt'])
    if FILE is not None:
        content = FILE.read().decode('utf-8')
        name = FILE.name
        summary = rag.chat_retriever(transcription=content, area=area)
        st.write(summary["result"])