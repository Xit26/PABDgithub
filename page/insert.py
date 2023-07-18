import streamlit as st

import controller.cliente as cliente


def inserir():
    st.title('Inserir Dados')
    
    with st.form(key='insert'):
        input_curso = st.text_input(label='Insira o nome do curso:')
        input_matricula = st.number_input(label='Insira a matricula')
        input_senha = st.text_input(label='Insira a Senha:')
        input_data = st.date_input(label='Digite sua data de nascimento:')
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_curso, input_matricula, input_senha, input_data)
            st.success('User incluido com sucesso') 