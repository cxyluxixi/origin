from selenium import webdriver
import requests
import pandas as pd 
import time
import json
import re 


data_list = []
base_url = 'http://www.qgsydw.com/'
pages = [2,3,4]
writer = pd.ExcelWriter('job.xlsx')
for page in pages:
    url = 'http://www.qgsydw.com/qgsydw/recruit/insrecruit/index_{page}.html'.format(page=page)
    driver = webdriver.Chrome()
    driver.get(url)
    job_ad_list  = driver.find_elements_by_xpath("html/body/div[4]/div[2]/div[2]/ul/li")
    data={}
    for i in range(1,len(job_ad_list)+1):
        data['日期'] = driver.find_element_by_xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/span'.format(i)).text
        data['标题'] = driver.find_element_by_xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/a'.format(i)).text
        # print(data['标题'])
        data['省份'] = re.findall(r'\[\w*\]',str(data['标题']))[0]
        # print(data['省份'])
        data['url_address'] = driver.find_element_by_xpath('html/body/div[4]/div[2]/div[2]/ul/li[{}]/a'.format(i)).get_attribute('href')
        with open('job.json','a+') as f :
        # f.write(mm['id'])
            line = json.dumps(dict(data),ensure_ascii=False) +','+'\n'
            f.write(line)
        f.close()
driver.close()
