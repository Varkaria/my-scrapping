from bs4 import BeautifulSoup
import requests
import os

print('Please input your miku-doujin id :')
doujin_id = input()

print('Requesting from url')
url = requests.get(f'https://miku-doujin.com/{doujin_id}/')

print('Scrapping from data')
soup = BeautifulSoup(url.content, 'html.parser')
data = soup.find(id='manga-content')
picture_selector = 'img.lazy'
pic = data.select(picture_selector)
os.mkdir(soup.title.string)

count = 1
for image in pic:
    print(f'Downloading page {count}')
    with requests.get(image['data-src']) as r:
        img_data = r.content
    with open(f'{soup.title.string}/{count}.jpg', 'wb') as handler:
        handler.write(img_data)
    count = count + 1

print('Finished!')