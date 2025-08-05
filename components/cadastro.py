import streamlit as st
import re
import time
from datetime import date
from utils.valida_email import valida_email
from controllers.alunos_controllers import select_aluno_by_email, insert_aluno, select_all_alunos

@st.dialog("Formulário de Cadastro de Alunos", width=True)
def cadastrar_aluno():
  alunos = select_all_alunos()
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
    email_is_valid = valida_email(email_aluno)
    result_db = select_aluno_by_email(email_aluno)

    cols = st.columns(2)

    with cols[0]:
      btn_cadastrar = st.form_submit_button("Cadastrar", use_container_width=True)

    with cols[1]:
      btn_cancelar =  st.form_submit_button("Cancelar", use_container_width=True)

  if btn_cadastrar:
    if not nome_aluno:
      return st.warning("O campo nome precisa ser preenchido!")
    
    if not email_is_valid:
      return st.warning("Email invalido!")
    
    if result_db:
      return st.warning("Email já está cadastrado com outro aluno!")

    if len(cpf_aluno_numeros) != 11:
      return st.warning("CPF invalido, digite somente numeros")

    if len(telefone_aluno_numeros) != 11:
      return st.warning("Telefone invalido, digite somente numeros")
    
    id_novo = (alunos[-1]["id_aluno"] + 1) if alunos else 1

    data_aluno = {
      "id_aluno": id_novo,
      "nome_aluno": nome_aluno,
      "email_aluno": email_aluno,
      "cpf_aluno": cpf_aluno_numeros,
      "dataNasc_aluno": dataNasc_aluno.strftime("%Y-%m-%d"),
      "telefone": telefone_aluno_numeros
    }

    result_insert = insert_aluno(data_aluno)

    if not result_insert:
      st.warning("Não foi possível realizar o cadastro!")
    
    st.success("Cadastro Realizado com Sucesso!")
    time.sleep(3)
    st.rerun()

  if btn_cancelar:
     st.rerun()