from Dicionarios.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        usuarios[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
        inserir(usuarios)
opcao = perguntar()

