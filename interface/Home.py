'''Module for the home page of the web app.'''
import streamlit as st


st.set_page_config(
    page_title="Animals App",
    page_icon="🦒",
)

st.markdown("# Bem-vido ao Animals App!")

st.markdown("## Selecione uma opção no menu lateral para começar.")

st.markdown("#### Sobre o projeto")
st.markdown('Este projeto foi desenvolvido como parte\
            do curso de Ciencia da computação da Cesar School')

st.markdown('O objetivo é criar uma interface para realizar o CRUD em uma\
            base de dados de animais')


