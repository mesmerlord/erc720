import cloudscraper
import requests
import pandas as pd
import bs4
import json
import csv
import random

proxy = pd.read_csv("prox.csv")
proxiesToList = proxy.values.tolist()

finalPage = 2735
def getTok(num):
    newscrape = cloudscraper.create_scraper()
    # for proxy in proxiesToList:
        
    #     splitprox = random.choice(proxiesToList)[0].split(":")
    #     proxyy = f'http://{splitprox[2]}:{splitprox[3]}@{splitprox[0]}:{splitprox[1]}'
    #     response = newscrape.get(f"https://ethplorer.io/service/service.php?page={num}&pageSize=100&search=c",proxies = {'http':proxyy, 'https':proxyy} )

    response = newscrape.get(f"https://ethplorer.io/service/service.php?page={num}&pageSize=100&search=c")
    jsonLoad = json.loads(response.content)['results']
    finalList = []
    for x in jsonLoad:
        finalList.append(x)
    return finalList

for x in range(finalPage):
    name = getTok(x+1)
    with open('new.csv','a',encoding="utf-8", newline = "") as newfile:
        writer = csv.writer(newfile)
        for line in name:
            writer.writerow(line)
