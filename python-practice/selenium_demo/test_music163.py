from selenium import webdriver
import requests
import time
import json

mm = {}
base_url = 'https://music.163.com/'
url = 'https://music.163.com/#/album?id=72375004'
driver = webdriver.Chrome()
driver.get(url)
driver.switch_to_frame('contentFrame')
musics = driver.find_elements_by_xpath('//span[@class="txt"]/a')
for item in musics:
    music_url = item.get_attribute('href')
    # music_id = music[9:]
    # music_url = base_url + music
    text_comments = []
    driver.get(music_url)
    driver.switch_to_frame('contentFrame')
    time.sleep(1)
    comments = driver.find_elements_by_xpath('//div[@class="itm"]/div[2]/div[1]/div')
    for i in range(1,len(comments)+1):
        text_comment = driver.find_element_by_xpath('//div[@class="itm"][{}]/div[2]/div[1]/div'.format(i)).text
        # print(text_comment)
        text_comments.append(text_comment)
        # print(driver.title)
        music = driver.find_element_by_xpath('//div[@class="tit"]/em[@class="f-ff2"]').text 
        artist = driver.find_element_by_xpath('//div[@class="cnt"]/p[1]/span/a').text 
        album = driver.find_element_by_xpath('//div[@class="cnt"]/p[2]/a').text 
        print(music,artist,album)
        mm['id'] = str(music_url)
        mm['music'] = str(music)
        mm['album'] = str(album)
        mm['artist'] = str(artist)
    mm['comments'] = str(text_comments)

print(mm)
with open('music163Comments.json','w+') as f :
        # f.write(mm['id'])
    line = json.dumps(dict(mm),ensure_ascii=False)
    f.write(line)
driver.close()



    
  
    