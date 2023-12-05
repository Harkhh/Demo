#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: hark
# @Time: 2023/12/4 21:04
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = 'https://www.feishu.cn'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get(url)

# 1、通过读取本地cookie信绕过短信验证登录
with open("feishu_cookies.txt", "r") as f:
    cookies_str = f.readline()
    cookies_dict = json.loads(cookies_str)

driver.delete_all_cookies()  # 清除当前网址的所有cookies
for cookie in cookies_dict:  # 循环读取cookies
    for k in cookie.keys():
        if k == "expiry":
            cookie[k] = int(cookie[k])
        driver.add_cookie(cookie)
time.sleep(2)
driver.refresh()
time.sleep(5)


# 2、点击右上角进入消息界面
def get_text():
    driver.find_element(By.CLASS_NAME, 'headerExtra_productList').click()
    time.sleep(5)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div[1]/ul/li[1]/div").click()
    time.sleep(5)


# 3、切换窗口，进入通讯录界面
def get_address_book():
    windows = driver.window_handles
    driver.switch_to.window((windows[-1]))
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "#app > section > div > section > section > section:nth-child(5)").click()
    time.sleep(5)


# 4、搜索联系人，并进入聊天界面
def get_contact():
    driver.find_element(By.CSS_SELECTOR, "#root-contacts > div > div.contactPageNav > div.contactPageNav__quick-jump-box.lark-draggable > div > div > div").click()
    time.sleep(5)
    driver.find_element(By.CLASS_NAME, "quickJump_input").send_keys("hark")  # 指定测试账号
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div').click()   # 失败率较高，增加异常重跑 / 切换其它定位方式
    time.sleep(10)

    # 输入聊天内容回车发送
    driver.find_element(By.XPATH, '//*[@id="root-messenger-nav-application"]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/pre').send_keys("Hello", Keys.ENTER)
    time.sleep(5)

    # 退出
    # driver.quit()


#  5、切换账号(未完善)
# 调用get_Cookies，保存两份cookies文件，切换账号时判断不同账号登录状态
def get_switch_user():
    driver.find_element(By.CSS_SELECTOR, "#app > section > div > section > div.appNavbar_bottomList > section > "
                                         "div.user-auth-list_itemBox.user-auth-list_joinTeamButton.js-btn-add-user"
                                         "-auth > div > svg").click()
    time.sleep(5)
    if driver.find_element(By.CLASS_NAME, "base-title-title"):
        driver.find_element(By.CSS_SELECTOR, "#__passport_join_team_container > div > div > div > div > div > div.team-discovery-content > div.team-discovery-login-other > button").click()
        time.sleep(5)


# 未完善
# pytest框架
# 业务数据分离
if __name__ == "__main__":
    get_text()
    get_address_book()
    get_contact()
    get_switch_user()



