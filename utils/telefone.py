def formatar_telefone(telefone):
  if len(telefone) == 11:
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
  return None