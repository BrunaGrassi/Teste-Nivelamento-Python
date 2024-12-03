# Parte 1 - Conceitos Básicos
# Exercício 2 --> Escreva um programa que leia uma lista de números e exiba apenas os números pares.

entrada = input("Digite uma lista de números inteiros separados por espaço em branco: ") 

# utilizamos o map() para converter cada elemento para inteiro; o split() para separar os elementos da lista utilizando o ' ' (espaço em branco) como divisor;
lista = list(map(int, entrada.split()))

def numeroPar(numero):
    return numero % 2 == 0

pares = list(filter(numeroPar, lista))
impares = list(filter(lambda x: not numeroPar(x), lista))
    
print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")