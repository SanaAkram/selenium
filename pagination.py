from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

root = 'https://subslikescript.com'
web = f'{root}/movies'
driver_path = '/chromedriver.exe'
links = []


# gets content of any Website URL
def get_web_content(website=None):
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get(website)
    content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(content, 'lxml')
    return soup




soup = get_web_content(web)
box = soup.find('article', class_='main-article')
articles = box.find_all('a', href=True)
# getting total pages - pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text
for link in articles:
    link = link['href']
    links.append(f'{root}/{link}')

for page in range(1, int(last_page) + 1):
    p = f'{web}?page={page}'
    content = get_web_content(p)
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator='  ')
    with open(f'/pages/{title}.txt', 'w', errors="ignore") as file:
        file.write(transcript)  # must be string


for link in links:
    try:
        result = requests.get(link)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator='  ')
        with open(f'/pages/{title}.txt', 'w', errors="ignore") as file:
            file.write(transcript)  # must be string
    except Exception as e:
        print(e)
