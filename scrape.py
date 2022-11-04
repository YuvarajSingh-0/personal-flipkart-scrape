import math
import time
import os
import requests
import random
import time
import json
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
    # links_prices = json.loads(links_prices.text)
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
        print(f"{prices[url][:]}")
        print(f"{curr_price}")
        if (curr_price != prices[url]):
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
            # with open('links_prices.json', 'w') as f:
            links_prices['prices'][url] = curr_price
            x = requests.post(pantry_url, json=links_prices)
            # json.dump(links_prices, f, indent=4)
            print(x.text)

            r = requests.post(webhook_url, json=data)
    print("Sleeping for 4 hours....")
    # time.sleep(7200)


if __name__ == '__main__':
    lambda_handler(None, None)
#        app.run(port=os.getenv('PORT', 5000))
