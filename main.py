import time
from trendyol import trendyolGetPrice

url1="https://www.trendyol.com/sr?q=kirmizi ayakkabi&qt=kirmizi ayakkabi&st=kirmizi ayakkabi&os=1"
#trendyol tek ürün url
# https://www.trendyol.com/reshell/sac-dokulmesine-karsi-bakim-sampuani-at-kuyrugu-ozlu-tuzsuz-kolajen-ve-keratin-katkili-500-ml-p-167311621?boutiqueId=61&merchantId=370159&sav=true
# trendyol search url
# https://www.trendyol.com/sr?q=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&qt=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&st=k%C4%B1rm%C4%B1z%C4%B1%20ayakkab%C4%B1&os=1


while(True):
    trendyolGetPrice(url1,100)
    time.sleep(3)

