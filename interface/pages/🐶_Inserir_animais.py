import streamlit as st
import sys

sys.path.append("..")

from data_base.repository.animals_repository import AnimalsRepository
from data_base.models.animals_orm import Animal
from data_base.repository.specie_repository import SpecieRepository

st.set_page_config(
    page_title="Inserir Animais",
    page_icon="🐶",
)

st.markdown('# Inserir Animal')

st.markdown('## Insira os dados do animal')

surname = st.text_input("Sobrenome:")
age = st.number_input("Idade:", min_value=0, max_value=200, value=0)
gender = st.selectbox("Gênero:", ["Masculino", "Feminino"])
#TODO - Mudar para os valores possiveis ser as especies cadastradas no banco de dados
specie = st.selectbox("Espécie:", SpecieRepository().select_all()) 

if st.button("Enviar"):
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
