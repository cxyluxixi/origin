import requests
import json
import random
import time 

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
params = {
    'first': 'false',
    'pn': '2',
    'kd': '人工智能',
}


#headers注意去掉content-lengths
headers='''
POST /jobs/positionAjax.json?needAddtionalResult=false HTTP/1.1
Host: www.lagou.com
Connection: keep-alive
Origin: https://www.lagou.com
X-Anit-Forge-Code: 0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
X-Anit-Forge-Token: None
DNT: 1
Referer: https://www.lagou.com/jobs/list_%E7%BC%96%E7%A8%8B%E8%80%81%E5%B8%88?labelWords=&fromSearch=true&suginput=
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: user_trace_token=20181221092055-13da0025-b661-4351-85c8-c342b16b8134; LGUID=20181221092056-aa69a2fc-04be-11e9-9d9a-5254005c3644; _ga=GA1.2.2046896704.1545355256; JSESSIONID=ABAAABAABEEAAJABC78F53CA9FFDBAA099C38C3199CD776; X_MIDDLE_TOKEN=38401508e22d17047f2f1553ca56aa27; index_location_city=%E5%85%A8%E5%9B%BD; PRE_UTM=; _gid=GA1.2.1887915762.1547207306; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22167ce59e1267e3-036199692182a7-35677607-1296000-167ce59e127e77%22%2C%22%24device_id%22%3A%22167ce59e1267e3-036199692182a7-35677607-1296000-167ce59e127e77%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LGSID=20190111195431-a7f80d9b-1597-11e9-9bfc-525400f775ce; PRE_HOST=cn.bing.com; PRE_SITE=https%3A%2F%2Fcn.bing.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; SEARCH_ID=850333a851444b579311ff4ea07ced7c; _gat=1; LGRID=20190111200039-83198558-1598-11e9-9bff-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1546692392,1546698319,1547207672,1547208039; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547208039

'''
def str2obj(s, s1=';', s2='='):
    li = s.split(s1)
    res = {}
    for kv in li:
        li2 = kv.split(s2)
        if len(li2) > 1:
            res[li2[0]] = li2[1]
    return res


from bs4 import BeautifulSoup

# 获取每个职位二级页面的详细信息
def readJobDetails(pid):
    html = requests.get('https://www.lagou.com/jobs/'+str(pid)+'.html', headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    res=soup.find('dd','job_bt').text.replace('\n','')
    return res

headers = str2obj(headers, '\n', ': ')

import requests
import pandas as pd

for n in range(1, 10):
    params['pn'] = n
    
    # 开始访问网站，并保存为json数据——data
    jsonData = requests.get(url, params=params, headers=headers)
    data = json.loads(jsonData.text)

    # 在搜索返回中找到职位信息，
    jobs = data['content']['positionResult']['result']
    print(json.dumps(jobs[0], indent=2, ensure_ascii=False))
    
    # 找到职位详细信息的链接positionId
    for job in jobs:
        pid = str(job['positionId'])
        fname='/Users/luxixi/Downloads/jobs/'+pid+'.json'
        job['details'] = readJobDetails(job['positionId'])
        # 保存到文件
        with open(fname, 'w') as f:
            f.write(json.dumps(job))
            f.close()
        print('>Got job:', pid)
        time.sleep(random.randint(1,4))
    time.sleep(random.randint(1,4))
print('>Finished!')

