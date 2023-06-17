import requests
from bs4 import BeautifulSoup
import time

url1="https://www.trendyol.com/reshell/sac-dokulmesine-karsi-bakim-sampuani-at-kuyrugu-ozlu-tuzsuz-kolajen-ve-keratin-katkili-500-ml-p-167311621?boutiqueId=61&merchantId=370159&sav=true"
# trendyol search url
# https://www.trendyol.com/sr?q=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&qt=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&st=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&os=1


def checkPrice(url,paramPrice):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
    }

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')

    productTitle=htmlPage.find("h1", class_="pr-new-br")

    price = htmlPage.find("span",class_="prc-dsc")

    print("aaaaaaaaaaaaaaaaaa")
    print(productTitle.getText())
    print(price.getText().replace(" TL",""))
    print("aaaaaaaaaaaaaaaaaa")
    '''
    convertedPrice = float(price.replace(",",".").replace(" TL",""))

    if(convertedPrice <= paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle,url)
        print("KIME_EMAIL","Ürünün fiyatı düştü👍👍", htmlEmailContent)
    else:
        print("ürün fiyatı düşmedi")
    '''
while(True):
    checkPrice(url1,100)
    time.sleep(3)

