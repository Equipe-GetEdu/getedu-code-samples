import random
import string
import time
import os
from flask import Flask, render_template, request
from google.cloud import storage
import requests

BUCKET_NAME = os.getenv("BUCKET_NAME")


# Inicia o objeto do framework Flask para construção da página Web
app = Flask(__name__)

# Cria o objeto do post que será introduzido dentro do html.
blog_post = {
    'title': 'Google Cloud com a GetEdu',
    'author': '<SEU_NOME>',
    'content': 'Vamos utilizar o Google Cloud Storage?'
}

# Função para simular teste de carga no servidor
def simulate_high_resource_utilization():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=100000))
    random_string.upper()
    time.sleep(0.2)


######################################################


# Endpoit do site (blog)
@app.route('/')
def home():
    return render_template('upload.html', post=blog_post)


# Endpoint do teste de carga
@app.route('/load')
def saturation():
    simulate_high_resource_utilization()
    return render_template('blog.html', post=blog_post)

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    destination_blob_name = str(time.time())
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(image, content_type='image/jpeg')
    return render_template('blog.html', post=blog_post)


# Inicializar o app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)