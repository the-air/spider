# coding=utf-8
import time
import xlrd
import random
import re
import requests

from splinter import Browser


def splinter(url):
    browser = Browser(driver_name='chrome')
    browser.visit(url)
    # 登陆
    browser.find_by_id('TPL_username_1').fill('18389555136')
    browser.find_by_id('TPL_password_1').fill('12345678lx')
    browser.find_by_id('J_SubmitStatic').click()

    # 提取书名
    data = xlrd.open_workbook('/home/lx/PycharmProjects/book.xlsx')
    table = data.sheets()[0]

    i = 1
    while i < 10810:
        # 导入书本信息
        name = table.row_values(i)
        s = '&sort=sale-desc'
        ip = 'https://s.taobao.com/search?q=' + name[0] + s
        cont = requests.get(url=ip).content
        print cont,
        # 回到淘宝首页
        browser.visit('https://www.taobao.com/')

        time.sleep(random.randint(2, 5))

        # 搜索书本信息
        browser.find_by_id('q').fill(name)
        time.sleep(random.randint(2, 5))

        # 点击搜索按钮
        browser.find_by_xpath('//*[@id="J_SearchForm"]/button').click()
        time.sleep(random.randint(2, 5))


        # 验证码出现机制，暂时手动验证
        if browser.find_by_id('checkcodeInput'):
            print u'打野爸爸，快来gank……'
            time.sleep(60)

        # 书本搜索不到时，报错，并跳转到下一个执行
        if browser.find_by_xpath('//*[@id="mainsrp-tips"]/div/div[2]/ul/li[1]'):
            print u'报告队长，发现%d是一名鬼子……' % i
            i += 1
            break

        # 点击销量按钮
        browser.find_by_xpath('//*[@id="J_relative"]/div[1]/div/ul/li[3]/a').click()





        # 获取当前网页的源代码
        a = browser.html


        # 获取书本标题
        # title = re.findall('"raw_title":"(.*?)"', a, re.S)

        # 匹配出书本的价格信息
        price = re.findall('"view_price":"(.*?)"', a, re.S)

        # 匹配当前书本销量信息
        # sales = re.findall('"view_sales":"(.*?)收货"', a, re.S)

        # 打印消息，方便调试
        # print a,

            # i,title,price,sales
        i += 1
        time.sleep(random.randint(10, 30))


if __name__ == '__main__':
    a = 'https://login.taobao.com/'
    splinter(a)
