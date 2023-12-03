import streamlit as st
import pandas as pd
import sys

sys.path.append("..")

from data_base.repository.specie_repository import SpecieRepository

st.set_page_config(
    page_title="Ver Espécies",
    page_icon="🐽",
)

st.markdown('# Ver todas as espécies')
st.markdown('## Lista de espécies')

species = SpecieRepository().select_all()

data = {
    'Nome': [specie.specie_name for specie in species],
    'Animais da espécie': [len(specie.animals) for specie in species],
}

df = pd.DataFrame(data=data)

st.dataframe(df,hide_index=True,width=1000)