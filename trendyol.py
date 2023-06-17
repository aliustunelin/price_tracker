import requests
from bs4 import BeautifulSoup


def trendyolGetPrice(url,paramPrice):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55"
    }

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')



    #productTitle=htmlPage.find("h1", class_="pr-new-br")

    # ürünlerin divi prdct-cntnr-wrppr
    # 1 tane ürünün firma adi 
    # 1tane ürünün adı prdct-desc-cntnr-name
    # 1 tane ürünün fiyat divi prc-box-dscntd

    #price list
    priceHtml = htmlPage.find_all(class_="prc-box-dscntd")
    productTitleHtml = htmlPage.find_all("span", class_="prdct-desc-cntnr-name")
    priceCount = []
    productTitle = []
    trendyol = []

    
    for i in range(len(priceHtml)):
        priceCount.append(priceHtml[i].getText())
        productTitle.append(productTitleHtml[i].getText())
        trendyol.append(
            {
                 productTitleHtml[i].getText() : priceHtml[i].getText()
            }
        )


    print(len(trendyol))
    print("-------")
    print(trendyol)


    
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

