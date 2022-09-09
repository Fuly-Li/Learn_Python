from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",  # 被测手机是安卓
    "platformVersion": "12",  # 手机安卓版本
    "deviceName": "****",  # 设备名，安卓手机可以随意填写
    "appPackage": "com.chatfun.and",  # 启动APP Package名称
    "appActivity": "com.voice.chat.wowed.android.login.view.activity.SplashActivity",  # 启动Activity名称
    # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    # 'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'

}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print("连接成功！")

driver.implicitly_wait(10)
driver.find_element(By.ID, 'com.chatfun.and:id/btn2').click()
sleep(3)

driver.find_element(By.ID, 'com.chatfun.and:id/btn3').click()
sleep(3)

driver.find_element(By.ID, 'com.chatfun.and:id/iv_tab_party').click()
sleep(3)

driver.find_element(By.ID, 'com.chatfun.and:id/iv_tab_chat').click()
sleep(3)

driver.find_element(By.ID, 'com.chatfun.and:id/iv_tab_mine').click()
sleep(3)

driver.find_element(By.ID, 'com.chatfun.and:id/civ_avatar').click()
sleep(3)

print("执行完毕！")
driver.quit()
