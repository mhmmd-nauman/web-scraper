# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:19:22 2020

@author: Nauman
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



startTime = time.time()
# use this manager Queue instead of multiprocessing Queue as that causes error
p = {}
pageNo = 1
qcount = 0
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store ratings of the product
results = []

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    
r = requests.get("https://www.amazon.com/s?k=laptops&page="+str(pageNo), headers=headers)#, proxies=proxies)
content = r.content
soup = BeautifulSoup(content)
#print(soup.encode('utf-8')) 
# uncomment this in case there is some non UTF-8 character in the content and
# you get error
for d in soup.findAll('div', attrs={'class':'sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28'}):
    name = d.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
    price = d.find('span', attrs={'class':'a-offscreen'})
    rating = d.find('span', attrs={'class':'a-icon-alt'})
   # print(name)
    if name is not None:
        products.append(name.text)
    if price is not None:
        prices.append(price.text)
    else:
        prices.append("0")
    if rating is not None:  
        ratings.append(rating.text)

print("I m here")

print("total time taken: ", str(time.time()-startTime), " qcount: ", qcount)
#print(q.get())
df = pd.DataFrame({'Product Name':products, 'Price':prices, 'Ratings':ratings})
print(df)
df.to_csv('products.csv', index=False, encoding='utf-8')