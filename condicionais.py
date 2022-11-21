
while True:
  senha = int(input('Digite uma senha de 4 digítos: '))

  if len(str(senha)) != 4:
    print("Digite uma senha de apenas 4 digítos, por favor!")
    continue
  else:
      print("Senha cadastrada com sucesso!")
      break