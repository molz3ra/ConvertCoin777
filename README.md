# 🪙 CONVERT COIN 777

## 📌 Descrição
**CONVERT COIN 777** é um conversor de moedas que busca taxas de câmbio atualizadas em tempo real utilizando a API da **ExchangeRate-API**. Com ele, você pode converter valores entre diferentes moedas de forma simples e rápida!

---

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Requests** (para chamadas de API)
- **Dotenv** (para armazenar a API Key de forma segura)

---

## 📂 Estrutura do Projeto
```
CONVERTCOIN777/
│── convertcoin777.py   # Código principal
│── .env                # Arquivo contendo a API Key (NÃO ENVIAR PARA O GITHUB!)
│── .gitignore          # Arquivo para ignorar o .env
│── README.md           # Documentação do projeto
```

---

## 🔧 Como Configurar e Executar

### 1️⃣ Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/convertcoin777.git
cd convertcoin777
```

### 2️⃣ Criar e Configurar o Arquivo `.env`
Crie um arquivo `.env` na raiz do projeto e adicione sua API Key:
```sh
echo EXCHANGE_API_KEY=coloque_sua_chave_aqui > .env
```

### 3️⃣ Instalar Dependências
```sh
pip install -r requirements.txt
```
(Se não tiver um `requirements.txt`, instale manualmente:)
```sh
pip install requests python-dotenv
```

### 4️⃣ Executar o Programa
```sh
python convertcoin777.py
```

---

## 🎯 Como Usar
1. O programa solicita um valor para conversão.
2. Você informa a moeda de origem (ex: USD, BRL, EUR).
3. Você informa a moeda de destino (ex: USD, BRL, EUR).
4. Ele retorna o valor convertido com a taxa de câmbio atual.

---

## 📌 Melhorias Futuras
- Adicionar mais moedas
- Criar uma interface gráfica (Tkinter)
- Suporte a conversão de criptomoedas

---

## 🤝 Contribuição
Fique à vontade para contribuir! Abra uma **issue** ou faça um **pull request**.

---

## 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar! 🎉
