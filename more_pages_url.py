# -*- coding: utf-8 -*-
# @Time   : 2021/4/25 19:49
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : more_pages_url.py

from get_url import single_page_links


def get_more_pages(start_page, end_page, root_url):
    for page_num in range(start_page, end_page):
        url = root_url + '/' + str(page_num)  # 根url不应该有'/'

        res = single_page_links(url)


jinjiang_wap = 'https://wap.jjwxc.net/ranks/recommend/noyq'
get_more_pages(1, 43, jinjiang_wap)
