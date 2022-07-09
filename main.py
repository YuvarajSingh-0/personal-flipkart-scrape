import time
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
load_dotenv()
old_price = "₹0"
productUrl = "https://dl.flipkart.com/s/Hod29OuuuN"
# productUrl = "https://www.flipkart.com/al-hind-sewing-machine-motor-full-copper-electric/p/itmed626d398dc69?pid=SMCFJA3APNTA5ZHK&lid=LSTSMCFJA3APNTA5ZHKZEP8ZQ&marketplace=FLIPKART&store=j9e&srno=b_1_5&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_3_4.dealCard.OMU_TJITB2TC6ZNU_3&otracker1=hp_omu_SECTIONED_manualRanking_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_3_NA_view-all_3&fm=neo%2Fmerchandising&iid=948c7e84-53c6-4bb8-950b-e419192d5f82.SMCFJA3APNTA5ZHK.SEARCH&ppt=browse&ppn=browse&ssid=xznzjdsddc0000001657316237526"
webhook_url = os.environ.get('WEBHOOK_URL')
print(webhook_url)
while(True):
    html_text = requests.get(productUrl).text
    soup = BeautifulSoup(html_text, 'html.parser')
    # print(soup.prettify())
    title = soup.find('span', {'class': "B_NuCI"}).text
    # print(title)
    img = soup.find('img', {'class': "q6DClP"})
    img_url = img['src']
    # print(img, img_url)
    curr_price = soup.find(
        'div', {'class': "_30jeq3 _16Jk6d"}).text
    if(curr_price != old_price):
        data = {
            "content": "",
            "username": "Spidey Bot",
            "embeds": [{
                "author": {
                    "name": "Price Change",
                    "icon_url": "https://i.imgur.com/R66g1Pe.jpg"
                },
                "title": f"{title} \n \n ",
                "url": f"{productUrl}",
                "description": f"**Price** : `{curr_price}` ~~{old_price}~~ \n \n **Link** -> [{title}]({productUrl})'",
                "color": 15258703,
                "image": {
                    "url": f"{img_url}"
                }
            },
            ]
        }
        r = requests.post(webhook_url, json=data)
        old_price = curr_price
    print(curr_price, r.text)
    # break
    time.sleep(3600)
