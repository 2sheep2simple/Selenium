# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 0:14
# @Author  : 2simple
# @Site    : 
# @File    : LocalTest.py
# @Software: PyCharm
from selenium import webdriver


def findInputBox():
    global nameInput
    nameInput = browser.find_element_by_name('name')
    global cardidInput
    cardidInput = browser.find_element_by_name('cardid')
    global ageInput
    ageInput = browser.find_element_by_name('age')
    global emailInput
    emailInput = browser.find_element_by_name('email')
    global addressInput
    addressInput = browser.find_element_by_name('address')
    global button
    button = browser.find_element_by_name('submitButton')  # 获取按钮对象


def test(url, name, cardid, age, address, email, exceptResult):
    try:
        browser.get(url)  # 请求待测试页面
        findInputBox()
        nameInput.send_keys(name)
        cardidInput.send_keys(cardid)
        ageInput.send_keys(age)
        emailInput.send_keys(email)
        addressInput.send_keys(address)
        button.click()
        alert = browser.switch_to.alert
        global realResult
        realResult = alert.text  # 获取通知框文本
        verificate(realResult, exceptResult)  # 添加验证点
        alert.accept()
        browser.quit()  # 关闭当前窗口和Session
    except:
        print("请求失败.....")


def verificate(realResult, exceptResult):
    if realResult == exceptResult:  # 验证期望值和真实值
        print("warns 0 ,error 0!，恭喜！")
    else:
        print("except:"+realResult, "but real is"+exceptResult+"...程序有错！")


def request(name, cardid, age, address, email, result):
    global browser
    url = "http://localhost:8080/MessageInput.jsp"
    browser = webdriver.Chrome(r"E:\chromedriver.exe")  # 实例化浏览器对象
    test(url, name, cardid, age, address, email, result)


if __name__ == "__main__":
    tests = [  # 数据资源池
        ["苏文进", "430503199110014010",  "67", "", "", "录入失败"],
        ["", "430503199610064010",  "67", "", "", "录入成功"],
        ["苏文进", "430503199610019010",  "67", "", "", "录入失败"],
        ["苏文进", "430593199610014010",  "67", "", "", "录入成功"],
        ["苏文进", "430563199610014010",  "", "", "", "录入成功"],
        ["苏文进", "430503190610014010",  "", "", "", "录入成功"],
        ["苏文进", "430503199010014010",  "67", "", "", "录入失败"]]
    for row in range(len(tests)):
        request(tests[row][0], tests[row][1], tests[row][2], tests[row][3], tests[row][4], tests[row][5])












