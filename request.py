import requests
from bs4 import BeautifulSoup
import randomHeader

print(randomHeader.randHeader())

data = {'viewmode': 'contents'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
req = requests.get("http://blog.csdn.net/zz110731", params=data, headers=headers)

soup = BeautifulSoup(req.text)

articles = soup.find_all(class_='link_title')

k = 0
while k < 100:
    m = 0
    for article in articles:
        link = 'http://blog.csdn.net' + article.a['href']
        # print(link)
        head = randomHeader.randHeader()
        qq = requests.get(link, headers=head)
        # print(head)
        m = m + 1
        print(m)
        print(qq)
    k  = k + 1
    print("第{0}次，请求完毕".format(k))

