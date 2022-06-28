def soma():
    x =float(input("Primeiro numero:"))
    y =float(input("Segundo numero:"))
    print("Soma:",x+y)

def subtracao():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("subtracao:",x-y)

def multiplicacao():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("multiplicacao",x*y)

def divisao():
    x = float(input("Primeiro numero:"))
    y = float(input("Segundo numero:"))
    print("divisao",x/y)

opcao = 1

while opcao:
    print("0 sair")
    print("1  somar")
    print("2 subtrair")
    print("3  multiplicação")
    print("4  Divisão")

    opcao = int(input("Opção:"))

    if(opcao==1):
        soma()
        if(opcao==2):
          subtracao()
          if(opcao==3):
            multiplicacao()

            if(opcao==4):
             divisao()
