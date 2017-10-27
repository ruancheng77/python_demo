#!/bin/env python3
#-*-encoding:utf-8-*-

'''
使用 selenium 模拟登陆，获取 QQ 邮箱中的用户昵称。
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://mail.qq.com/cgi-bin/loginpage"  # 定义要爬取网页的 url

try:
    # 获取浏览器驱动，下面是获取火狐的浏览器驱动
    # 如果已经在系统环境变量中存在 geckodriver，则不需要配置 executable_path
    driver = webdriver.Firefox(executable_path="D:/geckodriver/geckodriver.exe")
    driver.get(url)                             # 爬取指定 url 的页面（经过 js 渲染）
    driver.implicitly_wait(30)                  # 设置一个粘滞超时, 以隐式等待找到某个元素或要完成的命令。此方法只需要每次会话调用一次。
    print(driver.title)                         # 输出页面 title
    # 定位 iframe (iframe 比较特殊，无法通过 find_xxx 方法获取)
    driver.switch_to_frame("login_frame")
    login_method = 1 # 0: 快速登陆，1：用户名密码登录
    username = "410093793"
    password = "xxxxxxxxx"
    if login_method == 0:
        # 获取快速登陆标签
        ele_qlogin_label = driver.find_element_by_id("switcher_qlogin")
        # 点击快速登陆标签，显示快速登陆页
        ele_qlogin_label.click()
        # 获取快速登陆图标元素
        ele_qlogin = driver.find_element_by_id("img_out_%s"%username)
        # 点击快速登陆图标元素
        ele_qlogin.click()
    elif login_method == 1:
        # 获取账号密码登陆标签
        ele_plogin = driver.find_element_by_id("switcher_plogin")
        # 点击账号密码标签，显示账号密码登陆页
        ele_plogin.click()
        # 获取用户名输入框元素
        ele_user = driver.find_element_by_name("u")
        # 模拟键盘输入，在用户名输入框中输入用户名
        ele_user.send_keys(username)
        # 获取密码输入框元素
        ele_pwd = driver.find_element_by_name("p")
        # 模拟键盘输入，在密码输入框中输入密码
        ele_pwd.send_keys(password)

        ele_pwd.send_keys(Keys.RETURN)
        # 点击登陆按钮
        driver.find_element_by_id("login_button").click()
    # 在页面重定向之后，需要根据重定向 url，重新获取页面
    driver.get(driver.current_url)
    print(driver.title)
    # 获取昵称
    name = driver.find_element_by_id("useralias").text
    print(name)
except Exception as e:
    print(e)
finally:
    driver.quit()
