from bs4 import BeautifulSoup
import requests
import os

print('Please input your hentaithai topic id :')
doujin_id = input()

print('Requesting from url')
url = requests.get(f'https://hentaithai.com/forum/index.php?topic={doujin_id}')

print('Scrapping from data')
soup = BeautifulSoup(url.content, 'html.parser')
data = soup.find(style='margin-top:10px;')
picture_selector = '.img-fluid'
pic = data.select(picture_selector)
os.mkdir(soup.title.string[0:5])

count = 1
for image in pic:
    print(f'Downloading page {count}')
    with requests.get(image['src']) as r:
        img_data = r.content
    with open(f'{soup.title.string[0:5]}/{count}.jpg', 'wb') as handler:
        handler.write(img_data)
    count = count + 1