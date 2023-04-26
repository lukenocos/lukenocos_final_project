# file created by Luke Nocos

# sources: 
# https://www.youtube.com/watch?v=p3Z-qtUp4p8&ab_channel=JohnWatsonRooney


import requests 
import webbrowser




class ShopifyScraper():
    def __init__(self, url):
        self.url = url

    def downloadjson(self, page):
        r = requests.get(self.url + f"products.json?limit=250&page={page}")
        if r.status_code != 200:
            print ("Bad Status Code: ", r.status_code)
        if len((r.json())['products']) > 0:
            data = r.json()['products']
            return data 
        else:
            return
    
    def parsejson(self, jsondata):

        products =[]

        for product in jsondata:
            prod_id = product['id']
            prod_title = product['title']
            
            for v in product['variants']:
                item = {
                    "id": prod_id,
                    "title": prod_title,
                    "sku": v['sku'],
                    "price": v['price'],
                    "available": v['available']
                }

            print(item)

            return
        

        
        
        
        
    
Kith = ShopifyScraper('https://kith.com/')
data = Kith.downloadjson(3)
Kith.parsejson(data)
     





        
        
        
        





