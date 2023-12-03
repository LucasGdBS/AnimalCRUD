import streamlit as st
import sys

sys.path.append("..")

from data_base.repository.specie_repository import SpecieRepository, Specie

st.set_page_config(
    page_title="Inserir Espécies",
    page_icon="🦔",
)

st.markdown('# Inserir Espécie')
st.markdown('## Insira os dados da espécie')

with st.form('form', clear_on_submit=True, border=True):
    name = st.text_input("Nome da Espécie:")

    if st.form_submit_button("Enviar"):
        specie = Specie(
            specie_name = name
        )
        try:
            SpecieRepository().insert(specie)
            st.success("Espécie inserida com sucesso!")
        except Exception as e:
            st.error("Ocorreu um erro ao inserir a espécie.")
