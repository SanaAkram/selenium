from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

yourmarket = 'https://mnpcourier.com/cplight/login'
driver_path = '/chromedriver.exe'

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(yourmarket)
driver.implicitly_wait(10)
content = driver.page_source
driver.quit()

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())

boxes = soup.find('div', class_='form-group')
user = boxes.find('input', class_='form-control')
