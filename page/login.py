#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: hark
# @Time: 2023/12/4 19:55
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 初始化浏览器
def browser_first():

    url = "https://www.feishu.cn"
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    driver.get(url)
    return driver


# 登录飞书账号
def login_user(driver, **kwargs):

    # 判断是否出现弹窗，有则关闭
    if driver.find_element(By.CSS_SELECTOR, "body > div.hc_Popup > div.hc_Popup-content"):
        close_button = driver.find_element(By.CSS_SELECTOR, "body > div.hc_Popup > div.hc_Popup-content > div > div > div "
                                                            "> svg")
        close_button.click()
        time.sleep(5)

        # 点击登录按钮
        login_button = driver.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div > div > div > div > '
                                                            'a:nth-child(9)')
        login_button.click()
        time.sleep(5)

        # 点击输入账号
        user_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.web-login-left > div.web-main-content > '
                                                           'div.login-content-container > div.login-qr-switch-box > div > '
                                                           'div > div.switch-login-mode-container > div > span > svg')
        user_button.click()
        time.sleep(5)

        # 输入账号
        input_user = driver.find_element(By.NAME, 'mobile_input')
        input_user.send_keys("139***")  # 填入测试手机账号
        time.sleep(5)

        # 勾选同意
        checkbox_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.web-login-left > div.web-main-content > '
                                                               'div.login-content-container > div.new-account-login-box > '
                                                               'div > '
                                                               'div.new-account-login-module.new-account-module-nopadding '
                                                               '> div > '
                                                               'div.ud__modal__body.ud__scrollArea.ud__scrollArea-hide'
                                                               '-bar.ud__scrollArea-y > div > '
                                                               'div.terms-and-policy-container.enter-credential__terms > '
                                                               'label > span.ud__checkbox > input')
        checkbox_button.click()
        time.sleep(5)

        # 点击下一步按钮
        next_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.web-login-left > div.web-main-content > '
                                                           'div.login-content-container > div.new-account-login-box > div '
                                                           '> div.new-account-login-module.new-account-module-nopadding > '
                                                           'div > '
                                                           'div.ud__modal__body.ud__scrollArea.ud__scrollArea-hide-bar'
                                                           '.ud__scrollArea-y > div > button')
        next_button.click()
        time.sleep(5)

        # 输入密码
        password_button = driver.find_element(By.NAME, 'password_input')
        password_button.send_keys("123")  # 输入账号密码
        time.sleep(10)

        # 点击下一步
        pass_next_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.web-login-left > '
                                                                'div.web-main-content > div.login-content-container > '
                                                                'div > div > div:nth-child(3) > div > '
                                                                'div.ud__modal__footer > div > button')
        pass_next_button.click()
        time.sleep(10)

        # 需要输入手机验证——通过PC读取手机端短信进行验证(未实现)


if __name__ == "__main__":

    browser = browser_first()
    time.sleep(10)
    login_user(browser)
