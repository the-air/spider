# coding=utf-8
import requests
import re
import time
import random
import xlrd
import pymongo

# 构建目标url
data = xlrd.open_workbook('/home/lx/PycharmProjects/book.xlsx')
table = data.sheets()[0]
# 获取列数
nrows = table.nrows

i = 1
while i < 10810:
    # 构造url
    name = table.row_values(i)

    s = '&sort=sale-desc'
    ip = 'https://s.taobao.com/search?q=' + name[0] + s
    header = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"}

    cookie = {u'_cc_': u'UtASsssmfA%3D%3D',
              u'skt': u'87011a50e77aeb7b',
              u'existShop': u'MTQ1NzkyNzExNw%3D%3D',
              u'cookie17': u'Uoe3cr2mPHmUAQ%3D%3D',
              u'JSESSIONID': u'2547EABF87766D538AD2EA59BE22F371',
              u'uss': u'UteJrdqB9NEzwrAIg2EHbkxKrKoaEK6Iawjou1hXkFxqVmtVQjCU%2BbE2',
              u'cna': u'yCFtD1JYQk4CAWVRvgFWd4Nk',
              u'tg': u'0',
              u'tracknick': u'tb1339366017',
              u'cookie1': u'VTtB9k9riN0nVAItCdvbLNpg3a97m64VVnQpz5jhH44%3D',
              u'cookie2': u'2c65ea1fba7b26c1680d2e33baa30def',
              u'uc3': u'sg2=BxuQ0lMnn593MPlazvxGS9RPEkSlKP8pIUGwmPadXqw%3D&nk2=F5REPQL9MX4LrcYp&id2=Uoe3cr2mPHmUAQ%3D%3D&vt3=F8dASmw4fTMHAFsDKzs%3D&lg2=WqG3DMC9VAQiUQ%3D%3D',
              u'uc1': u'cookie14=UoWyiaN%2BGqlc3A%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=7&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0',
              u'whl': u'-1%260%260%260',
              u'lgc': u'tb1339366017',
              u'_nk_': u'tb1339366017',
              u'_l_g_': u'Ug%3D%3D',
              u'lastalitrackid': u'www.taobao.com',
              u'_tb_token_': u'yfdC6UjYVPMgSU7',
              u'swfstore': u'148859',
              u'thw': u'cn',
              u'l': u'AhISzcXIMWADqMStIGK409O3QtP0Ixa9',
              u'alitrackid': u'www.taobao.com',
              u'mt': u'ci=8_1',
              u'unb': u'1635013639',
              u't': u'b46cc7fe209a5d3e1157dd832d7a8873',
              u'v': u'0',
              u'x': u'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0',
              u'sg': u'798'}

    # 返回查询内容
    cont = requests.get(url=ip, headers=header, cookies=cookie).content
    # if len(cont) == 0:
    # print cont,


    # 匹配价格
    c = re.findall('"view_price":"(.*?)"', cont, re.S)
    if len(c) == 0:
        print u'快点暂停我……'
    # 匹配销量
    d = re.findall('"view_sales":"(.*?)收货"', cont, re.S)
    # 连接本机数据库
    conn = pymongo.MongoClient('localhost', 27017)
    # 进入指定名称的数据库
    db = conn.book
    # 获取数据库里的 names 集合
    names = db.names
    u = dict(bookname=name, price=c, sales=d)
    # 将数据插入到 users 集合
    db.names.insert(u)
    print i,
    time.sleep(random.randint(15,20))
    i += 1
