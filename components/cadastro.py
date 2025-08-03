import streamlit as st

@st.dialog("Formulário de Cadastro de Alunos")
def cadastrar_aluno():
  nome_aluno = st.text_input("Nome do Aluno", placeholder="Nome do Aluno")
  email_aluno = st.text_input("Email do Aluno", placeholder="Email do Aluno")
  cpf_aluno = st.text_input("CPF do Aluno", placeholder="CPF do Aluno")
  dataNasc_aluno = st.date_input("Data de Nascimento do Aluno")
  telefone_aluno = st.text_input("Telefone do Aluno", placeholder="Telefone do Aluno")

  cols = st.columns(2)

  with cols[0]:
    btn_cadastrar = st.button("Cadastrar", use_container_width=True)

  with cols[1]:
    btn_cancelar =  st.button("Cancelar", use_container_width=True)

  if btn_cadastrar:
    st.info("Você criar a Lógica para o cadastro de Aluno")

  if btn_cancelar:
     st.rerun()