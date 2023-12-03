'''Desenvolva um programa de agenda de contatos. Os usuários podem adicionar, 
visualizar, editar e excluir contatos. Use um dicionário onde as chaves são os nomes 
dos contatos e os valores são os detalhes de contato (número de telefone, email, 
etc.).'''

import os
os.system('cls')

contatos = {}

menu = ('Menu: \n'
    '1. Adicionar contato \n'
    '2. Remover contato \n'
    '3. Visualizar contatos \n'
    '4. Editar contato \n'
    '5. Sair \n')

print(menu)

escolha = 0

def exibir_contatos():
    if len(contatos) == 0:
        print('A agenda está vazia.')
    else:
        print('Contatos:')
        for nome, detalhes in contatos.items():
            print(f"Nome: {nome}, Telefone: {detalhes['telefone']}, Email: {detalhes['email']}")
        print()

def editar_contato():
    if len(contatos) == 0:
        print('A agenda está vazia.')
    else:
        print('Contatos:')
        for nome, detalhes in contatos.items():
            print(f"Nome: {nome}, Telefone: {detalhes['telefone']}, Email: {detalhes['email']}")
        nome_editar = input('Informe o nome do contato que deseja editar: ')
        if nome_editar in contatos:
            print(f'Editar contato: {nome_editar}')
            telefone = input('Digite o novo telefone: ')
            email = input('Digite o novo email: ')
            contatos[nome_editar] = {'telefone': telefone, 'email': email}
            print(f"O contato '{nome_editar}' foi atualizado com sucesso!")
        else:
            print(f"O contato '{nome_editar}' não existe na agenda.")

while escolha != 5:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        contatos[nome] = {'telefone': telefone, 'email': email}
    elif escolha == 2:
        if len(contatos) == 0:
            print('Não há contatos para remover!')
        else:
            exibir_contatos()
            nome_remover = input('Informe o nome do contato que deseja remover: ')
            if nome_remover in contatos:
                del contatos[nome_remover]
                print(f"O contato '{nome_remover}' foi removido com sucesso!")
            else:
                print(f"O contato '{nome_remover}' não existe na agenda.")
    elif escolha == 3:
        exibir_contatos()
    elif escolha == 4:
        editar_contato()
    elif escolha == 5:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção inválida')