import requests
from empresa import empresa

def url_acesso():
    return "https://sandbox.asaas.com/api/v3/payments"

def criar(empresa, descricao):
    url = url_acesso()

    payload = {
        "billingType": "BOLETO",
        "value": empresa.valor,
        "dueDate": empresa.data_vencimento,
        "description": descricao,
        "customer": empresa.id_asaas  # Supondo que empresa.id_asaas é o ID do cliente na Asaas API
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        if 'id' in response_json:
            return response_json['id']
        else:
            return False
    else:
        return response.text

def busca_uma(empresa, id_cobranca):
    url = f"{url_acesso()}/{id_cobranca}"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Retorna os dados da cobrança como um dicionário
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def recupera_status(empresa, id_cobranca):
    url = f"{url_acesso()}/{id_cobranca}/status"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['status']  # Retorna os dados do status da cobrança como um dicionário
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def listar_cobrancas(empresa, status="PENDING", offset=0, limit=10):
    url = f"{url_acesso()}?customer={empresa.id_asaas}&status={status}&offset={offset}&limit={limit}"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Retorna os dados das cobranças como uma lista de dicionários
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def atualizar(empresa,id_asaas, novo_valor, nova_data_vencimento, nova_descricao):
    url = f"{url_acesso()}/{id_asaas}"

    payload = {
        "billingType": "BOLETO",
        "value": novo_valor,
        "dueDate": nova_data_vencimento,
        "description": nova_descricao
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return True  # Retorna True se a cobrança for atualizada com sucesso
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def remover(empresa, id_asaas):
    url = f"{url_acesso()}/{id_asaas}"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return True  # Retorna True se a cobrança for removida com sucesso
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def restaurar_remocao(empresa, id_asaas):
    url = f"{url_acesso()}/{id_asaas}/restore"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return True  # Retorna True se a restauração for bem-sucedida
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def confirmacao_dinheiro(empresa, id_asaas, valor, data_pagamento):
    url = f"{url_acesso()}/{id_asaas}/receiveInCash"

    payload = {
        "notifyCustomer": True,
        "value": valor,
        "paymentDate": data_pagamento
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return True  # Retorna True se a confirmação for bem-sucedida
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida

def desfazer_confirmacao_dinheiro(empresa, id_asaas):
    url = f"{url_acesso()}/{id_asaas}/undoReceivedInCash"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return True  # Retorna True se a ação for bem-sucedida
    else:
        return False  # Retorna False se a solicitação não for bem-sucedida
