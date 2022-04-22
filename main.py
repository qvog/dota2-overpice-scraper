from urllib import response
from fake_useragent import UserAgent
import requests
import json

ua = UserAgent()

def collect_data(rarity_item=5):

    offset = 0
    step_size = 60
    result = []

    while True:
        for item in range(offset, offset + step_size, 60):

            url = f'https://inventories.cs.money/5.0/load_bots_inventory/570?buyBonus=40&isStore=true&limit=60&maxPrice=10000&minPrice=50&offset={item}&order=desc&rarity={rarity_item}&sort=price&withStack=true'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )

            offset += step_size

            data = response.json()

            items = data.get('items')

            print(type(items))

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_quality = i.get('quality')
                    item_img = i.get('img')
                    item_price = i.get('price')
                    item_overprice = i.get('overprice')

                    result.append(
                        {
                            'quality': item_quality,
                            'img': item_img,
                            'price': item_price,
                            'overprice': item_overprice,
                        }
                    )

        if len(items) < 60:
            break
    
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    
    print(len(result))

def main(): 
    collect_data()

if __name__ == '__main__':
    main()

