import logging
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from src.params import Params
from multiprocessing import Pool
from datetime import datetime
import os

logger = logging.getLogger('nodes.data_preparation')


def abrir_site():
    """
    Função que leva a home do site, como o o selenium não possuí um cache,
    a cada acesso é necessário selecionar a cidade em uma lista, bem como fechar um popup.
    @return: driver já com o acesso a home
    """
    # define url a ser utilizada
    url = Params.url_abc
    # define o chrome como webdriver a ser utilizado pelo selenium
    driver = webdriver.Chrome(executable_path=Params.chrome_path)
    # maximiza a janela
    driver.maximize_window()
    # efetua um get na url definida anteriormente
    driver.get(url)
    # seleciona a cidade na lista que aparece no site
    Select(driver.find_element_by_xpath('//*[@id="preHomeCidade"]')).select_by_value("Divinópolis")
    # efetua novo get após a seleção da cidade
    driver.get(url)
    # cria elemento a ser fechado pelo popup e clicka nele
    elem = driver.find_element_by_xpath('//*[@id="popupCorona"]/span')
    elem.click()
    # aguarda para o carregamento da página
    time.sleep(2)
    # retorna o driver
    return driver


def get_cat_I():
    """
    Busca na home do site através do menu suspenso as categorias mãe presente no site
    @return:uma lista com os links das categorias mãe
    """
    # através da função abrir_site() gera o driver já acessado na home
    driver = abrir_site()
    # busca o elemento que abre o menu suspenso e clicka nele
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div[1]/div[2]/div[1]/button')
    elem.click()
    # após clickado no menu busca o html da página e faz a leitura com o BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # no menu fixo busca todas as categorias
    cat_raiz = soup.find_all('div', {'class': 'menu-fixo-link'})
    # para cada categoria encontrada, extrai o link desde que ele tenha o número de segmentos correspondentes apos o split
    cat_raiz = [item.find('a')['href'] for item in cat_raiz if len(item.find('a')['href'].split('/')) == 4]
    cat_raiz = [item + '?PS=50' for item in cat_raiz]
    # fecha o drive criado anteriormente
    driver.quit()
    # retorna a lista com as categorias mãe
    return cat_raiz


def get_cat_II(driver, cat_I: str):
    """
    Busca os links das sub categorias para cada categoria criada anteriormente, e retorna em uma lista
    @param cat_I:link com a categoria mãe
    @return:lista com links das sub categorias, encontradas na categoria mãe do informada
    """
    # através da função abrir_site() gera o driver já acessado na home
    # efetua um get na categoria mãe passada anteriormente
    driver.get(cat_I)
    # aguarda o get busca a opção que expande as sub categorias e clicka nele
    time.sleep(1)
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/div/div/div[1]/button')
    elem.click()
    time.sleep(1)
    # capta a html do site, transforma para o BeautifulSoup e busca todas sub categorias
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find_all('ul', {'style': 'display: block; overflow: hidden;'})
    soup = [item.find_all('li') for item in soup]
    soup = [item for li in soup for item in li]
    links = [item.find('a')['href'].replace('20', '50') for item in soup]
    # retorna os links
    return links


def get_categories(cat_I):
    """
    Função que através de paralelização gera a lista com as sub categorias, através da categoria mãe
    @return:retorna lista com todas as sub categorias
    """
    driver = abrir_site()
    driver.get(cat_I)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    n_products = int(soup.find('p', {'class': 'searchResultsTime'}).find('span', {'class': 'value'}).text)
    if n_products > 990:
        sites = get_cat_II(driver, cat_I)
        links = [get_product_links(driver, link) for link in sites]
        driver.quit()
        return links
    else:
        links = get_product_links(driver, cat_I)
        driver.quit()
        return links


def get_product_links(driver, url):
    """
    Para cada sub categoria, busca o link de todos os produtos presentes nela e salva em um csv
    @param cat_II: link da sub categoria
    """
    # cria o driver já na pagina home e efetua um get no link e aguarda o carregamento
    driver.get(url)
    time.sleep(1)
    # laço while para expandir a pagina, afim de exibir todos os produtos presentes na pagina
    while True:
        try:
            # aguarda para verificar se o botão carregar mais está presente na pagina se sim clicka no mesmo
            wait = WebDriverWait(driver, 3)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="carregar-mais"]')))
            element.click()
            time.sleep(3)
        except:
            # caso não seja encontrado o botão o laço while é findado
            break
    # busca o html da pagina após expandir todos os produtos
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    # com o soup busca todos o produtos
    links = soup.find_all('a', {'class': 'prateleira__name'})
    # cria uma lista com os links de cada produto
    links = [item['href'] for item in links]
    return links


def get_links():
    """
    Através da paralelização, busca todos o links dos produtos de cada sub categoria
    """
    # gera uma lista através da função get_categories() com todas as subcategorias
    cat_I_lst = get_cat_I()
    pool = Pool(processes=4)
    links = pool.map(get_categories, cat_I_lst)
    pool.terminate()
    print(links)
    f = open(Params.product_links, 'a')
    f.write('\n'.join(links))
    f.close()


def clean_files():
    """
    no início do update apaga os arquivos anteriores para nova atualização
    """
    # busca o path com os arquivos
    path = Params.path_data_raw
    # cria lista com os arquivos
    lst_files = os.listdir(path)
    # arquivos a serem apagados
    files = ['product_links.csv', 'sub_cat.csv']
    # apaga cada arquivo
    [os.remove(path + item) for item in files if item in lst_files]
    f = open(Params.sub_cat_processed, 'w+')
    f = open(Params.product_links, 'w+')


def update(params):
    """
    Busca no ecommerce www.superabc.com.br todos os links dos produtos presentes no site e salva em um arquivo csv
    @param params: parametros definidos na classe Params, arquivo: params.py
    """
    # efetua a limpeza de dados anteriores
    clean_files()
    # busca os links
    get_links()
    # atualiza em um txt a data da atualização
    file = open(params.last_update_links, mode='w+')
    file.write(params.today)
    file.close()

params = Params()
update(params)