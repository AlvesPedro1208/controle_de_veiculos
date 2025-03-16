from src.config import conecta_db
from datetime import datetime

class Veiculo:
    def __init__(self, placa, modelo, marca, ano_fabricacao, cor, chassi, tipo, capacidade_carga, combustivel, hodometro, data_aquisicao, observacoes):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.chassi = chassi
        self.tipo = tipo
        self.capacidade_carga = capacidade_carga
        self.combustivel = combustivel
        self.hodometro = hodometro
        self.data_aquisicao = data_aquisicao
        self.observacoes = observacoes
        self.status = True  
        self.criado_em = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def cadastrar_veiculo(self):
        query = """
            INSERT INTO veiculos (placa, modelo, marca, ano_fabricacao, cor, chassi, tipo, capacidade_carga, combustivel, hodometro, data_aquisicao, observacoes, status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        params = (
            self.placa,
            self.modelo,
            self.marca,
            self.ano_fabricacao,
            self.cor,
            self.chassi,
            self.tipo,
            self.capacidade_carga,
            self.combustivel,
            self.hodometro,
            self.data_aquisicao,
            self.observacoes,
            self.status
        )

        conecta_db(query, params)
        print(f"Veículo {self.modelo} ({self.placa}) cadastrado com sucesso!")

    @staticmethod
    def listar_veiculos():
        query = "SELECT id, placa, modelo, marca, ano_fabricacao, status FROM veiculos ORDER BY id;"
        veiculos = conecta_db(query)

        if veiculos:
            for v in veiculos:
                status_text = "Ativo" if v[5] else "Inativo"
                print(f"ID: {v[0]} | Placa: {v[1]} | Modelo: {v[2]} | Marca: {v[3]} | Ano: {v[4]} | Status: {status_text}")
        else:
            print("Nenhum veículo cadastrado.")

    @staticmethod
    def alterar_status_veiculo(placa):
        # Verifica o status atual
        query_verifica = "SELECT status FROM veiculos WHERE placa = %s;"
        status_atual = conecta_db(query_verifica, (placa,))

        if not status_atual:
            print(f"Veículo com placa {placa} não encontrado.")
            return

        novo_status = not status_atual[0][0]  

        # Atualiza o status no banco
        query_altera = "UPDATE veiculos SET status = %s WHERE placa = %s;"
        conecta_db(query_altera, (novo_status, placa))

        status_text = "Ativado" if novo_status else "Desativado"
        print(f"Status do veículo {placa} alterado para: {status_text}")
