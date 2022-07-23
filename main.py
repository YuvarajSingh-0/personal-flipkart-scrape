import math
import time
import os
import requests
import random
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
load_dotenv()

products_url = ["https://dl.flipkart.com/s/Hod29OuuuN",
                "https://www.flipkart.com/fastrack-analog-watch-men/p/itm7759c653a3b95", ]
webhook_url = os.environ.get('WEBHOOK_URL')
prices = {}
print(webhook_url)
for product_url in products_url:
    prices[product_url] = "₹0"
# print(prices)
while(True):
    for url in products_url:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        title = soup.find('span', {'class': "B_NuCI"}).text
        img = soup.find('img', {'class': "q6DClP"})
        img_url = img['src']
        curr_price = soup.find(
            'div', {'class': "_30jeq3 _16Jk6d"}).text
        if(curr_price != prices[url]):
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
                    "description": f"**Price** : `{curr_price}`   ~~`{prices[url]}`~~ \n \n **Link** -> [{title}]({url})'",
                    "color": math.floor(random.random() * 16777214) + 1,
                    "image": {
                        "url": f"{img_url}"
                    }
                },
                ]
            }
            r = requests.post(webhook_url, json=data)
            prices[url] = curr_price
        # print(curr_price, r.text)
        print(prices)
    time.sleep(7200)


# if __name__ == '__main__':
#     app.run(port=os.getenv('PORT', 5000))
