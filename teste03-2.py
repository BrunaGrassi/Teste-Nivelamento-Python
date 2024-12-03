# Parte 1 - Conceitos Básicos
# Exercício 3 --> Crie um dicionário que armazene o nome de três pessoas como chaves e suas idades como valores. Depois, exiba o nome da pessoa mais velha.

pessoas = {}

while True:
    nome = input("Digite o nome da pessoa (ou digite 'sair' para finalizar.): ")
    if nome.lower() == 'sair':
        break
    valor = int(input(f"Digite a idade de {nome}: "))
    pessoas[nome] = valor


if pessoas:
    maisVelha = max(pessoas, key=pessoas.get)
    print(f"A pessoa mais velha na lista é: {maisVelha} com {pessoas[maisVelha]} anos.")
else:
    print("Nenhuma pessoa foi adicionada à lista.")