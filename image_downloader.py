from bs4 import *
import requests as rq 
import os
import uuid

def image_downloader(url):
    r2 = rq.get(url)

    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []

    x = soup2.select('img[src]')

    for img in x:
        if img['src'][:6] == "http:/":
            links.append(img['src'])

    # for l in links:
    #     print(l)

    # print(len(links))

    i = 1
    for index, img_link in enumerate(links):
        if i<= 20:
            img_data = rq.get(img_link).content
            with open('src/dataset/' + str(uuid.uuid4())[:7] + '.jpg', 'wb+') as f:
                f.write(img_data)
            i += 1
        else:
            f.close()
            break

if __name__ == "__main__":
    url = "https://www.google.com"
    image_downloader(url)