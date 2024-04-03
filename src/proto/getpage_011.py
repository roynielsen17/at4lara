#!/usr/bin/env -S python -u
"""
"""

import json
import requests
from bs4 import BeautifulSoup
from bs2json import BS2Json


list_of_urls = [
         'https://www.kdnuggets.com/2023/04/stepbystep-guide-web-scraping-python-beautiful-soup.html',
        ]

scraped_data = []
author = ""

## Scraping Function
def start_scrape():
   
    '''
    https://pypi.org/project/bs2json/ 
    from bs2json import bs2json
    bs2json = bs2json.BS2Json(html)
    # Convert soup to JSON
    # json_obj = bs2json.convert()
    html = '<html><head><title>Page Title</title></head><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'
    bs2json = bs2json(html)
    # Convert soup to JSON
    json_obj = bs2json.convert()
    # Save JSON to file
    bs2json.save()
    # Print prettified output
    '''

    ## Loop Through List of URLs
    for url in list_of_urls:
        
        ## Send Request
        response = requests.get(url)

        if response.status_code == 200:
            print(response.text)

            # soup = BeautifulSoup(response, 'html.parser')
            htmlData = response.content
            print(htmlData)
            parsedData = BeautifulSoup(htmlData, "html.parser")
            print("**********************************************")
            print("**********************************************")
            print("**********************************************")
            print(parsedData.prettify())
            json_results = BS2Json(parsedData).convert()
            print("**********************************************")
            print("**********************************************")
            print("**********************************************")
            print(json.dumps(str(json_results), indent=2))
            print("**********************************************")
            print("**********************************************")
            print("**********************************************")

            for key in json_results.keys():
               if key == "author" : 
                   author = author["author"]
                   print(author)
               if key == "Author" :
                   author = author["Author"]
                   print(author)
               if key == "AUTHOR" : 
                   author = author["AUTHOR"]
                   print(author)
            

            for item in json_results:
                if isinstance(item, dict):
                    :wq!




exit()
            
            ## Parse Data
            # soup = BeautifulSoup(response.content, 'html.parser')
            # products = soup.select('product-item')
            for product in products:
                price = product.select('span.price')[0].get_text().replace('\nSale price£', '')
                url = product.select('div.product-item-meta a')[0]['href']
                
                ## Add To Data Output
                scraped_data.append({
                    'name': name,
                    'price': price,
                    'url': 'https://www.chocolate.co.uk' + url
                })


if __name__ == "__main__":
    start_scrape()
    # print(scraped_data)
    
