# 🎬 API de Consulta de Filmes

Este projeto é composto por uma **API de consulta de informações sobre filmes**, estruturada em **três microserviços** distintos. A aplicação é desenvolvida em **Python com Flask** e utiliza **Docker** para conteinerização e orquestração dos serviços.

Este projeto foi desenvolvido com base na versão 3 do projeto [Feed de Notícias](https://gitlab.com/luiscarvalho1/soa/-/blob/master/2025/versao3.zip), elaborada pelo professor Dr. Luis Paulo da Silva Carvalho.

---

## 📌 Descrição

O sistema é dividido em três microserviços principais:

1. **Filmes (`movies`)**  
   Responsável por armazenar e fornecer informações básicas dos filmes:
   - Título
   - Gênero
   - Elenco
   - Ano
   - Diretor
   - Sinopse

2. **Comentários & Reviews (`comments`)**  
   Gerencia os comentários e avaliações deixados por usuários sobre os filmes.

3. **Recomendações (`recommendations`)**  
   Fornece sugestões de filmes com base em um determinado título.

Além da API, há também um **cliente (`client.py`)** que consome os três microserviços e apresenta as informações de forma unificada para o usuário final.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python**
- 🌐 **Flask**
- 📦 **Docker**
- 🔌 REST APIs
- 🧱 Arquitetura de **Microserviços**

---

## 🛠️ Como executar o projeto

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. Clone este repositório e acesse a pasta do projeto.
    ```bash
    git clone https://github.com/seu-usuario/api-filmes-python-flask-docker.git
    cd api-filmes-python-flask-docker
    ```

2. Crie um ambiente virtual com o comando:  
   ```bash
   python3 -m venv venv
   ```

3. Ative o ambiente virtual:  
   - No Linux/Mac: 
   ```bash 
   source venv/bin/activate
   ``` 
   - No Windows (cmd): 
   ```bash 
   venv\Scripts\activate
   ``` 
   - No Windows (PowerShell): 
   ```bash 
   venv\Scripts\Activate.ps1`
   ``` 

4. Instale as dependências com:  
   ```bash 
   pip3 install -r requirements.txt
   ```

5. Execute os microserviços usando Docker:  
   ```bash 
   docker-compose up --build
   ```

---

## 🌐 Endpoints dos Microserviços

- **Movies**: http://localhost:5001  
- **Comments**: http://localhost:5002  
- **Recommendations**: http://localhost:5003

---

## ▶️ Como testar

Com os microserviços ativos, execute o cliente com:  
```bash 
python3 client.py
```

O cliente irá buscar e exibir as informações de filmes, comentários e recomendações de forma integrada.

---

## 📴 Como desativar logicamente um microserviço

Para simular a indisponibilidade de um microserviço, altere a variável `ALIVE` em seu respectivo código para:

`ALIVE = "não"`

Quando a variável estiver com esse valor, o microserviço será tratado como inativo pelo cliente.

---

## 📂 Estrutura do Projeto

```text 
.
├── data/
│   └── comments.json
│   └── movies.json
│   └── recommendations.json
├── services/
│   └── comments/
│      └── service.py
│   └── movies/
│      └── service.py
│   └── recommendations/
│      └── service.py
├── client.py
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
``` 

📺 Demonstração em Vídeo

Foi produzido um vídeo demonstrando o uso do sistema, incluindo o consumo dos microserviços e a simulação da parada lógica de cada um deles.
A demonstração está disponível no YouTube e pode ser acessada [clicando aqui]().

---

## 👨‍💻 Autor

**Marco Antonio S. Silva**  
[LinkedIn](https://www.linkedin.com/in/marcosilva95) • [GitHub](https://github.com/marcoantoniossilva) • [YouTube](https://www.youtube.com/@MarcoAntonioSSilvaDev)
