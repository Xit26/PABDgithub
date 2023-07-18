import streamlit as st

import controller.cliente as cliente


def atualizar():
    st.title('Atualizar registro')
    matricula = st.number_input('Matrícula do aluno')
    curso = st.text_input("Novo curso")
    senha = st.text_input("Nova senha")
    data_nasc = st.date_input("Nova data de nascimento")

    if st.button('Atualizar'):
        cliente.alterar(curso, matricula, senha, data_nasc)
        st.success('Registro alterado com sucesso')