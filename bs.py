from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait


root = 'https://subslikescript.com'
website = f'{root}/movies'
driver_path = '/chromedriver.exe'

service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.implicitly_wait(2)
content = driver.page_source
driver.quit()

soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_='main-article')
articles = box.findAll('a', href=True)
links = []
for link in articles:
    link = link['href']
    links.append(f'{root}/{link}')

for link in links:
    result = requests.get(link)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator='  ')
    with open(f'/pages/{title}.txt', 'w', errors="ignore") as file:
        file.write(transcript) # must be string
# Creates blank spaces at the start of the line
# user = boxes.find('input', class_='form-control').get_text(strip=True, seperators=' ')
# with open(f'{user}.txt', 'w') as file:
#     file.write(user) # must be string







