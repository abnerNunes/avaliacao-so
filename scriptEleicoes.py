from conexaoBanco import *

print("----- Bem vindo ao voto Eleitoral -----\n")

print("Candidatos      Numero        Partido\n")
print("Bolsonaro         17            PSL")
print("Lula              13            PT")
print("Cabo Daciolo      51            PATRIA")
print("Boulos            50            PSOL")
print("Marina Silva      18            REDE")
print("Ciro Gomez        12            PDT\n")

nome = input("Digite seu nome:")
cpf = input("Digite seu CPF:")
candidato = int(input("Digite o numero do seu candidato:\n"))

print("Lembre-se o Voto é secreto")

insert_db(nome, cpf, candidato)
    




