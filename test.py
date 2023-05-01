# file created by Luke Nocos

# sources: 
# https://www.youtube.com/watch?v=p3Z-qtUp4p8&ab_channel=JohnWatsonRooney


import requests 
import webbrowser
from bs4 import BeautifulSoup
import json



r = requests.get("https://sagostudio.co/products.json")

products = json.loads(r.text)['products']

productkey = input("Enter Item Name: ")

for product in products:
    print (product['title'])
    productname = product['title']

    if productname == productkey:
        
    # if productname == "Grey Bandana Mesh Shorts":
        # print(productname)

        producturl = 'https://sagostudio.co/products/' + product['handle']
        print (producturl)

webbrowser.open(producturl)



