import requests
import json
import sys
from bs4 import BeautifulSoup

def get_link():
    r = requests.get('http://gstatic.com/generate_204')
    if(r.status_code != 200):
        raise Exception('Você já está logado ou não está conectado ao wifi!')
    soup = BeautifulSoup(r.text, 'html.parser')
    link = soup.find_all('script')[0].text
    link = link[link.find('location="')+10:link.find('";')]
    print('Pegando link')
    return link

def get_inputs(link):
    r = requests.get(link)
    data = {}
    soup = BeautifulSoup(r.text, 'html.parser')
    inputs = soup.find_all('input')
    data[inputs[0]['name']] = inputs[0].attrs['value']
    data[inputs[1]['name']] = inputs[1].attrs['value']
    print('Fazendo request')
    return {
        inputs[0].attrs['name']: inputs[0].attrs['value'],
        inputs[1].attrs['name']: inputs[1].attrs['value']
    }

def logar(link, data, username, password):
    data['username'] = username
    data['password'] = password
    print('Logando...')
    return requests.post(link, data=data).text.find('keepalive') != -1
    # Retorna True se tiver logado

def configuracao(arquivo):
    print(('-' * 7) + 'Configuração' + ('-' * 7) + '\n')
    username = input('Digite o seu usuário: ')
    password = input('Digite a sua senha: ')
    with open(arquivo, 'w') as file:
        file.write(str({'username': username, 'password': password}))

def ajuda():
    print('\nAjuda\n')

if __name__ == '__main__':
    for arg in sys.argv:
        if(arg == '-c'):
            configuracao('login_info.json')
    if(len(sys.argv) == 1):
        username, password = None, None
        try:
            with open('login_info.json', 'r') as file:
                infos = json.loads(file.readline().replace("'", '"'))
                username = infos['username']
                password = infos['password']
        except:
            print('\nVocê ainda não fez a configuração!\n')
        if(username == None or password == None):
            configuracao('login_info.json')
        try:
            link = get_link()
            data = get_inputs(link)
            if(logar(link, data, '09683282610', '09683282610')):
                print('\nLogado com sucesso!\n')
        except Exception as error:
            print('Ocorreu um erro: \n')
            print(error)
    print()
