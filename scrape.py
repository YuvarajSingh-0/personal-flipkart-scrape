import math
import os
import json
import requests
import random
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()


def lambda_handler(event, context):
    pantryid = os.environ.get('PANTRYID')
    pantry_url = str(
        f"https://getpantry.cloud/apiv1/pantry/{pantryid}/basket/links_prices")
    webhook_url = os.environ.get('WEBHOOK_URL')
    links_prices = requests.get(
        pantry_url).json()
    print(links_prices)
    products_url = links_prices['products_url']
    prices = links_prices['prices']
    for url in products_url:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        title = soup.find('span', {'class': "B_NuCI"}).text
        img = soup.find('img', {'class': "q6DClP"})
        img_url = img['src']
        curr_price = soup.find(
            'div', {'class': "_30jeq3 _16Jk6d"}).text
        # print(f"{prices[url][:]}")
        print(f"{curr_price}")
        if (prices.get(url) == None):
            data = {
                "content": "",
                "username": "Spidey Bot",
                "embeds": [{
                    "author": {
                        "name": "Price Tracking started for this product",
                        "icon_url": "https://i.imgur.com/R66g1Pe.jpg"
                    },
                    "title": f"{title} \n \n ",
                    "url": f"{url}",
                    "description": f"**Price** : `{curr_price}` \n \n **Link** -> [{title}]({url})'",
                    "color": math.floor(random.random() * 16777214) + 1,
                    "image": {
                        "url": f"{img_url}"
                    }
                },
                ]
            }
            links_prices['prices'][url] = curr_price
            x = requests.post(pantry_url, json=links_prices)
            r = requests.post(webhook_url, json=data)
            continue

        if (curr_price == prices.get(url)):
            continue

        data = {
            "content": "",
            "username": "Spidey Bot",
            "embeds": [{
                "author": {
                    "name": "Price Change!",
                    "icon_url": "https://i.imgur.com/R66g1Pe.jpg"
                },
                "title": f"{title} \n \n ",
                "url": f"{url}",
                "description": f"**Price** : `{curr_price}`   ~~`{prices[url][0]} {prices[url][1:]}`~~ \n \n **Link** -> [{title}]({url})'",
                "color": math.floor(random.random() * 16777214) + 1,
                "image": {
                    "url": f"{img_url}"
                }
            },
            ]
        }
        links_prices['prices'][url] = curr_price
        x = requests.post(pantry_url, json=links_prices)
        print(x.text)
        r = requests.post(webhook_url, json=data)
        print(r)
    print("Sleeping for 4 hours....")


if __name__ == '__main__':
    lambda_handler(None, None)
#        app.run(port=os.getenv('PORT', 5000))
