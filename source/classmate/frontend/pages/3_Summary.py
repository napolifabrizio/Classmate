import streamlit as st

from classmate.backend.infrastructure.environs import Environs
from classmate.backend.RAG.rag import Rag
from classmate.frontend.constants import ALLOWED_FILE_TYPES

FILE = None

environs = Environs()
rag = Rag()

st.title("Carregue a transcrição aqui!")
file_type = st.selectbox('Selecione o tipo de arquivo', ALLOWED_FILE_TYPES)
area = st.text_input("Qual a área?")
if file_type == 'txt':
    FILE = st.file_uploader('Faça o upload do arquivo txt', type=['txt'])
    if FILE is not None:
        if st.button('Gerar Resumo e Insights'):
            content = FILE.read().decode('utf-8')
            name = FILE.name
            st.success(f"Arquivo '{name}' carregado com sucesso!")
            with st.spinner('O Agente está analisando a transcrição...'):
                summary = rag.chat_retriever(transcription=content, area=area)
                st.subheader("Resultado da Análise")
                st.write(summary["result"])
