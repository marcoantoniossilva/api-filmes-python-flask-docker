# realiza o download da ultima versao de imagem python disponivel no docker hub
FROM python:latest

# instalando as dependencias python
RUN pip install Flask

# criando diretorio onde serao guardados os dados
RUN mkdir /data

# criando diretorio de trabalho onde serao guardados os arquivos dos servicos
RUN mkdir /service
WORKDIR /service

