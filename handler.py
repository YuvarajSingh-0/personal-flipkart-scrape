# import json


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v3.0! Your function executed successfully!",
#         "input": event,
#     }

#     return {"statusCode": 200, "body": json.dumps(body)}


import math
import os
import json
import requests
import random
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()


def scrape(event, context):
    pantryid = os.environ.get('PANTRY_ID')
    pantry_url = str(
        f"https://api.npoint.io/{pantryid}")
    webhook_url = os.environ.get('WEBHOOK_URL')
    links_prices = requests.get(pantry_url).json()
    # print(links_prices)

    for item in links_prices:
        html_text = requests.get(item["url"]).text
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Accessing the 'text' attribute (which is actually not an HTML attribute but the text content of a tag)
        title = soup.find('span', {'class': "VU-ZEz"})
        title = title.text if title else 'No title found'
        
        # Finding an 'img' tag and accessing its 'src' attribute
        img = soup.find('img', {'class': "DByuf4 IZexXJ jLEJ7H"})
        img_url = img['src'] if img else 'No image found'
        
        # Accessing the 'text' content of a 'div' tag
        curr_price = soup.find('div', {'class': "Nx9bqj CxhGGd"}).text if soup.find('div', {'class': "Nx9bqj CxhGGd"}) else 'No price found'
        
        # Example of accessing other attributes, e.g., 'alt' of an image
        img_alt = img['alt'] if img and 'alt' in img.attrs else 'No alt text'
        
        # print(f"{prices[url][:]}")
        # print(f"{curr_price}")
        if (len(item.get("price")) == 0):
            data = {
                "content": "",
                "username": "Spidey Bot",
                "embeds": [{
                    "author": {
                        "name": "Price Tracking started for this product",
                        "icon_url": "https://i.imgur.com/R66g1Pe.jpg"
                    },
                    "title": f"{title} \n \n ",
                    "url": f"{item['url']}",
                    "description": f"**Price** : `{curr_price}` \n \n **Link** -> [{title}]({item['url']})'",
                    "color": math.floor(random.random() * 16777214) + 1,
                    "image": {
                        "url": f"{img_url}"
                    }
                },]
            }
            item["price"] = curr_price
            x = requests.post(pantry_url, json=links_prices)
            r = requests.post(webhook_url, json=data)
            continue

        if (curr_price == item["price"]):
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
                "url": f"{item['url']}",
                "description": f"**Price** : `{curr_price}`   ~~`{item['price'][0]} {item['price'][1:]}`~~ \n \n **Link** -> [{title}]({item['url']})'",
                "color": math.floor(random.random() * 16777214) + 1,
                "image": {
                    "url": f"{img_url}"
                }
            },
            ]
        }
        index = links_prices.index(item)
        links_prices[index]["price"] = curr_price
        x = requests.post(pantry_url, json=links_prices)
        print(x.text)
        # print(data)
        r = requests.post(webhook_url, json=data)  # type: ignore
        print(r)
    # print("Sleeping for 4 hours....")
    return {
        'statusCode': 200,
        'body': json.dumps('Check Done!')
    }


if __name__ == '__main__':
    scrape(None, None)
