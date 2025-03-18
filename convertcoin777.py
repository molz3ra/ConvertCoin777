import requests
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("EXCHANGE_API_KEY")  # Pega a chave do arquivo .env

# Função para obter a taxa de câmbio atual
def obter_taxa(moeda_origem, moeda_destino):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{moeda_origem}"

    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200 and moeda_destino in dados["conversion_rates"]:
        return dados["conversion_rates"][moeda_destino]
    else:
        return None

# Função para converter o valor
def converter_moeda(valor, moeda_origem, moeda_destino):
    taxa = obter_taxa(moeda_origem, moeda_destino)
    
    if taxa:
        return valor * taxa
    else:
        return "Erro ao obter taxa de câmbio."

# Entrada do usuário
valor = float(input("Digite o valor a converter: "))
moeda_origem = input("Moeda de origem (ex: USD, BRL, EUR): ").upper()
moeda_destino = input("Moeda de destino (ex: USD, BRL, EUR): ").upper()

# Faz a conversão e exibe o resultado
resultado = converter_moeda(valor, moeda_origem, moeda_destino)
print(f"Valor convertido: {resultado}")
