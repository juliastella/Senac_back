#Bibliotecas:
import pirnt as bib

#Opção 1: parte de confirmação de senha:

def testeSh(senha):
    if str(len(senha)) != 4:
        bib.incorretoSh()
    else:
        bib.corretoSh()