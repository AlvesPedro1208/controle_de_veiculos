import os

veiculosRegistrados = [{'placa':'F63WJN','modelo':'NISSAN','ano':'2020','statusAtivação':False}, {'placa':'JF92N3','modelo':'CIVIC','ano':'2018','statusAtivação':False}, {'placa':'F8D9WJ','modelo':'HRV','ano':'2019','statusAtivação':False}]

#FUNÇÕES PARA MOSTRAR TEXTO

def exibir_nome_do_programa():
    print("""Cᴏɴᴛʀᴏʟᴇ Pɴᴇᴜs     
        """)
    
def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)


def exibir_opcoes():
    print('1. Cadastrar veículo')
    print('2. Listar veículos')
    print('3. Ativar veículo')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulos('Finalizando o app\n')

def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def voltar_ao_menu():
   resposta = input('Deseja voltar ao menu principal? (Y/N) ')
   if resposta == 'Y' or resposta == 'y':
       main()
    
#FUNÇÃO QUE CADASTRA NOVOS VEÍCULOS

def cadastrar_novo_veiculo():
    exibir_subtitulos('Cadastro de novos veículos\n')
    placa_do_veiculo = input('Digite a placa do veículo: ')
    veiculosRegistrados.append(placa_do_veiculo)
    modelo_veiculo = input('Digite o modelo do veículo: ')
    veiculosRegistrados.append(modelo_veiculo)
    ano_veiculo = input('Digite o ano do veiculo: ')
    veiculosRegistrados.append(ano_veiculo)
    print()
    print(f'O veículo {modelo_veiculo} com placa {placa_do_veiculo} e ano {ano_veiculo} foi cadastrado com sucesso')
    resposta_cadastro = input('Deseja cadastrar mais algum veículo? (Y/N): ')
    if resposta_cadastro == 'Y' or resposta_cadastro == 'y':
        cadastrar_novo_veiculo()
    elif resposta_cadastro == 'N' or resposta_cadastro == 'n':
        main ()
    else:
        print('Opção inválida! Retornando a tela inicial.')
        main()

#FUNÇÃO QUE LISTA TODOS OS VEICULOS CADASTRADOS

def listar_veiculos():
    exibir_subtitulos('Lista de veículos cadastrados: ')
    print()
    
    for veiculo in veiculosRegistrados:
        placa_do_veiculo = veiculo['placa']
        modelo_veiculo = veiculo['modelo']
        ano_veiculo = veiculo['ano']
        status_veiculo = 'Ativado' if veiculo['statusAtivação'] else 'desativado'
        
        print(f'{placa_do_veiculo.ljust(7)} - {modelo_veiculo.ljust(7)} - {ano_veiculo.ljust(7)} - {status_veiculo}')
    print()

    voltar_ao_menu()

def alterar_status_veiculo():
    exibir_subtitulos('Veículos ativos: ')

    placa_veiculo = input('Digite a placa do veículo que deseja alterar o status: ')
    veiculo_encontrado = False
    
    for veiculo in veiculosRegistrados:
        if placa_veiculo == veiculo['placa']:
            veiculo_encontrado = True
            veiculo['statusAtivação'] = not veiculo['statusAtivação']
            mensagem = f'O veiculo com a placa {placa_veiculo} foi ATIVADO com sucesso!' if veiculo['statusAtivação'] else f'O veículo com a placa {placa_veiculo} foi DESATIVADO com sucesso!'
            print(mensagem)
    if not veiculo_encontrado:
        print('O veículo não foi encontrado!')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida =int(input('Escolha uma opção: ')) 

        if opcao_escolhida == 1:
            cadastrar_novo_veiculo()
        elif opcao_escolhida == 2:
            listar_veiculos()
        elif opcao_escolhida == 3:
            alterar_status_veiculo()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

#função main

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()