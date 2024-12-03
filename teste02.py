# Parte 1 - Conceitos Básicos
# Exercício 2 --> Escreva um programa que leia uma lista de números e exiba apenas os números pares.

entrada = input("Digite uma lista de números inteiros: ") 

# utilizamos o map() para converter cada elemento para inteiro; o split() para separar os elementos da lista utilizando o ' ' (espaço em branco) como divisor;
lista = list(map(int, entrada.split()))

print(lista)