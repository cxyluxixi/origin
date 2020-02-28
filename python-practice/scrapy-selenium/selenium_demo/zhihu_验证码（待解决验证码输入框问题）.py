import selenium
import requests
from selenium import webdriver
import time
from PIL import Image
import base64
import io
from selenium.webdriver.common.keys import Keys

headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
def get_image_captcha(driver):
    # url = driver.find_element_by_css_selector('#root > div > main > div > div > div > div.SignContainer-inner > div.Login-content > form > div.Captcha.SignFlow-captchaContainer > div > span > div > img').get_attribute("src")
    # url = base64.b64decode(url)
    # im = Image.open('capt.png')
    # with open('captcha.jpg','wb') as f:
    #     f.write(url)
    # image = Image.open('captcha.jpg')
    # image.show()
    # driver.save_screenshot('capt.png')
    # im = Image.open('capt.png')
    # im.show()
    captchaNum = input('输入验证码')
    # im.close()
    return captchaNum

def get_captcha(driver):
    captn = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/div/div[1]/input')
    return captn


def get_password(driver):
    passw = driver.find_element_by_xpath('//input[@name="password"]')
    return passw


def get_username(driver):
    usern = driver.find_element_by_xpath('//input[@name="username"]')
    return usern


if __name__ == "__main__":
    # 打开一个浏览器
    driver = webdriver.Chrome()

    # driver打开网页
    driver.get('http://www.zhihu.com/')

    # 获取元素
    switchToLogin = driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span')
    # 点击它
    switchToLogin.click()

    user1 = get_username(driver)
    pass1 = get_password(driver)
    user1.clear()
    user1.send_keys('632137620@qq.com')
    pass1.clear()
    pass1.send_keys('hsh199131')


    # # 获取元素
    # usern = driver.find_element_by_xpath('//input[@name="username"]')
    # # 清空元素里的文本
    # usern.clear()
    # # 向元素中input信息，模拟键盘输入
    # usern.send_keys('632137620@qq.com') 

    # passw = driver.find_element_by_xpath('//input[@name="password"]')
    # passw.clear()
    # passw.send_keys('hsh199131')
    loginB = driver.find_element_by_xpath("//button[@class='Button SignFlow-submitButton Button--primary Button--blue']")
    loginB.click()
    try:
        if driver.find_elements_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[3]/div/div/div[2]'):
            
            cap1 = get_captcha(driver)
            capn = get_image_captcha(driver)
            # 输入验证码后，input标签中的placeholder属性值，无法取消，
            # 使用click(),输入tab键，使用clear(),都无法消除。
            cap1.send_keys(Keys.ENTER)
            # cap1.clear()
            
            cap1.send_keys(capn)
        
    except:
        pass


    
    loginB = driver.find_element_by_xpath("//button[@class='Button SignFlow-submitButton Button--primary Button--blue']")
    loginB.click()
    time.sleep(3)
    print(driver.title)
    

    # 关闭浏览器
    driver.close()