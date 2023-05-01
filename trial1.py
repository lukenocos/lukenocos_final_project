from bs4 import BeautifulSoup as soup
import requests
import time
import json
import urllib3
import codecs
import random
from settings import *



def get_products():
    link = base_url + "/products.json"
    r = requests.get(link , verify = False)

    products_json = json.loads(r.text)
    products = products_json['products']

    # return products


    for product in products:

        keys = 0 

        for keyword in keywords:

            if(keyword.upper() in product["title"].upper()):

                keys += 1

            if(keys == len(keywords)):
                print (product)

    for variant in product['variant']:

        if(size in variant['title']):
            variant = str(variant[id])
            
            return variant

    link = base_url + "/cart/" + variant + ":1"
    print (link)

get_products()



    

