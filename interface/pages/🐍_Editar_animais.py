import streamlit as st
import sys
from time import sleep

sys.path.append("..")

from data_base.repository.animals_repository import AnimalsRepository, Animal
from data_base.repository.specie_repository import SpecieRepository

st.set_page_config(
    page_title="Editar Animais",
    page_icon="🐍",
)

st.markdown('# Editar Animal')
animal_escolhido = st.selectbox("Selecione o animal:", AnimalsRepository().select_all())

surname = st.text_input("Apelido:", animal_escolhido.surname if animal_escolhido.surname else "")
age = st.number_input("Idade:", min_value=0, max_value=200, value=animal_escolhido.age if animal_escolhido.age else 0)
gender = st.selectbox("Gênero:", ["Masculino", "Feminino"], index=1 if animal_escolhido.gender == "F" else 0)
specie = st.selectbox("Espécie:", SpecieRepository().select_all(), index=animal_escolhido.specie_id-1 if animal_escolhido.specie_id else 0)

if st.button("Editar"):
    animal = Animal(
        id = animal_escolhido.id,
        surname = surname,
        age = age,
        gender = "M" if gender == "Masculino" else "F",
        specie_id = specie.id
    )
    try:
        AnimalsRepository().update(animal)
        st.success("Animal editado com sucesso!", icon="✅")
        sleep(1)
        st.rerun()
    except Exception as e:
        st.error("Ocorreu um erro ao editar o animal.", icon="❌")
