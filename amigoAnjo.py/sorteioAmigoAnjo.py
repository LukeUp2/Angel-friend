import random 

# Achar o arquivo com o nome dos participantes
pathPessoas = input('Insira o path do arquivo com o nome dos participantes: ')
# Cria um objeto 'pessoas' para interagir com o arquivo
pessoas = open(pathPessoas, 'r')

# Pega todas as pessoas do arquivo e coloca em uma lista
listaDePessoas = pessoas.readlines()

# Embaralha a lista
random.shuffle(listaDePessoas)

tamListaPessoas = len(listaDePessoas)
pessoas.close()

duplas = open('duplas.txt', 'a+')
i = 0
duplas.write('Duplas sortedadas: \n')
for pessoa in listaDePessoas:
    if i+1 < tamListaPessoas:
        duplas.write(str(listaDePessoas[i]) + 'vai ser o amigo anjo do(a): ' + str(listaDePessoas[i+1]) + '\n')
        i = i + 1

        if i == tamListaPessoas-1:
            duplas.write(str(listaDePessoas[i]) + 'vai ser o amigo anjo do(a): ' + str(listaDePessoas[0]) + '\n')
duplas.close()
