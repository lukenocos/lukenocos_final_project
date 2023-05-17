# file created by Luke Nocos

'''
GOALS:

to scrape all the data from a shopify website and generate link
to purchase a desired item through keywords.

'''

# sources: 
# https://www.youtube.com/watch?v=p3Z-qtUp4p8&ab_channel=JohnWatsonRooney
# https://www.youtube.com/watch?v=-31Or1HSmyo&ab_channel=straight_code
# https://www.youtube.com/watch?v=bLCx348H0Kw&ab_channel=YasCode
# https://github.com/abocati/shopify-bot/blob/master/checkout-shopify.py


import requests
import time
import json
import urllib3
import codecs
import random
from settings import *
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.common.by import By
import time

session = requests.session()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
product = None

def get_products(session):
    '''
    Gets all the products from a Shopify site.
    '''
    # Download the products
    link = base_url + "/products.json"
    r = session.get(link, verify=False)

    # Load the product data
    products_json = json.loads(r.text)
    products = products_json["products"]

    # Return the products
    return products


def keyword_search(session, products, keywords):
    '''
    Searches through given products from a Shopify site to find the a product
    containing all the defined keywords.
    '''
    # Go through each product
    for product in products:
        # Set a counter to check if all the keywords are found
        keys = 0
        # Go through each keyword
        for keyword in keywords:
            # If the keyword exists in the title
            if(keyword.upper() in product["title"].upper()):
                # Increment the counter
                keys += 1
            # If all the keywords were found
            if(keys == len(keywords)):
                # Return the product
                return product


def find_size(session, product, size):
    '''
    Find the specified size of a product from a Shopify site.
    '''
    # Go through each variant for the product
    for variant in product["variants"]:
        # Check if the size is found
        
        if(size == variant["title"]):
            variant = str(variant["id"])

            # Return the variant for the size
            return variant
        

def generate_cart_link(session, variant):
    '''
    Generate the add to cart link for a Shopify site given a variant ID.
    '''
    # Create the link to add the product to cart
    link = base_url + "/cart/" + variant + ":1"

    # Return the link
    return link

def execute_page():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get(cart_link)

    driver.find_element(By.ID, 'email').send_keys(email)
    time.sleep(0.75)
    driver.find_element(By.ID, 'TextField1').send_keys(first_name)
    time.sleep(0.75)
    driver.find_element(By.ID, 'TextField2').send_keys(last_name)
    time.sleep(0.75)
    driver.find_element(By.ID, 'address1').send_keys(address)
    time.sleep(0.75)
    driver.find_element(By.ID, 'TextField4').send_keys(appt)

    driver.find_element(By.ID, 'TextField5').send_keys(city)

    driver.find_element(By.ID, 'TextField6').send_keys(zipcode)



# Loop until a product containing all the keywords is found
while(product == None):
    # Grab all the products on the site
    products = get_products(session)
    # Grab the product defined by keywords
    product = keyword_search(session, products, keywords)
    

# Get the variant ID for the size
variant = find_size(session, product, size)

# Get the cart link
cart_link = generate_cart_link(session, variant)


print ("found product link and adding to cart: " + cart_link)
execute_page()
# print (product)


