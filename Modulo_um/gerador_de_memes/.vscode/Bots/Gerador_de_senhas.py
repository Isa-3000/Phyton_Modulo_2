import random

elementos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#%"

tamanho = int(input("Digite o tamanho da senha desejada: "))

senha = ""

for i in  range(tamanho):
    caractere = random.choice(elementos)
    senha = senha + caractere

print(f"A senha gerada é: {senha}")