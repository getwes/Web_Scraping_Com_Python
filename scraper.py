
#imports 
#caso não tenha pip install requests e bs4

import requests
from bs4 import BeautifulSoup

url = 'https://www.pichau.com.br/hardware/placa-de-video'

# my user agente
headers = {'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

#pendindo requerimento aos dados do site
site = requests.get(url, headers=headers)