import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
from PIL import Image


def get_captcha(driver):
    captn = driver.find_element_by_xpath('//*[@id="vcode"]')
    return captn


def get_password(driver):
    passw = driver.find_element_by_xpath('//*[@id="password"]')
    return passw


def get_username(driver):
    usern = driver.find_element_by_xpath('//*[@id="loginname"]')
    return usern


def get_image_captcha(driver):
    # driver.save_screenshot('yzm.png')
    # im = Image.open('yzm.png')
    # im.show()
    captchaNum = input('输入验证码')
    # im.close()
    return captchaNum




# 鼠标拖拽，保持，各种鼠标键盘动作，

# def ActionChainss(driver):
#     elementA = driver.find_element_by_xpath('xxxx')
#     elementB = driver.find_element_by_xpath('xxxx')
#     action = ActionChains(driver)
#     action.drag_and_drop(elementA,elementB).perform()
#     action.key_down('s')
#     action.move_to_element(elementA)
#     action.pause('seconds')
#     action.release(on_element='aaa')





# 连续动作链，比如scroll

# def scroll_page(driver):
#     driver.execute_script('js code')
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#     driver.execute_script('alert("xxxx")')


if  __name__ == "__main__" :
    driver = webdriver.Chrome()
    driver.get('https://xiaoyuan.zhaopin.com/LoginManager/Login')
    
    # 获取元素
    # switchToLogin = driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span')
    # # 点击它
    # switchToLogin.click()

    user1 = get_username(driver)
    pass1 = get_password(driver)
    cap1 = get_captcha(driver)
    user1.clear()
    user1.send_keys('13871134209')
    pass1.clear()
    pass1.send_keys('hsh199131')
    capn = get_image_captcha(driver)
    # cap1.clear()
    cap1.send_keys(capn)

    loginB = driver.find_element_by_xpath('//*[@id="login"]')
    loginB.click()
    # loginB.submit()
    
    

    # 窗口切换
    # driver.switch_to_frame('FrameName')
    # driver.switch_to_window(driver.window_handles['index123...'])



    # 显式等待
    wait = WebDriverWait(driver, 3)
    # wait.until(EC.presence_of_element_located(cap1))



    print(driver.title)
    # driver.save_screenshot('page.png')
    

    # 滚动条加载
    scroll_js = 'var q = document.documentElement.scrollTop=100'
    driver.execute_script(scroll_js)
    # 关闭浏览器
    driver.close()
