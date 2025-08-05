import json
import os

ALUNOS = "data/alunos.json"

def select_all_alunos():
  if os.path.exists(ALUNOS):
    with open(ALUNOS, "r", encoding="utf-8") as arq_json:
      return json.load(arq_json)
  else:
    return []
  
def select_aluno_by_id(id):
  return

def select_aluno_by_email(email):
  alunos = select_all_alunos()

  for aluno in alunos:
    if aluno["email_aluno"] == email:
      return True
  return False

def insert_aluno(aluno):
  if not isinstance(aluno, dict) or not aluno:
    return False
  
  alunos = select_all_alunos()
  alunos.append(aluno)

  with open(ALUNOS, "w", encoding="utf-8") as arq_json:
    json.dump(alunos, arq_json, indent=4, ensure_ascii=False)
  return True