import streamlit as st
import sys
from time import sleep

sys.path.append("..")

from data_base.repository.animals_repository import AnimalsRepository, Animal
from data_base.repository.specie_repository import SpecieRepository, Specie

st.set_page_config(
    page_title="Editar Animais",
    page_icon="🐍",
)

st.markdown('# Editar Animal')
animal_escolhido = st.selectbox("Selecione o animal para editar:", AnimalsRepository().select_all())

# Para encontrar o index da espécie do animal escolhido
all_species = SpecieRepository().select_all()
index_specie = next((index for index, specie in enumerate(all_species) if specie.id == animal_escolhido.specie_id), None)

with st.form('form', clear_on_submit=True, border=True):
    surname = st.text_input("Apelido:", animal_escolhido.surname if animal_escolhido.surname else "")
    age = st.number_input("Idade:", min_value=0, max_value=200, value=animal_escolhido.age if animal_escolhido.age else 0)
    gender = st.selectbox("Gênero:", ["Masculino", "Feminino"], index=1 if animal_escolhido.gender == "F" else 0)
    specie = st.selectbox("Espécie:", SpecieRepository().select_all(),index=index_specie)

    with st.container():
        columns = st.columns([5, 0.8])
        if columns[0].form_submit_button("Editar"):
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
        
        if columns[1].form_submit_button("Deletar"):
            try:
                AnimalsRepository().delete(animal_escolhido)
                st.success("Animal deletado com sucesso!", icon="✅")
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error("Ocorreu um erro ao deletar o animal.", icon="❌")
    
    st.info("Escolha o animal para editar e clique em 'Editar' para salvar as alterações.")
