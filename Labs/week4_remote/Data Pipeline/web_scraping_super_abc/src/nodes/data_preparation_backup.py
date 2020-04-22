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
    #maximiza a janela
    driver.maximize_window()
    #efetua um get na url definida anteriormente
    driver.get(url)
    #seleciona a cidade na lista que aparece no site
    Select(driver.find_element_by_xpath('//*[@id="preHomeCidade"]')).select_by_value("Divinópolis")
    #efetua novo get após a seleção da cidade
    driver.get(url)
    #cria elemento a ser fechado pelo popup e clicka nele
    elem = driver.find_element_by_xpath('//*[@id="popupCorona"]/span')
    elem.click()
    #aguarda para o carregamento da página
    time.sleep(2)
    #retorna o driver
    return driver


def get_cat_I():
    """
    Busca na home do site através do menu suspenso as categorias mãe presente no site
    @return:uma lista com os links das categorias mãe
    """
    #através da função abrir_site() gera o driver já acessado na home
    driver = abrir_site()
    #busca o elemento que abre o menu suspenso e clicka nele
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div[1]/div[2]/div[1]/button')
    elem.click()
    #após clickado no menu busca o html da página e faz a leitura com o BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #no menu fixo busca todas as categorias
    cat_raiz = soup.find_all('div', {'class': 'menu-fixo-link'})
    #para cada categoria encontrada, extrai o link desde que ele tenha o número de segmentos correspondentes apos o split
    cat_raiz = [item.find('a')['href'] for item in cat_raiz if len(item.find('a')['href'].split('/')) == 4]
    #fecha o drive criado anteriormente
    driver.quit()
    #retorna a lista com as categorias mãe
    return cat_raiz


def get_cat_II(cat_I : str):
    """
    Busca os links das sub categorias para cada categoria criada anteriormente, e retorna em uma lista
    @param cat_I:link com a categoria mãe
    @return:lista com links das sub categorias, encontradas na categoria mãe do informada
    """
    # através da função abrir_site() gera o driver já acessado na home
    driver = abrir_site()
    # efetua um get na categoria mãe passada anteriormente
    driver.get(cat_I)
    #aguarda o get busca a opção que expande as sub categorias e clicka nele
    time.sleep(1)
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/div/div/div[1]/button')
    elem.click()
    #capta a html do site, transforma para o BeautifulSoup e busca todas sub categorias
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find_all('h4')
    #dentre as sub categorias criadas traz os links de cada uma
    links = [item.find('a')['href'] for item in soup]
    #encerra o drive
    driver.quit()
    #retorna os links
    return links

def get_categories():
    """
    Função que através de paralelização gera a lista com as sub categorias, através da categoria mãe
    @return:retorna lista com todas as sub categorias
    """
    #através da função get_cat_I() busca todas as categorias mãe
    cat_I_lst = get_cat_I()
    #cria um pool com 4 processos para efetuar a paralelização
    pool = Pool(processes=4)
    #é feita a função map aplicando a função get_cat_II percorrendo a lista com as categorias
    result = pool.map(get_cat_II, cat_I_lst)
    pool.terminate()
    #entre os links gerados é criada uma lista filtrando somente para sub categorias através do split
    result = [item for cat in result for item in cat if len(item.split('/')) >= 5]
    return result

def get_product_links(cat_II):
    """
    Para cada sub categoria, busca o link de todos os produtos presentes nela e salva em um csv
    @param cat_II: link da sub categoria
    """
    #abri o arquivo com as sub categorias já processadas e o transforma em uma lista
    f = open(Params.sub_cat_processed)
    links_worked= list(csv.reader(f))
    f.close()
    #cria uma condição que verifica se a categoria já foi trabalhada anteriormente, se não inicia a busca
    if [cat_II] not in links_worked:
        #cria o driver já na pagina home e efetua um get no link e aguarda o carregamento
        driver = abrir_site()
        driver.get(cat_II)
        time.sleep(1)
        #laço while para expandir a pagina, afim de exibir todos os produtos presentes na pagina
        while True:
            try:
                #aguarda para verificar se o botão carregar mais está presente na pagina se sim clicka no mesmo
                wait = WebDriverWait(driver, 2)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="carregar-mais"]')))
                element.click()
                time.sleep(2)
            except:
                #caso não seja encontrado o botão o laço while é findado
                break
        #busca o html da pagina após expandir todos os produtos
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        #com o soup busca todos o produtos
        links = soup.find_all('a', {'class': 'prateleira__name'})
        #cria uma lista com os links de cada produto
        links = [item['href'] for item in links]
        #encerra o drive
        driver.quit()
        #salva os links dos produtos e salva em um csv
        f=open(Params.product_links, 'a')
        f.write('\n'.join(links))
        f.close()
        #salva o link da categoria mãe no arquivo controle dos links processados
        fd=open(Params.sub_cat_processed, 'a')
        fd.write(cat_II + '\n')
        fd.close()
    else:
        pass

def get_links():
    """
    Através da paralelização, busca todos o links dos produtos de cada sub categoria
    """
    #gera uma lista através da função get_categories() com todas as subcategorias
    cat_II_lst = get_categories()
    #cria a variavél tentativas para ser utilizado como contador
    attempts = 0
    #cria um while que irá rodar 3 vezes quando o get der algum erro
    while attempts < 3:
        try:
            #através de paralelização busca os links dos produtos para cada sub categoria
            pool = Pool(processes=4)
            pool.map(get_product_links, cat_II_lst)
            pool.terminate()
            break
        except:
            #caso tenha dado algum erro é acresenta-se uma tentativa e tenta efetuar a busca novamente
            attempts +=1
            pool = Pool(processes=4)
            pool.map(get_product_links, cat_II_lst)
            pool.terminate()

def clean_files():
    """
    no início do update apaga os arquivos anteriores para nova atualização
    """
    #busca o path com os arquivos
    path = Params.path_data_raw
    #cria lista com os arquivos
    lst_files = os.listdir(path)
    #arquivos a serem apagados
    files = ['product_links.csv','sub_cat.csv']
    #apaga cada arquivo
    [os.remove(path+item) for item in files if item in lst_files]

def update(params):
    """
    Busca no ecommerce www.superabc.com.br todos os links dos produtos presentes no site e salva em um arquivo csv
    @param params: parametros definidos na classe Params, arquivo: params.py
    """
    #efetua a limpeza de dados anteriores
    clean_files()
    #busca os links
    get_links()
    #atualiza em um txt a data da atualização
    file = open(params.last_update_links, mode='w+')
    file.write(params.today)
    file.close()


def done(params):
    """
    Função que verifica a ultima data da atualização dos links, e verifica a necessidade de nova atualização
    @param params:parametros definidos na classe Params, arquivo: params.py
    @return: boolean que irá definir a necessidade de atualização ou não
    """
    #cria a variavél now com a data atual
    now = datetime.now()
    #busca no arquivo last_update.txt qual a última data de atualização
    file = open(Params.last_update_links, mode='r')
    last_update = datetime.strptime(file.read(), "%Y-%m-%d")
    file.close()
    #calcula há quantos dias atrás foi a ultima atualização
    date_diff = abs((now - last_update).days)
    #cria condição para retorno da função conforme a diferença de dias
    if date_diff > params.days_to_update_prep:
        return False
    else:
        return True