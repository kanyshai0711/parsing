# pip3 install -r req.txt установка библиотек

# pip3 install -> название_библиотеки

# pip freeze -> просмотр установленных библиотек

# python3 -m venv venv -> создание виртуального

# .venv/bin/active -> активизация виртуального окружения

import requests 
from bs4 import BeautifulSoup 
import csv

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow([data['title'], data['image'], data['price'], data['description']])

def get_html(url):
    response = requests.get(url)
    # print(response.text)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html,'lxml')
    page_list = soup.find('div', class_ = 'pager-wrap').find('ul',class_ = 'pagination').find_all('li')
    # print(page_list)
    last_page = page_list[-1].text
    # print(last_page)
    return int(last_page)

get_total_pages(get_html('https://www.kivano.kg/noutbuki'))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    products = soup.find('div', class_ ='list-view').find_all('div',class_='item')
    # print(products)
    for product in products:
        title = product.find('div',class_ = 'listbox_title').find('strong').text
        image = 'https://www.kivano.kg/' + product.find('img').get('src')
        price = product.find('div',class_='listbox_price').find('strong').text
        description = product.find('div', class_= 'product_text pull-left').text


        dict_ = {'title': title, 'image': image,'price': price, 'description': description}
        # print(dict_)'
        write_to_csv(dict_)
with open('data.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['title         ','image           ','price         ', 'description          '])

def main():
    url = "https://www.kivano.kg/noutbuki"
    pages = '?page='
    html = get_html(url)
    number = get_total_pages(html)
    get_data(html)
    for i in range(2, number+1):
        url_with_page = url + pages + str(i)
        print(url_with_page)
        html = get_html(url_with_page)
        get_data(html)

main()





























