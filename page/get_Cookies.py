#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: hark
# @Time: 2023/12/4 21:02

from selenium import webdriver
import time
import json


def browser_initial():
    """
    浏览器初始化
    :return:
    """

    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://login.feishu.cn/accounts/page/login?app_id=11&redirect_uri=https%3A%2F%2Fwww.feishu.cn%2F&template_id=7159153320657698818'
    return url, driver


# 获取扫码后的cookies保存到本地
def get_cookies(url, driver):
    """
    获取Cookies保存到本地
    :param url:
    :param driver:
    :return:
    """
    driver.get(url)
    time.sleep(20)
    dict_cookies = driver.get_cookies()
    json_cookies = json.dumps(dict_cookies)

    with open('feishu_cookies.txt', 'w') as f:
        f.write(json_cookies)
    print("cookies保存成功")

    driver.quit()  # 退出


if __name__ == "__main__":
    turl = browser_initial()
    get_cookies(turl[0], turl[1])
