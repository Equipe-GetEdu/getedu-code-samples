import random
import string
import time
from flask import Flask, render_template

# Inicia o objeto do framework Flask para construção da página Web
app = Flask(__name__)

# Cria o objeto do post que será introduzido dentro do html.
blog_post = {
    'title': 'Google Cloud com a GetEdu',
    'author': '<SEU_NOME>',
    'content': 'Esse é o primeiro post do meu blog. Sejam bem-vindos!'
}

# Função para simular teste de carga no servidor
def simulate_high_resource_utilization():
    while True:
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=100000))
        random_string.upper()

        time.sleep(0.2)


######################################################


# Endpoit do site (blog)
@app.route('/')
def home():
    return render_template('blog.html', post=blog_post)


# Endpoint do teste de carga
@app.route('/load')
def saturation():
    simulate_high_resource_utilization()
    return render_template('blog.html', post=blog_post)

# Inicializar o app
if __name__ == '__main__':
    app.run(debug=True)