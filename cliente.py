import requests
from empresa import empresa

def url_acesso():
    return "https://sandbox.asaas.com/api/v3/customers"

def criar(empresa):
    """
    Cria um novo cliente na Asaas API usando os dados fornecidos.

    Args:
    - empresa: Um objeto contendo os detalhes da empresa, como nome, cpf, email, sistema e telefone.

    Returns:
    - O ID do cliente criado se a solicitação for bem-sucedida, False caso contrário.
    """
    url = url_acesso()

    payload = {
        "name": empresa.nome,
        "cpfCnpj": empresa.cpf,
        "email": empresa.email,
        "company":empresa.sistema,
        "mobilePhone": empresa.telefone
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
        return False
    
def buscar_um(empresa):
    """
    Busca informações de uma única cobrança na Asaas API com base no ID fornecido.

    Args:
    - empresa: Objeto representando a empresa. Deve conter os atributos 'id_asaas' e 'access_token'.

    Returns:
    - Se a solicitação for bem-sucedida (status code 200), retorna os detalhes da cobrança em formato JSON.
    - Caso contrário, retorna False.
    """

    url = f"{url_acesso()}/{empresa.id_asaas}"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return False

def lista_clientes(empresa, offset=0, limit=100):
    """
    Busca um cliente específico na Asaas API usando o ID fornecido.

    Args:
    - empresa: Um objeto contendo os detalhes da empresa, como id_asaas e access_token.

    Returns:
    - Um dicionário com os dados do cliente se a solicitação for bem-sucedida, False caso contrário.
    """
    url = f"{url_acesso()}?offset={offset}&limit={limit}"
    
    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return False

def alterar(empresa):
    """
    Altera os detalhes de uma empresa na Asaas API com base no ID fornecido.

    Args:
    - empresa: Objeto representando a empresa. Deve conter os atributos 'id_asaas', 'nome', 'cpf', 'sistema', 'email', 'telefone' e 'access_token'.

    Returns:
    - Se a solicitação for bem-sucedida (status code 200), retorna os novos detalhes da empresa em formato JSON.
    - Caso contrário, retorna False.
    """

    url = f"{url_acesso()}/{empresa.id_asaas}"

    payload = {
        "name": empresa.nome,
        "cpfCnpj": empresa.cpf,
        "company":empresa.sistema,
        "email": empresa.email,
        "mobilePhone": empresa.telefone
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.put(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return False

def remover(empresa):
    url = f"{url_acesso()}/{empresa.id_asaas}"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

def restaurar_removido(empresa):
    url = f"{url_acesso()}/{empresa.id_asaas}/restore"

    headers = {
        "accept": "application/json",
        "access_token": empresa.access_token
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

# print(criar(empresa))
