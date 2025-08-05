import streamlit as st
import re
import time
from datetime import date, datetime
from utils.telefone import formatar_telefone
from utils.cpf import formatar_cpf
from utils.valida_email import valida_email

@st.dialog("Formulário de Cadastro de Alunos", width=True)
def cadastrar_aluno():
  with st.form("form_cadastro_aluno"):
    data_minima = date(1900, 1, 1)
    data_maxima = date.today()

    nome_aluno = st.text_input("Nome do Aluno", placeholder="Nome do Aluno")
    email_aluno = st.text_input("Email do Aluno", placeholder="Email do Aluno")
    cpf_aluno = st.text_input("CPF do Aluno, digite apenas numeros:", placeholder="CPF do Aluno, somente números", max_chars=11)
    dataNasc_aluno = st.date_input(
      "Data de Nascimento do Aluno",
      value=data_maxima,
      min_value=data_minima,
      max_value=data_maxima
    )
    telefone_aluno = st.text_input("Telefone do Aluno", placeholder="Telefone do Aluno", max_chars=11)

    cpf_aluno_numeros = re.sub(r"\D", "", cpf_aluno)
    telefone_aluno_numeros = re.sub(r"\D", "", telefone_aluno)
    result_email = valida_email(email_aluno)
    cols = st.columns(2)

    with cols[0]:
      btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)

    with cols[1]:
      btn_cancelar =  st.form_submit_button("Cancelar", use_container_width=True)

  if btn_cadastrar:
    if not result_email:
      return st.warning("Email invalido!")
    
    if len(cpf_aluno_numeros) != 11:
      return st.warning("CPF invalido, digite somente numeros")

    if len(telefone_aluno_numeros) != 11:
      return st.warning("Telefone invalido, digite somente numeros")
    

    data_aluno = {
      "nome_aluno": nome_aluno,
      "email_aluno": email_aluno,
      "cpf_aluno": cpf_aluno_numeros,
      "dataNasc_aluno": dataNasc_aluno.strftime("%d-%m-%Y"),
      "telefone": telefone_aluno_numeros
    }

    st.write(data_aluno)
    st.success("Cadastro Realizado com Sucesso!")
    time.sleep(3)

  if btn_cancelar:
     st.rerun()