from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path='/Users/marcooliveira/chromedriver', options=chrome_options)

driver.set_window_size(1024, 768)

url = "https://www.jdsports.pt/product/preto-fred-perry-casaco-hooded-brentham-lightweight/498483_jdsportspt/"

try:
    request = requests.get(url)
except Exception as error:
    print(error)
jd_html = request.text
soup = BeautifulSoup(jd_html, 'html.parser')

div_tamanhos = soup.find("div", class_="options")
tamanhos = div_tamanhos.find_all("button", class_="btn") #a lista tem o numero de buttons

try:
    driver.get(url)
except:
    print("Erro")

lista_tamanhos = []
i = 1
sleep(1)
botao_cookies = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/button[2]')
botao_cookies.click()
while i <= len(tamanhos):
    xpath = f'//*[@id="productSizeStock"]/button[{i}]'
    try:
        tamanho_botao = driver.find_element_by_xpath(xpath)
        tamanho_botao.click()
    except:
        pass
    lista_tamanhos.append(tamanho_botao.text)
    i = i + 1
    print(lista_tamanhos)

   
