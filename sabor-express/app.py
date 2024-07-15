import os

restaurantes = [{"nome": "Praça é Nossa","categoria":"Japonesa", "ativo":False}, 
                {"nome":"Cachorro Careca", "categoria":"Italiana", "ativo":True}, 
                {"nome":"Camelo Rebaixado", "categoria":"Brasileira", "ativo": False}
                ]

def exibir_nome_do_programa():
    """Essa função é responsável por exibir o nome do programa
    Outputs:
        › Imprimindo o título do programa
    """
    print("Sabor Express\n");

def exibir_opcoes():
    """Essa função é responsável por exibir as opções do usuário
    Outputs:
        › Exibindo as 4 opções.
    """
    print('1. Cadastrar estaurante')
    print('2. Listar Restaurantes')
    print('3. Alternar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    """Essa função é responsável por finalizar o app
    Outputs:
        › Finalizando o App
    """
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    """Essa função é responsável por retornar ao menu inicial do app
    Inputs:
        › Qualquer tecla 

    Outputs:
        › Retorna ao menu inicial
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    """Essa função é responsável por exibir a opção inválida
    Outputs:
        › Gerando opção inválida
    """
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    """Essa função é responsável por exibir os subtítulos
    Outputs:
        › Subtítulo das Opções com Detalhes de *.
    """
    os.system('cls')
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    """Essa função é responsável por cadastrar um novo restaurante
    Inputs:
        › Nome do Restaurante;
        › Categoria do Restaurante. 

    Outputs:
        › Adiciona um novo restaurante à lista de restaurantes. 
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'O nome de categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Essa função é responsável por listar os restaurantes cadastrados
        Outputs:
        › Exibindo o subtítulo;
        › Exibindo o Nome do Restaurante, Categoria e Status.
    """
    exibir_subtitulo('Listando restaurantes')

    print(f"{"NOME DO RESTAURANTE".ljust(22)} | {"CATEGORIA".ljust(20)} | STATUS")
    print()

    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    """Essa função é responsável por alterar o status do restaurante
    Inputs:
        › Nome do Restaurante.

    Outputs:
        › Exibindo subtitulo;
        › Alterando o Status.
    """
    exibir_subtitulo("Alternando Estado do Restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")
    
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()

def escolher_opcao():
    """Essa função é responsável pela escolha do usuário à uma das opções
    Inputs:
        › Escolha de Opção.

    Outputs:
        › Procedendo para a opção desejada.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alterar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Essa função é a principal"""
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()