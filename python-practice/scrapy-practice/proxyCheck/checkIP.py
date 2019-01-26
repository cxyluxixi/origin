import requests

from multiprocessing.dummy import Pool as ThreadPool

dir_path = '/Users/luxixi/luxixi2018/githubpractice/python-practice/scrapy-practice/proxyCheck/'
useful_ip = []

# 多线程，池
pool= ThreadPool(20)


def test_ip(proxy):
    # 测试ip有效性，返回测试结果，有用就写入useful_ip.txt,没用就pass

    global useful_ip

    proxies = {'http':proxy}
    print('start test:{}'.format(proxies))

    try:
        r = requests.get('http://www.baidu.com',proxies=proxies,timeout = 3)
        r.raise_for_status()
        print('sucess, keep it ')
        useful_ip.append(proxies['http'])
    except:
        print('failure, delete it ')


def out_file(useful_ip=[]):
    # 将有用的ip写入文件

    with open(dir_path+'useful_ip.txt','a+') as f :
        for ip in useful_ip:
            f.write(ip+'\n')

        print('useful_ip 写入完毕')

    
def main(filename='kdl——proxy.txt'):
    # 主程序，循环处理原始ip文件中的每个ip

    with open(dir_path+filename,'r') as f:
        lines = f.readlines()
        proxylist = list(map(lambda x: x.strip(),[x for x in lines]))

        # 多线程布置
        pool.map(test_ip,proxylist)

        # 写入文件
        out_file(useful_ip)


if __name__ == "__main__":
    main('kdl_proxy.txt')