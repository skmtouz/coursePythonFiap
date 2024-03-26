arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo!")
with arquivo as arquivo:
    arquivo.write("\nPikachu!!")

