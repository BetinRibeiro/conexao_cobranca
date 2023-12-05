class Empresa:
    def __init__(self,id_asaas, nome,sistema, cpf, email, telefone,valor,data_vencimento, access_token):
        self.id_asaas = id_asaas
        self.nome = nome
        self.sistema = sistema
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.valor = valor
        self.data_vencimento=data_vencimento
        self.access_token = access_token

# Exemplo de uso:
empresa = Empresa(
    id_asaas=ID_ASAAS,
    nome=NOME,
    sistema=SISTEMA,
    telefone=TELEFONE,
    cpf=CPF,
    email=EMAIL,
    valor=VALOR,
    data_vencimento='2024-01-01',
    access_token= SEU_TOKEN
)
