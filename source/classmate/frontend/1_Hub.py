
import streamlit as st

# Optional: Add your logo here
# st.image('path/to/logo.png', width=200)

st.title('Meet Keyllex')
st.markdown("""
<style>
.big-font {font-size:28px !important; font-weight: 600;}
.center {text-align: center;}
</style>
""", unsafe_allow_html=True)

st.write('''
**Meet Keyllex** é uma plataforma para geração de resumos inteligentes, com base no treinamento que você fará á ela! Você pode gravar a reunião,
ou usar transcrições (de reuniões) que você já tenha para gerar seus resumos.
''')

st.markdown('''<hr>''', unsafe_allow_html=True)

st.header('Guia das Páginas')
st.markdown('''
1. **Hub:** Onboarding da aplicação
2. **Record:** Gravar a reunião atual
3. **Summary:** Gerar resumos das reunições, a partir das transcrições
4. **Rag:** Treinamento da IA, para enriquecer o resumo da reunião com o seu próprio conhecimento.
''')

st.markdown('''<hr>''', unsafe_allow_html=True)

st.warning('''
Para o treinamento da IA, atualmente só aceitamos arquivos de texto em markdown. \n
Em caso de dúvidas, consulte a documentação ou entre em contato com o suporte.
''')

with st.expander('Exemplo de arquivo de treinamento'):
	st.code('''# Como vender mais
## Sorria
Sorria sempre!
## Seja gentil
Seja gentil
## Resolva dores
Resolva algum problema
    ''', language='markdown')

# st.markdown('''<hr>''', unsafe_allow_html=True)
# st.caption('Desenvolvido por [Seu Nome/Equipe] • © 2025')

