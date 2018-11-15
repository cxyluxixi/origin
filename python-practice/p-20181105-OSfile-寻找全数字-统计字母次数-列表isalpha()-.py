# 函数返回值，语法糖
def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco
 
@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'


# 文件处理，创建，读取，写入，保存关闭，
import os
f = open('thisIsASong.txt','a+') #a表示追加写，r只读，w清空原文件覆盖写，x创建写（如果文件已存在，则报错）
lst1 = f.readlines() 
lst1.insert(0,'1--')
lst1.insert(1,'2--')
lst1.append('last')
lst1 = ''.join(lst1)
print(lst1)
f.seek(0)
f.write(lst1)
f.close()

# 列表操作
def clean_list(lst):
    cleaned_list = []
    for item in lst:
        for i in item:
            if i.isalpha() != True:
                item = item.replace(i,'')
        cleaned_list.append(item)
    return cleaned_list

    

if __name__ == "__main__":
    coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
    cleaned_list = clean_list(coffee_list)
    for k,v in zip(range(1,len(cleaned_list)+1),cleaned_list):
        print(k,v)


# 统计出现的字母的次数，
def countchar(string):
    num = [0]*26 #列表，产生26个元素‘0’
    string = string.lower()
    for i in range(0,len(string)):
        if string[i].isalpha():
            letter = ord(string[i]) - ord('a')
            num[letter] += 1
    return num

if __name__ == "__main__":
    string = input("请输入要统计字母次数的文本")
    print(countchar(string))


# 寻找输入数字中的全数字
def pandigital(nums):
    
    lxx = False 
    for num in nums:
        num = str(num)
        goodNumber = []
        neededNumber = []
        for i in range(1,len(num)+1):
            neededNumber.append(str(i))
        for m in neededNumber:
            if m in num:
                goodNumber.append(m)
        if len(goodNumber) == len(neededNumber):
            print(num)
            lxx = True
    if lxx == False :
        print('not found')

if __name__ == '__main__':
   pandigital(eval(input()))



#统计词频,判断word的词频并输出（可能是0次）
def countfeq(s):
    s = s.replace('.',' ')
    s = s.replace(',',' ')
    wordKeys = s.split(' ')
    countNum ={}
    for i in wordKeys:
        if i in countNum:
            countNum[i] +=1
        else:
            countNum[i] = 1
            
    return countNum
    
if __name__ == "__main__":
    s = "Not clumsy person in this world, only lazy people, only people can not hold out until the last."
    s_dict = countfeq(s.lower())
    word = input()
    if word in s_dict.keys():
        print(s_dict[word])
    else:
        print('0')

