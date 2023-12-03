import streamlit as st
import sys
from time import sleep

sys.path.append("..")

from data_base.repository.specie_repository import SpecieRepository, Specie

st.set_page_config(
    page_title="Editar Espécies",
    page_icon="🐸",
)

st.markdown('# Editar Espécies')
especie_escolhida = st.selectbox("Selecione a espécie:", SpecieRepository().select_all())

name = st.text_input("Nome da Espécie:", value=especie_escolhida.specie_name if especie_escolhida.specie_name else "")

if st.button("Editar"):
    specie = Specie(
        id = especie_escolhida.id,
        specie_name = name
    )
    try:
        SpecieRepository().update(specie)
        st.success("Espécie editada com sucesso!", icon="✅")
        sleep(1)
        st.rerun()
    except Exception as e:
        st.error("Ocorreu um erro ao editar a espécie.", icon="❌")
