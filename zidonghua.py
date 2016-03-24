# coding=utf-8
import time
import random
import xlrd
from splinter import Browser


def splinter(url):
    browser = Browser(driver_name='chrome')
    data = xlrd.open_workbook('/home/lx/PycharmProjects/zhanghu.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    i = 500
    n = 0
    while i < nrows:

        # 循环取账号
        c = table.row_values(i)

        a = c[0]
        b = c[1]

        # login

        browser.visit(url)
        # wait web element loading
        time.sleep(1)

        # fill in account and password
        browser.find_by_id('ap_email').fill(a)
        browser.find_by_id('ap_password').fill(b)

        time.sleep(1)

        # click the button of login
        browser.find_by_id('signInSubmit').click()

        if browser.find_by_id('auth-captcha-guess'):
            print i,
            print u'爷，要输入验证码啦！'
            break



        elif browser.find_by_id('auth-error-message-box'):

            print u'这个账号或密码有误' + i,

            i += 1
            n += 1
            continue
        else:

            # 领取优惠券
            # browser.visit('http://www.amazon.cn/gp/collect-coupon/handler/redeem-coupon-detailpage.html?ref_=pu_redeem_coupon&encryptedPromotionId=AOPQVZZY0SW9J')
            # time.sleep(1)
            # browser.back()
            # time.sleep(1)
            # browser.visit('http://www.amazon.cn/gp/collect-coupon/handler/redeem-coupon-detailpage.html?ref_=pu_redeem_coupon&encryptedPromotionId=A3GU8GKVJFOHDC')
            # time.sleep(1)
            # browser.back()
            # 点击 图书
            browser.find_by_xpath('//*[@id="nav-flyout-shopAll"]/div[2]/span[4]/a').click()

            # 点击 领取活动
            browser.find_by_xpath('//*[@id="bxw-content-grid_ns_1GB52GD7KEHHF4W7G54H_769__cg_5368"]/div/div[2]/div[1]/div/div/a/div/img').click()

            browser.find_by_xpath('//*[@id="a-autoid-0-announce"]').click()

            # 点击 200减100 优惠
            # browser.find_by_id('a-autoid-7').click()

            # 点击 100减20 优惠
            # browser.find_by_id('A138AQQQZXTTHH').click()




            print i,

            i += 1
            n += 1
            print n,
            # if n > 7:
            #     n = 0
            #     # 退出账号
            #     time.sleep(2)
            #     browser.find_by_id('nav-link-yourAccount').mouse_over()
            #     time.sleep(2)
            #     browser.find_by_id('nav-item-signout').click()
            #     print u'请等待15分钟'
            #     time.sleep(900)

            time.sleep(random.randint(15, 20))
            # close the window of brower
            # browser.quit()


if __name__ == '__main__':
    websize3 = 'https://www.amazon.cn/ap/signin?_encoding=UTF8&openid.assoc_handle=cnflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.cn%2F%3Ftag%3Dbaidhydrcnnv-23%26hvadid%3D{creative}%26ref%3Dnav_ya_signin'
    splinter(websize3)
