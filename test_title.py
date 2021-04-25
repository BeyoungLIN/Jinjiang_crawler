# -*- coding: utf-8 -*-
# @Time   : 2021/4/25 20:15
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : test_title.py

import requests
from bs4 import BeautifulSoup
res = requests.get("https://wap.jjwxc.net/book2/4456728n")
res.encoding = 'gb18030'
soup = BeautifulSoup(res.text,'lxml')
print(soup.head.title.text)