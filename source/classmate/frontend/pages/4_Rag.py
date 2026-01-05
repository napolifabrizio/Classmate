import streamlit as st

from classmate.backend.infrastructure.environs import Environs
from classmate.backend.RAG.rag import Rag
from classmate.backend.models import UserInputRag
from classmate.frontend.constants import ALLOWED_FILE_TYPES

environs = Environs()
rag = Rag()

FILE = None

tabs = st.tabs(['Upload de Arquivos', 'Deleção de Arquivos'])
with tabs[0]:
    area = st.text_input("Qual a área?")
    file_type = st.selectbox('Selecione o tipo de arquivo', ALLOWED_FILE_TYPES)
    if file_type.lower() == 'txt':
        FILE = st.file_uploader('Faça o upload do arquivo txt', type=['.txt'])
        if FILE is not None:
            content = FILE.read().decode('utf-8')
            name = FILE.name
            input_rag = UserInputRag(
                Content=content,
                Name=name,
                Area=area
            )
            rag.default_save_txt_file(input_rag)
            st.write("IA treinada com sucesso!")

with tabs[1]:
    area = st.text_input("Digite a área do conhecimento")
    file_name = st.text_input("Digite o nome do arquivo")
    if file_name and area:
        rag.default_delete_vector(file_name=file_name, area=area)
        st.write("Arquivo deletado do treinamento com sucesso!")
