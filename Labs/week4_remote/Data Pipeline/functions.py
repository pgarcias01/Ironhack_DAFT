import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def abrir_site():
    url = 'https://www.superabc.com.br/'
    driver = webdriver.Chrome(executable_path='C:/Users/pedro/selenium/chromedriver.exe')
    driver.maximize_window()
    driver.get(url)
    Select(driver.find_element_by_xpath('//*[@id="preHomeCidade"]')).select_by_value("Divinópolis")
    driver.get(url)
    elem = driver.find_element_by_xpath('//*[@id="popupCorona"]/span')
    elem.click()
    time.sleep(2)
    return driver

def get_cat_I():
    driver = abrir_site()
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div[1]/div[2]/div[1]/button')
    elem.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    cat_raiz = soup.find_all('div', {'class': 'menu-fixo-link'})
    cat_raiz = [item.find('a')['href'] for item in cat_raiz if len(item.find('a')['href'].split('/')) == 4]
    driver.quit()
    return cat_raiz

def get_cat_II(cat_I):
    driver = abrir_site()
    driver.get(cat_I)
    time.sleep(1)
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/main/div[1]/div[2]/div/div/div[1]/button')
    elem.click()
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    soup = soup.find_all('h4')
    links = [item.find('a')['href'] for item in soup]
    driver.quit()
    return links

def get_product_links(cat_II):
    driver = abrir_site()
    driver.get(cat_II)
    time.sleep(1)
    while True:
        try:
            wait = WebDriverWait(driver, 3)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="carregar-mais"]')))
            element.click()
            time.sleep(2)
        except:
            break
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', {'class': 'prateleira__name'})
    links = [item['href'] for item in links]
    driver.quit()
    return links

def get_product_data(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    descricao = soup.find('h1').text
    try:
        preco = soup.find('strong', {'class': 'skuBestPrice'}).text
        float(preco.split(' ')[1].replace(',', '.'))
    except:
        preco = np.nan
    imagem = soup.find('div', {'id': 'image'}).find('a')['href']
    ean = re.findall(r'(\d+)', re.findall(r'/\d+\w', url)[0])[0]
    return (descricao, preco, ean, imagem)
