# how about you import some bitches
import requests
from os import mkdir, sep
from random import randint
from threading import Thread

api = 'https://api.waifu.pics/nsfw/waifu'


def get(directory="bitches", amount=randint(50, 1000)):
    try:
        mkdir(directory)
    except Exception:
        pass
    for i in range(amount):
        print("Get Pics")
        Thread(target=bitches, args=(directory, amount)).start()


def bitches(dir_, amount=randint(50, 1000)):
    for i in range(amount):
        req_url = requests.get(api)
        url = req_url.json()['url']
        print(url)
        if not req_url.ok:
            print("error: "+req_url)
        with open(dir_+sep+url[21:], 'wb') as f:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                f.write(block)
