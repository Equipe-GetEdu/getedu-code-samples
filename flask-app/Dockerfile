# Imagem base
FROM python:3.9-slim

# Define o diretório de trabalho padrão na imagem do container
WORKDIR /app

# Copia os arquivos local para dentro da imagem do container
COPY main.py .
COPY templates templates/

# Instala dependências
RUN pip install flask

# Expõe a porta do container
EXPOSE 80

# Comando para iniciar o app Flask
CMD ["python", "main.py"]