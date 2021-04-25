# -*- coding: utf-8 -*-
# @Time   : 2021/4/25 22:49
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : run_crawl_all_books.py

from get_url import single_page_links
from get_single_book import run_whole_book


def run_crawl(start_page, end_page, root_url):
    '''
    # 此处为了防止不从0页开始
    # 晋江的机制如果页数非1-43则返回初始页
    if start_page == 1:
        try:
            url = root_url
            res = single_page_links(url)

        except:
            print('从第0页加载起')
    '''
    for page_num in range(start_page, end_page):
        url = root_url + '/' + str(page_num)  # 填写根url时不应该有'/'
        # print(url)

        single_page_urls = single_page_links(url)
        # print(single_page_urls)
        for book_url in single_page_urls:
            print(book_url)
            run_whole_book(book_url, 'gb18030')


if __name__ == '__main__':
    jinjiang_wap = 'https://wap.jjwxc.net/ranks/recommend/noyq'
    run_crawl(0, 44, jinjiang_wap)
