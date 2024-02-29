class veiculo:
    def __init__(self, placa_veiculo, modelo_veiculo, ano_veiculo):
        self.placa_veiculo = placa_veiculo
        self.modelo_veiculo = modelo_veiculo
        self.ano_veiculo = ano_veiculo
        self.status_veiculo = False

veiculo_novo = veiculo('NFOW29', 'NISSAN', 2020)

print(vars(veiculo_novo))