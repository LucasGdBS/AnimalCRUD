import streamlit as st
import pandas as pd
import sys

sys.path.append("..")

from data_base.repository.animals_repository import AnimalsRepository
from data_base.repository.specie_repository import SpecieRepository

st.set_page_config(
    page_title="Ver Animais",
    page_icon="🦄",
)

st.markdown('# Ver todos os animais')
st.markdown('## Lista de animais')


animals = AnimalsRepository().select_all()
data = {
    'Apelido': [animal.surname for animal in animals],
    'Idade': [animal.age for animal in animals],
    'Gênero': [animal.gender for animal in animals],
    'Espécie': [SpecieRepository().select_by_id(animal.specie_id).specie_name for animal in animals]
}

df = pd.DataFrame(data=data)

st.dataframe(df,hide_index=True,width=1000)
