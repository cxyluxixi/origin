import os
import re 
filePath = '/Users/luxixi/Downloads/huimeiyijian/'
alreadyInresult = []
with open('/Users/luxixi/Downloads/huimeiyijian/Result-ShengWuGu.txt','a') as sheng:
    fileList = os.listdir(filePath)
    for item in fileList:
        if item in alreadyInresult:
            print(item)
            continue
        else:
            alreadyInresult.append(item)
            if re.search(r'[0-9]{7}',item):
                eachFilePath = filePath + item
                for line in open(eachFilePath):
                    # assert print(line)
                    sheng.writelines(line)
                    sheng.write('\n')
                    print(item,'已写入')
            else:
                print('文件名不对，跳过')
                continue