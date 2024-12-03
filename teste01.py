# Parte 1 - Conceitos Básicos
# Exercício 1 --> Escreva um código que peça ao usuário dois números e exiba a soma deles.

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número para somar: "))

    print(f"A soma dos números é: {(n1 + n2)}")
except ValueError:
    print("Insira apenas números inteiros, por favor.")