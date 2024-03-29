# Tarefa 1: Ler o arquivo ao iniciar o programa (+0,5 pontos)
# Tarefa 2: Desenvolver funcionalidade listar (+0,5 pontos)
# Tarefa 3: Adicionar 3 atributos, sendo pelo menos um numérico (+0,5 pontos)
# Tarefa 4: Checar valores inválidos ou vazios em loop (+0,5 pontos)
# Tarefa 5: Desenvolver funcionalidade remover (+1 ponto)
# Tarefa 6: Desenvolver funcionalidade editar (+1 ponto)
# Tarefa EXTRA: Desenvolver todas as 4 operações para Itens, no mesmo sistema (+1 ponto)
# Total: 4 pontos
# Nota máxima: 5 pontos
# Atividade individual ou em dupla

import json

caminho_arquivo = 'personagens.json'
criaturas = []

def ler_arquivo():
    with open('personagens.json') as arquivo:
        criaturas = json.load(arquivo)
    return criaturas

def salvar_arquivo(criaturas):
    with open('personagens.json', 'w') as arquivo:
        json.dump(criaturas, arquivo, indent=4)

def imprimir_criatura(criatura):
    for atributo, valor in criatura.items():
        print(atributo, valor)
def ler_criatura():
    condicao = True
    while condicao:
        nome = input('Entre com o nome da criatura mágica: ')
        especie = input('Entre com a espécie: ')
        habitat = input('Qual o habitat da criatura? ')
        poder = input('Qual é a habilidade principal da criatura? ')
        level = input('Digite o nível da criatura: ')
        if nome == '' and especie != '' and habitat == '' and poder == '' or level == str:
            print('Valor inválido.')
        else:
            condicao = False

    criatura = {
        'nome_criatura:': nome,
        'especie_criaturaa:': especie,
        'habitat_criatur:': habitat,
        'poder_criatura:': poder,
        'level_criatura:': level
    }

    return criatura

def cadastrar():
    print('====== CADASTRO ======')
    criatura = ler_criatura()
    print('Confirma o cadastro? [s/n]')
    confirma = input('===> ')
    if confirma.lower() == 's':
        criaturas.append(criatura)
        salvar_arquivo(criaturas)
        return True

    return False

def listar():
    print('====== LISTAR ======')
    for criatura in criaturas:
        imprimir_criatura(criatura)


def editar():
    return None

def remover():
    return None

def menu():
    opcoes = {
        's': 'Sair',
        'c': 'Cadastrar',
        'l': 'Listar',
        'e': 'Editar',
        'r': 'Remover'
    }

    # imprime todas as descrições
    print('Entre com uma das opções')
    for opcao, descricao in opcoes.items():
        print(opcao, '-', descricao)

    opcao_escolhida = input('===> ')
    # passa o valor digitado para minúsculo
    opcao_escolhida = opcao_escolhida.lower()
    if opcao_escolhida not in opcoes.keys():
        print('Opção inválida!')
        return True
    elif opcao_escolhida == 'c':
        criatura = cadastrar()
        return True
    elif opcao_escolhida == 'l':
        listar()
        return True    
    elif opcao_escolhida == 's':
        print('Realmente deseja sair? [s/n]')
        confirma = input('===> ')
        if confirma.lower() == 's':
            print('Adeus!')
            return False
        return True
    
# aplicação principal
criaturas = ler_arquivo()
print(criaturas)
while menu():
    print('--------------------------------------') 