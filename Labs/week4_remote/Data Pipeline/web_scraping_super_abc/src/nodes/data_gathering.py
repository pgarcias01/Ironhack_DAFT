import logging
import numpy as np
from src.params import Params
import csv
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time
import re
import os

logger = logging.getLogger('nodes.data_gathering')


def get_product_data(url):
    """
    Busca os dados de cada produto através de web scraping, e appenda em um arquivo csv
    @param url: link do produto
    """
    #faz o request na url e busca o html da página
    url = url[0]
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    #busca as informações de categorias do produto
    #tenta buscar de duas formas a categoria
    categorias = soup.find_all('li', {'typeof': 'v:Breadcrumb'})
    if len(categorias) == 0:
        categorias = soup.find_all('li', {'itemprop': 'itemListElement'})
    #cria uma lista com categorias excluindo um item que não se refere a categoria
    categorias = [item.text for item in categorias if item.text != 'abcemcasa']
    # caso o scrap tenha sido efetuado corretamente salva a categoria, se não assume como NAN
    try:
        cat1 = categorias[0]
        cat2 = categorias[1]
        cat3 = categorias[2] if len(categorias) == 3 else np.nan
    except:
        cat1 = np.nan
        cat2 = np.nan
        cat3 = np.nan
    #busca a descrição para o produto
    descricao = soup.find('h1').text
    #busca o preço do produto, para produtos indisponiveis assume como NAN
    try:
        preco = soup.find('strong', {'class': 'skuBestPrice'}).text
        preco = float(preco.split(' ')[1].replace(',', '.'))
    except:
        preco = np.nan
    #busca link da imagem
    imagem = soup.find('div', {'id': 'image'}).find('a')['href']
    #através de duas formas usando regex busca o ean
    try:
        ean = re.findall(r'(\d+)', re.findall(r'/\d+\w', url)[0])[0]
    except:
        try:
            ean = re.findall(r'(\d+)', re.findall(r'/\d+.jpg', imagem)[0])[0]
        except:
            ean = np.nan
    #cria lista com todos os dados a serem salvos como uma row no csv
    lst_to_send = [url,str(ean),str(cat1),str(cat2),str(cat3),descricao,str(preco),imagem]
    #appenda o dado do produto no csv
    fd = open(Params.data_csv, 'a')
    fd.write(','.join(lst_to_send) + '\n')
    fd.close()
    #salva o link na lista de já processados
    f = open(Params.links_processed, 'a')
    f.write(url + '\n')
    f.close()

def check_try_start(url):
    """
    Busca se o link já foi processado em caso negativo, evita o retrabalho
    @param url: link do produto a ser pesquisado
    """
    #através do arquivo, cria uma lista com as url's já processadas
    f = open(Params.links_processed)
    links_worked = list(csv.reader(f))
    f.close()
    if [url] not in links_worked:
        get_product_data(url)
    else:
        pass


def update(params):
    fd = open(params.links_processed, 'w+')
    fd.write('')
    fd.close()
    fl = open(Params.data_csv, 'w+')
    fl.write('link,ean,catI,catII,catIII,descricao,preco,imagem_link\n')
    fl.close()
    f = open(params.product_links)
    links = list(csv.reader(f))
    f.close()
    attempts = 0
    while attempts < 3:
        try:
            pool = Pool(processes=4)
            pool.map(check_try_start, links)
            pool.terminate()
            break
        except:
            time.sleep(2)
            attempts += 1
            pool = Pool(processes=4)
            pool.map(check_try_start, links)
            pool.terminate()



def done(params):
    files = os.listdir(Params.path_data_processed)
    file_to_find = Params.today + '.csv'
    if file_to_find in files:
        return True
    else:
        return False
