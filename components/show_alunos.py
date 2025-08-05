import streamlit as st
from controllers.alunos_controllers import select_all_alunos
from utils.cpf import formatar_cpf

def show_alunos():
  alunos = select_all_alunos()
  if not alunos:
    return st.info("Nenhum Aluno Cadastrado. Para cadastrar Aluno ou Alunos Clique no botão cadastrar acima.")

  tabs_alunos = st.tabs(["Alunos", "Pesquisar"])

  with tabs_alunos[0]:
    cols_header = st.columns([3, 2, 3, 2, 2])
    cols_header[0].subheader("Nome")
    cols_header[1].subheader("CPF")
    cols_header[2].subheader("Email")
    cols_header[3].subheader("Vizualizar")
    cols_header[4].subheader("Deletar")

    for aluno in alunos:
      cols = st.columns([3, 2, 3, 2, 2])

      cpf_formatado = formatar_cpf(aluno["cpf_aluno"])

      cols[0].write(aluno["nome_aluno"])
      cols[1].write(cpf_formatado)
      cols[2].write(aluno["email_aluno"])

      if cols[3].button("View", key=f"edit_{aluno["id_aluno"]}", use_container_width=True):
        # view_aluno(aluno)
        pass

      if cols[4].button("Deletar", key=f"delete_{aluno["id_aluno"]}", use_container_width=True):
        # modal_deletar(aluno["id_aluno"], aluno["nome_aluno"])
        pass