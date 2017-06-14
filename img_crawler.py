# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:10:42 2017

@author: john

Simple crawler for Baidu tieba
Just for fun~
Crawling url: http://tieba.baidu.com/f?kw=%E6%91%84%E5%BD%B1&ie=utf-8&tab=good&cid=6
This url is a threads list. 
Each thread includes many pictures of great natural scenery.

The default script downloads the first 5 pictures of each thread into local directory './img_dl/[thread title]/'. 

Current script can only crawl the 1st page.
To avoid crawling repeatly adding md5-check or url cache may help.
"""

import os
import re
import time
import requests
import datetime
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


def get_src_html(urlToGet):
    return  requests.get(urlToGet).text

def get_data(src):
    return urllib.request.urlopen(src)

def save_data(data, Id, suffix, prefix='', path='./img_dl'):
    if not os.path.isdir(path):
        os.makedirs((path))
        print("Directory %s was created." %path)
    with open(path+prefix+str(Id)+suffix, 'wb') as to_write:
        to_write.write(data)

def get_by_thread(thrd_url, thrd_title, first_n_img=-1, originImg=True):
    src_html = get_src_html(thrd_url)
    soup = BeautifulSoup(src_html,'lxml')
    img_items_raw = soup.select('.BDE_Image')
    img_origin_prefix = 'https://imgsa.baidu.com/forum/pic/item/'
    
    for cnt, item in enumerate(img_items_raw):
        if first_n_img > 0 and cnt > first_n_img-1:
            break
        img_src = item.get('src')
        if not originImg:
            img_src_origin = img_src
        else:
            img_src_origin_fname = img_src.split('/')[-1]
            img_src_origin = img_origin_prefix + img_src_origin_fname
        img_data = get_data(img_src_origin).read()
        banned_sybs = '<>/\|:""*?'
        table = ''.maketrans(banned_sybs, '_'*len(banned_sybs))
        thrd_title_dir = thrd_title.translate(table)
        save_data(img_data, cnt, '.jpg', 'IMG'+'_', './img_dl/'+thrd_title_dir+'/')
        time.sleep(0.01)
        print('No. {} image saved'.format(cnt))
        print('img_url: ', img_src_origin)

url_all = 'http://tieba.baidu.com/f?kw=%E6%91%84%E5%BD%B1&ie=utf-8&tab=good&cid=6'
src_html = get_src_html(url_all)

soup = BeautifulSoup(src_html,'lxml')
threads_raw = soup.select('.threadlist_title')

thrd_href_prefix = 'https://tieba.baidu.com'
#title_cond = re.compile('[第][0-9]?[0-9]')
title_cond = re.compile('')

for thrd in threads_raw:
    thrd_title = thrd.select_one('a').get_text()
    if os.path.exists('./img_dl/'+thrd_title+'/'):
        print('Skip thread: ', thrd_title)
        continue
    if title_cond.findall(thrd_title):
        thrd_href = thrd_href_prefix + thrd.select_one('a').get('href') +'?see_lz=1'
        print('\nCrawling thread: ', thrd_title)
        get_by_thread(thrd_href, thrd_title, 5)
        time.sleep(0.01)
