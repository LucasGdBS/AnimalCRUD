import streamlit as st
import sys

sys.path.append("..")

from data_base.repository.animals_repository import AnimalsRepository, Animal
from data_base.repository.specie_repository import SpecieRepository

st.set_page_config(
    page_title="Inserir Animais",
    page_icon="🐶",
)

st.markdown('# Inserir Animal')

st.markdown('## Insira os dados do animal')

with st.form('form', clear_on_submit=True):
    surname = st.text_input("Apelido:")
    age = st.number_input("Idade:", min_value=0, max_value=200, value=0)
    gender = st.selectbox("Gênero:", ["Masculino", "Feminino"])
    specie = st.selectbox("Espécie:", SpecieRepository().select_all()) 

    if st.form_submit_button("Enviar"):
        animal = Animal(
            surname = surname,
            age = age,
            gender = "M" if gender == "Masculino" else "F",
            specie_id = specie.id
        )
        try:
            AnimalsRepository().insert(animal)
            st.success("Animal inserido com sucesso!")
        except Exception as e:
            st.error("Ocorreu um erro ao inserir o animal.")
