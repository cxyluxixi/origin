#! /usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import logging
import httplib
import urllib
import pickle
import re


array = [u'乐高', u'vipkid']
current_url = ''

def debug2(str):
    logging.error(": " + str)
    return

def get_data(page):
    current_url = driver.current_url
    while True:
        print "inside while true"
        for i in [1,2,3,4,5,6,7,8,9]:
            try:
                driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
            except:
                print 'body error'
                pass
        try:
            weibo = driver.find_element_by_id("pl_weibo_direct")
            if page == 1:
                weibo1 = weibo.find_element_by_xpath('./div/div[3]/div')  #实时微博
            else:
                weibo1 = weibo.find_element_by_xpath('./div/div/div')  #实时微博

            oDivs = weibo1.find_elements_by_class_name('WB_cardwrap')
            
            for oDiv in oDivs:
                try:
                    odiv = oDiv.find_element_by_xpath("./div[@action-type='feed_list_item']")
                    # print odiv.get_attribute('mid')
                    oTargent = odiv.find_element_by_xpath('./div[1]/dl[1]/div[1]')
                    oface = oTargent.find_element_by_class_name('face')
                    ocontent = oTargent.find_element_by_class_name('content')

                    oa = oface.find_element_by_xpath('./a')
                    oimg = oface.find_element_by_xpath('./a/img')

                    ofeedContent = ocontent.find_element_by_class_name('feed_content')
                    ocomment = ofeedContent.find_element_by_class_name('comment_txt')

                    nickname = oa.get_attribute('title')
                    href = oa.get_attribute('href')
                    osrc = oimg.get_attribute('src')
                    usercard = oimg.get_attribute('usercard')
                    userid1 = usercard.split('&')[0]
                    userid = userid1.split('id=')[1]

                    comment = ocomment.text
                    x = u"乐高蝙蝠侠"
                    if x in comment:
                        print u'===========该条不符合要求,丢弃==========='
                        continue
                    
                    print nickname
                    print href
                    print osrc
                    print userid
                    print comment
                    print '---------------------------------'

                    try:
                        link = href.encode('utf8')
                        nickname = nickname.encode('utf8')
                        src = osrc.encode('utf8')
                        userid = userid.encode('utf8')

                        dic = {'link':link, 'nickname':nickname, 'src':src, 'userid':userid}
                        res = urllib.urlencode(dic)
                        print res
                        import urllib2
                        u = "http://127.0.0.1:8001/organization/create_weibo/?" + res
                        print 'opening'
                        urllib2.urlopen(u)
                    except:
                        print u'传数据异常'
                        pass
            
                except:
                    continue
        except:
            pass
        
        print "I want to go to next page ---------"
        time.sleep(5)
        if page < 50:
            page = page + 1
            print '-----------' + str(page)
            try:
                url = current_url + '&page=' + str(page)
                driver.get(url)
            except TimeoutException:
                print "excption on get url error"
                driver.execute_script('window.stop()')
            except WebDriverException:
                url = current_url + '&page=' + str(page)
                try:
                    driver.get(url)
                except:
                    pass
                    
            time.sleep(10)
        else:
            break

        print "sleeping ********"
        time.sleep(5)

def search_keys():
    # ainput = driver.find_element_by_class_name('searchInp_form')
    # ainput.send_keys(u'乐高')
    # a = driver.find_element_by_class_name('searchBtn')
    # a.click()
    # a.send_keys(Keys.RETURN)

    for key in array:
        print '==================================' + key
        a = driver.find_element_by_class_name('card-wrap')
        cinput = a.find_element_by_xpath('./input')
        submit = a.find_element_by_xpath('./a')
        cinput.send_keys(key)
        # submit.click();
        submit.send_keys(Keys.RETURN)

        print 'waiting........'
        time.sleep(15)
        # driver.execute_script('window.stop()')

        print '111'
        time.sleep(5)
        print "222"
        print "current url=" + driver.current_url
        current_url = driver.current_url

        get_data(1)


def login_weibo(url):
    driver.set_page_load_timeout(30)
    driver.maximize_window()  #浏览器最大化
    
    try:
        driver.get(url)
    except TimeoutException:
        print "excption on get url " + url
        driver.execute_script('window.stop()')
    except WebDriverException:
        driver.get(url)

    print "after first"
    #time.sleep(3)
    print "after first 0"
    print "after first 1"
    #print page_title

    print "after first 2"
    
    time.sleep(30)

    login_form = driver.find_element_by_id('pl_login_form')
    form = login_form.find_element_by_xpath('./*[1]/*[3]')

    username = form.find_element_by_class_name('username')
    user_input = username.find_element_by_xpath('./*[1]/input')
    user_input.click()
    user_input.send_keys('****')

    print 'username = ' + u'**@qq.com'

    password = form.find_element_by_class_name('password')
    pass_input = password.find_element_by_xpath('./*[1]/input')
    pass_label = password.find_element_by_xpath('./*[1]/span')
    password.click()
    pass_input.send_keys('****')

    print 'password = ' + u'**'

    

    submit = form.find_element_by_class_name('login_btn')
    submit_btn = submit.find_element_by_xpath('./a')
    # submit_btn.click();
    submit_btn.send_keys(Keys.RETURN)

    print 'logining......'

    time.sleep(15)
    # driver.execute_script('window.stop()')
    driver.back()
    time.sleep(15)
    print 'login success.'

    search_keys()

def run_for_one(url):

    login_weibo(url);

    time.sleep(10)
    print "**************end"


logfile = 'mac.log'
logging.basicConfig(format='%(asctime)s %(message)s', filename=logfile,
                   level=logging.ERROR)

fp = webdriver.FirefoxProfile()
fp.set_preference("network.image.imageBehavior", 2)

import urllib2
#driver = webdriver.Firefox(firefox_profile=fp)
driver = webdriver.Firefox()
run_for_one("http://weibo.com/")
#run_for_one(sys.argv[1])

driver.quit()
