import requests
from bs4 import BeautifulSoup
from requests.api import get



def get_current_price(steam_url:str):

    url = 'https://store.steampowered.com/app/'+ steam_url

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    # TODO: need to reverse these in cases where bundles appear

    sale_result = soup.find_all("div" , {"class":"discount_final_price"}, limit=1)

    if sale_result:

        print('game is on sale')
        price_dirty = sale_result[0].text

        current_price = float(price_dirty.strip().replace("$",''))

        return current_price

    else:

        print('game is not on sale')
        result = soup.find_all("div", {"class":"game_purchase_price price"}, limit=1)
        price_dirty = result[0].text

        current_price = float(price_dirty.strip().replace("$",''))

        return current_price

if __name__ == "__main__":
    current_price = get_current_price(steam_url='1466860/Age_of_Empires_IV/')
    print(current_price)