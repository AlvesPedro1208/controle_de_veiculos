import os

veiculosRegistrados = [{'placa':'F63WJN','modelo':'NISSAN','ano':'2020'}, {'placa':'JF92N3','modelo':'CIVIC','ano':'2018'}, {'placa':'F8D9WJ','modelo':'HRV','ano':'2019'}]

#FUNÇÕES PARA MOSTRAR TEXTO

def exibir_nome_do_programa():
    print("""Cᴏɴᴛʀᴏʟᴇ Pɴᴇᴜs     
        """)
    
def exibir_subtitulos(texto):
    os.system('cls')
    print(texto)

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
    
    for veiculo in veiculosRegistrados:
        placa_do_veiculo = veiculo['placa']
        modelo_veiculo = veiculo['modelo']
        ano_veiculo = veiculo['ano']
        print(f'{placa_do_veiculo} - {modelo_veiculo} - {ano_veiculo}')

def escolher_opcao():
    try:
        opcao_escolhida =int(input('Escolha uma opção: ')) 

        if opcao_escolhida == 1:
            cadastrar_novo_veiculo()
        elif opcao_escolhida == 2:
            listar_veiculos()
        elif opcao_escolhida == 3:
            print('Ativar veículo')
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