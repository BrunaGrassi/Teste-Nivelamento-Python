# Parte 1 - Conceitos Básicos
# Exercício 3 --> Crie um dicionário que armazene o nome de três pessoas como chaves e suas idades como valores. Depois, exiba o nome da pessoa mais velha.

pessoas = {}

for i in range(3):
    chave = input(f"Digite o nome da {i + 1}a pessoa: ")
    valor = int(input(f"Digite a idade da {i + 1}a pessoa: "))
    pessoas[chave] = valor

maisVelha = max(pessoas, key=pessoas.get)

print(f"A pessoa mais velha na lista é: {maisVelha} com {pessoas[maisVelha]} anos.")