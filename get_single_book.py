# -*- coding: utf-8 -*-
# @Time   : 2021/4/25 20:04
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : get_single_book.py

from get_title import page_title
import os


def jinjiang_novel_content(book_url):
    novel_folder_name = page_title(book_url, 'gb18030')
    # print(novel_folder_name)
    if not os.path.exists('晋江小说合集/' + novel_folder_name):
        os.mkdir('晋江小说合集/' + novel_folder_name)

    


jinjiang_novel_content('https://wap.jjwxc.net/book2/4456728')
