# -*- coding: utf-8 -*-
# @Time   : 2021/4/25 20:04
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_single_book.py

import os

import requests
from bs4 import BeautifulSoup

from get_title import page_title


def jinjiang_novel_content(chap_url, encode='utf-8'):
    res = requests.get(chap_url)
    res.encoding = encode
    # sel = '#js_content'
    # results = r.html.find(sel)
    soup = BeautifulSoup(res.text, "lxml")
    content = soup.select_one(
        'body > div.grid-c > div > div:nth-child(13) > div:nth-child(2) > ul > li:nth-child(1)').text
    # body > div.grid-c > div > div:nth-child(14) > div:nth-child(2) > ul > li
    # body > div.grid-c > div > div:nth-child(14) > div:nth-child(2) > ul > li:nth-child(1)
    # body > div.grid - c > div > div: nth - child(14) > div:nth - child(2) > ul > li: nth - child(1)
    content.replace('&nbsp;', '\n').replace("&emsp;", "  ")
    # content = '\n'.join(content[0].text.split())
    # print('\n'.join(content[0].text.split()))
    print(content)
    return content

def jinjiang_novel_content_14(chap_url, encode='utf-8'):
    res = requests.get(chap_url)
    res.encoding = encode
    # sel = '#js_content'
    # results = r.html.find(sel)
    soup = BeautifulSoup(res.text, "lxml")
    content = soup.select_one(
        'body > div.grid-c > div > div:nth-child(14) > div:nth-child(2) > ul > li:nth-child(1)').text
    # body > div.grid-c > div > div:nth-child(14) > div:nth-child(2) > ul > li
    # body > div.grid-c > div > div:nth-child(14) > div:nth-child(2) > ul > li:nth-child(1)
    # body > div.grid - c > div > div: nth - child(14) > div:nth - child(2) > ul > li: nth - child(1)
    content.replace('&nbsp;', '\n').replace("&emsp;", "  ")
    # content = '\n'.join(content[0].text.split())
    # print('\n'.join(content[0].text.split()))
    print(content)
    return content


def whole_chaps_num(book_url, encode='utf-8'):
    res = requests.get(book_url)
    res.encoding = encode
    # sel = '#js_content'
    # results = r.html.find(sel)
    soup = BeautifulSoup(res.text, "lxml")
    chaps_nums = soup.select_one(
        'body > div.grid-c > div:nth-child(11) > div:nth-child(3) > a:nth-child(21) > span:nth-child(1)').text
    chaps_nums = chaps_nums.replace('.', '')
    chaps_nums = int(chaps_nums)
    return chaps_nums
    # print(chaps_nums)


def run_whole_book(book_url, encode='utf-8'):
    novel_title = page_title(book_url, encode)
    # print(novel_folder_name)
    novel_folder_name = '晋江小说合集/' + novel_title
    if not os.path.exists(novel_folder_name):
        os.mkdir(novel_folder_name)

    all_chaps = whole_chaps_num(book_url, encode)

    for chap_num in range(25, all_chaps):
        chap = book_url + '/' + str(chap_num)
        try:
            res = jinjiang_novel_content(chap, encode)
        except:
            try:
                res = jinjiang_novel_content_14(chap, encode)
            except:
                print(chap_num)
                break
        # res = jinjiang_novel_content(chap, encode)
        with open(novel_folder_name + '/Chapter ' + str(chap_num) + '.txt', 'w', encoding='utf-8') as f:
            f.write(res)


if __name__ == '__main__':
    run_whole_book('https://wap.jjwxc.net/book2/5343061', 'gb18030')
# jinjiang_novel_content('https://wap.jjwxc.net/book2/5343061', 'gb18030')
# whole_chaps_num('https://wap.jjwxc.net/book2/5343061', 'gb18030')
