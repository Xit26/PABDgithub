import streamlit as st

import controller.cliente as cliente


def excluir():
    st.title('Excluir matrícula')
    matricula = st.number_input("Matrícula do aluno")
    
    if st.button("Excluir"):
        cliente.deletar(matricula)
        st.success("Matrícula excluida com sucesso")