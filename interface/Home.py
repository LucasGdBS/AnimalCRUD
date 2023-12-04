'''Module for the home page of the web app.'''
import streamlit as st


st.set_page_config(
    page_title="Animals App",
    page_icon="🦒",
)

st.markdown("# Bem-vido ao Animals App!")

st.markdown("## Selecione uma opção no menu lateral para começar.")

st.markdown("#### Sobre o projeto")
st.markdown('Este projeto foi desenvolvido como uma\
            necessidade de estudar e praticar os conhecimentos de\
            banco de dados e da integração de backend com o frontend.')

st.markdown('O AnimalCRUd é um projeto MVP (Minimum Viable Product)\
            que tem como objetivo criar um CRUD (Create, Read, Update, Delete)\
            de animais, e implementar em uma interface web interativa.')


