import streamlit as st

import controller.cliente as cliente


def consultar():
    st.title('Consultar Dados')
    colunas = st.columns((1,2,1,2,1))
    campos = ['Id', 'Curso', 'Matrícula', 'Senha', 'Data_nasc']
    
    for coluna, campo in zip(colunas, campos):
        coluna.write(campo)
    
    for item in cliente.selecionar():
        col1, col2, col3, col4, col5 = st.columns((1,2,1,2,1))
        
        col1.write(item[0])
        col2.write(item[1])
        col3.write(item[2])
        col4.write(item[3])
        col5.write(item[4])