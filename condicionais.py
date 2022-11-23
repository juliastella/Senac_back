"""import classe as bib"""
import pirnt as bib
"""import funcaBase as bib"""
import  time

# Testagem de senha:
bib.explicaSh()
while True:
  senha = int(input('\nDigite uma senha de 4 digítos: \n'))
  time.sleep(0.5)

  if len(str(senha)) != 4:
    print("\n|Digite uma senha com apenas 4 digítos!|")
    continue
  else:
    print("\n|Senha cadastrada e deposito com sucesso!|")
  break
