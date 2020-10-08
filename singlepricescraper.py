#How to save scraped data to a database

import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

#create connection
conn = sqlite3.connect('cputest.db')
c = conn.cursor()

#scraping function and insert
def getPriceOVC(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    store = 'OVC'
    title = soup.find('h1').text.strip().replace('\n','')
    price = soup.find('div', {'class': 'article_details_price'}).text.replace('*', '').strip().replace('£', '')
    stock = soup.find('span', {'class': 'popup-text'}).text.strip()
    c.execute('''INSERT INTO prices VALUES(?,?,?,?,?)''',(current_date, store, title, price, stock))
    #print(current_date, store, title, price, stock)
    return


#run funtion and commit changes to DB
getPriceOVC('https://www.overclockers.co.uk/amd-ryzen-9-3900x-twelve-core-4.6ghz-socket-am4-processor-retail-cp-3b5-am.html')
conn.commit()
print('complete.')

#select all from table
c.execute('''SELECT * FROM prices''')
results = c.fetchall()
print(results)

#close connection
conn.close()
