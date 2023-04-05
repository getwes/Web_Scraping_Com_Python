
#imports 
#caso não tenha pip install requests e bs4

import requests
from bs4 import BeautifulSoup

url = 'https://www.pichau.com.br/hardware/placa-de-video'

# my user agente
headers = {'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

#pendindo requerimento aos dados do site
site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')#basicamente vou estar analizando o conteudo do site
placas = soup.find_all('div' , class_='MuiCardContent-root jss62' )
ultima_pagina= soup.find('button', class_='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-root')
placa = placas[0]
marca = placa.find('h2', class_='MuiTypography-root jss76 jss77 MuiTypography-h6')

print(marca)