# coding = utf-8

import requests
from bs4 import BeautifulSoup


def page_title(url, encode='utf-8'):
    try:
        res = requests.get(url)
        res.encoding = encode
        soup = BeautifulSoup(res.text, 'lxml')
        web_title = soup.head.title.text
        # print(web_title)

    except:
        pass
    return web_title


# page_title('https://wap.jjwxc.net/book2/4456728', 'gb18030')
