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

with st.form('form', clear_on_submit=True, border=True):
    name = st.text_input("Nome da Espécie:", value=especie_escolhida.specie_name if especie_escolhida.specie_name else "")

    with st.container():
        columns = st.columns([5, 0.8])
        if columns[0].form_submit_button("Editar"):
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
        
        if columns[1].form_submit_button("Deletar"):
            try:
                SpecieRepository().delete(especie_escolhida)
                st.success("Espécie deletada com sucesso!", icon="✅")
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error("Ocorreu um erro ao deletar a espécie.", icon="❌")
    
    st.info("Escolha a espécie para editar e clique em 'Editar' para salvar as alterações.")
