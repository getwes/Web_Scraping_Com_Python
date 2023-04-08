
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
#placas = soup.find_all('div' , class_='MuiCardContent-root jss62' ) # div onde passa os dados, nome,preço,parcela
ultima_pagina= soup.find('button', class_='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-textPrimary MuiPaginationItem-sizeLarge').get_text().strip()

for i in range(1,int(ultima_pagina)):
    url_pag = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}2'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div' , class_='MuiCardContent-root jss62' )

    with open ('precos_placas.csv', 'a', newline='',encoding='UTF-8') as f:
        for placa in placas:
            marca = placa.find('h2', class_='MuiTypography-root jss76 jss77 MuiTypography-h6').get_text().strip()
            
            try:
                preco = placa.find('div', class_='jss87').get_text().strip()
                num_preco = preco[2:] 
                num_preco = num_preco[:-3] 
            except:

                num_preco = '0'
            
            try:
                preco_avista = placa.find('div', class_='jss79').get_text().strip()
                index = preco_avista.rfind('.') #pedindo os dados antes do index (,)
                num_preco_avista = preco_avista[2:index]
            except:
                num_preco_avista = '0'
            
            linha = marca + ';' + num_preco + ';' + num_preco_avista + '\n'

            print(linha)
            f.write(linha)
    print(url_pag)
