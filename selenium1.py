# coding=utf-8
import xlrd
import time
import random
import requests
import re
import pymongo
from selenium import webdriver


def text(a):
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get(a)
    time.sleep(2)
    driver.find_element_by_id('TPL_username_1').send_keys('18389555136')
    driver.find_element_by_id('TPL_password_1').send_keys('12345678lx')
    driver.find_element_by_id('J_SubmitStatic').click()

    # 提取书名
    data = xlrd.open_workbook('/home/lx/PycharmProjects/book.xlsx')
    table = data.sheets()[0]
    # 获取列数
    # nrows = table.nrows

    i = 1
    while i < 10810:
        # 构造url
        name = table.row_values(i)
        # 搜索书名
        # print name[0]
        driver.find_element_by_id('q').clear()
        driver.find_element_by_id('q').send_keys(name[0])
        time.sleep(2)

        # 点击搜索按钮
        driver.find_element_by_xpath('//*[@id="J_SearchForm"]/button').click()

        # 点击销量排行按钮
        driver.find_element_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[3]/a').click()



        time.sleep(7)
        # 获取当前网页源码
        cont = driver.page_source


        # 匹配价格
        c = re.findall('<strong>(.*?)</strong>', cont, re.S)
        if len(c) == 0:
            print u'快点暂停我……'
            print c
        # 匹配销量
        d = re.findall('<div class="deal-cnt">(.*?)</div>', cont, re.S)

        # time.sleep(3)
        # # 连接本机数据库
        # conn = pymongo.MongoClient('localhost', 27017)
        # # 进入指定名称的数据库
        # db = conn.book
        # # 获取数据库里的 names 集合
        # names = db.names
        # u = dict(bookname=name, price=c, sales=d)
        # # 将数据插入到 users 集合
        # db.names.insert(u)
        print i,c,d,
        i += 1
        time.sleep(random.randint(10, 15))



if __name__ == "__main__":
    a = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.7724922.1997563269.1.QXzT2G&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
    text(a)
