from connection import *

print("----- Lojinha -----\n")

print("Produtos      Codigo        Preço\n")
print("Bolo             1          20.0")
print("Suco             2          10.0")
print("Fruta            3          2.0")
print("Cigarro          4          8.0")
print("Pão              5          1.5")
print("Salgadinho       6          4.0\n")

nome = input("Qual o Seu Nome?:")
tel = input("Qual o Seu Celular?:")
candidato = int(input("Qual o código do produto?:\n"))

insert_db(nome, tel, candidato)
    




