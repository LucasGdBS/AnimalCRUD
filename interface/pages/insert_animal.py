import streamlit as st

st.set_page_config(
    page_title="insert Animals",
    page_icon="🐶",
)

st.markdown('# Inserir Animal')

st.markdown('## Insira os dados do animal')

surname = st.text_input("Sobrenome:")
age = st.number_input("Idade:", min_value=0, max_value=200, value=0)
gender = st.selectbox("Gênero:", ["Masculino", "Feminino"])
#TODO - Mudar para os valores possiveis ser as especies cadastradas no banco de dados
specie = st.selectbox("Espécie:", ["Cachorro", "Gato", "Pássaro", "Outro"], index=0) 

if st.button("Enviar"):
    # TODO - Enviar os dados para o banco de dados
    # E se falhar mostrar uma mensagem de erro
    st.write(f"Sobrenome: {surname}")
    st.write(f"Idade: {age}")
    st.write(f"Gênero: {gender}")
    st.write(f"Espécie: {specie}")
