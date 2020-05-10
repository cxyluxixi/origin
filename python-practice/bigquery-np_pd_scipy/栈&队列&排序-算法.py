# 栈——括号消除
class Stack:
    def __init__(self):
        self.items =[]
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def len(self):
        return len(self.items)

def matches(a,b):
    astr = '([{'
    bstr = ')]}'
    return astr.index(a) == bstr.index(b)

def check(str):
    s = Stack()
    state_result = True
    index = 0
    while index < len(str) and state_result:
        s_i = str[index]
        if s_i in '([{':
            s.push(s_i)
        else:
            if s.isEmpty():
                state_result = False
            else:
                left = s.pop()
                if not matches(left,s_i):
                    state_result = False 
        index+=1  
    if state_result and s.isEmpty():
        return True
    else:
        return False
# print(check(str(input())))



# 栈——字母连连消除    
def disappear(str):
    s = Stack()
    S = Stack()
    state_result = ''
    index = 0
    while index < len(str):
        s_i = str[index]
        if s.isEmpty():
            s.push(s_i)
            index += 1
        else:
            left = s.peek()
            if left != s_i:
                s.push(s_i)
                index +=1
            else:
                s.pop()
                index +=1
    while s.isEmpty()==False:
        S.push(s.pop())
    while S.isEmpty()==False:
        state_result += S.pop()
    return state_result
# print(disappear(str(input())))



# 栈——盘子回收
def plat(uin):
    s = Stack()
    index = 0
    # maxn = '9'
    uin_result = ''
    while index < len(uin):
        u_i = uin[index]
        if s.isEmpty():
            s.push(u_i)
            index +=1
        else:
            left = s.peek()
            if left > u_i :
                s.push(u_i)
                if index == 9 :
                    uin_result += s.pop()
                    uin_result += u_i
                else:
                    index+=1
            else:
                uin_result += s.pop()
    print(uin_result)
    if uin_result =="0123456789":
        return 'Yes'
    else:
        return 'No'
# print(plat(str(input("请输入："))))



#队列——
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def potato(namequeue,deliver_num):
    q = Queue()
    for name in namequeue:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(deliver_num):
            q.enqueue(q.dequeue())
            i+=1
        q.dequeue()

    return q.dequeue()
# print(potato(input(),input()))


#队列——字符的和最小的顺序
def func(S):
    # your code here
    q= Queue()
    s = str(S)
    compare = S
    i = 0
    while i < len(s):
        for m in s:
            q.enqueue(m)
        q.enqueue(q.dequeue())
        state = ''
        while q.size() >= 1:
            state += q.dequeue()
        if state <= compare:
            compare = state
        s = state
        i += 1
    output = compare
    return output
    
S = eval(input())
print(func(S))






#队列——列表数据大小排列
def funcc(ll):
    i = 0                                    #初始为个位排序
    n = 1                                     #最小的位数置为1（包含0）
    max_num = max(ll)                      #得到带排序数组中最大数
    while max_num > 10**n:                   #得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}                          #用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])         #将每个桶置空
        for x in ll:                       #对每一位进行排序
            radix =int((x / (10**i)) % 10)   #得到每位的基数
            bucket[radix].append(x)         #将对应的数组元素加入到相                          #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:         #若桶不为空
                for y in bucket[k]:         #将该桶中每个元素
                    ll[j] = y                       #放回到数组中
                    j += 1
        i += 1
    return  ll

mylist = eval(input())
print(func(mylist))



#链表节点
class Node:
    def __init__(self,initdate):
        self.data = initdate
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
    
class OrderedList:
    def __init__(self,initdate):
        self.head = None
        self.data = initdate
        self.next = None
    
    def add(self,item):
        current = self.head
        previous = None 
        stop = False 
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current 
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
     
    def search(self,item):
        current = self.head 
        found = False 
        stop = False 
        while current != None and not stop:
            if current.getData() == item:
                found = True 
            else:
                if current.getData() >item :
                    stop = True 
                else:
                    current = current .getNext()
        return found 

    def isEmpty(self):
        return self.head == None

#队列——最近请求次数1
def compp(mylist):
    output = []     # 输出列表
    for i in range(len(mylist)):    # 遍历请求时间列表，i为当前指针
        j = 0       # j为比较指针，每次循环归0
        while i > j and mylist[i] == mylist[j]:
            output.append(output[j])
        else:    
            while i >= j and mylist[i] - mylist[j] >10000:  # 当前指针i大于等于比较指针j，并且当前请求时间比比较请求时间大超过10000,
                j += 1      # 则向前移动比较指针
            output.append(i-j+1)    # while结束后，当前指针于比较指针之间的元素就是10000内发生的事件个数
    return output


#队列——最近请求次数1
def comp(ll):
    L = list(range(len(ll)))
    for i in range(len(ll)):
        k = j = i 
        while (j > 0 and ll[i]-ll[j-1]<=10000):
            j -= 1
        while (k<len(ll)-1 and ll[i] == ll[k+1]):
            k+=1
        L[i:k+1] = [k-j+1]*(k-i+1)
        i = k
    return L
# mylist = eval('[0,0,10000,10000,10000,20000]')
# print(comp(mylist))


#数字大小排序——进制基底排序
def RadixSort(ll):
    i = 0                                    #初始为个位排序
    n = 1                                     #最小的位数置为1（包含0）
    max_num = max(ll)                      #得到带排序数组中最大数
    while max_num > 10**n:                   #得到最大数是几位数
        n += 1
    while i < n:
        bucket = {}                          #用字典构建桶
        for x in range(10):
            bucket.setdefault(x, [])         #将每个桶置空
        for x in ll:                       #对每一位进行排序
            radix =int((x / (10**i)) % 10)   #得到每位的基数
            bucket[radix].append(x)         #将对应的数组元素加入到相                          #应位基数的桶中
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:         #若桶不为空
                for y in bucket[k]:         #将该桶中每个元素
                    ll[j] = y                       #放回到数组中
                    j += 1
        i += 1
    return  ll

if __name__ =='__main__':
    S = eval(input('bbb'))
    print(S)
    print(funcc(S))



#递归——进制转换
a = input()
b = input()

nn = a.split()[0]
base = a.split()[1]
b = int(b,int(nn))
check = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def tostr(b,base):
    base = int(base)
    check2 = check[:base]
    if b<base:
        return check2[b]
    else:
        return tostr(b//base,base)+check2[b%base]

print(tostr(b,base))



#递归——汉诺塔四柱
count = 0
def moveDisk(disk,aa,bb):
    pass
    #print('moving disk[{0}] from {1} tp {2}'.format(disk,aa,bb))

def moveP(height,aP,bP,cP,dP):
    global count 
    if height >1:
        moveP(height-2,aP,bP,dP,cP)
        moveDisk(height-1,aP,bP)
        moveDisk(height,aP,dP)
        moveDisk(height-1,bP,dP)
        count += 3
        moveP(height-2,cP,aP,bP,dP)
    elif height == 1:
        count +=1
        moveDisk(height,aP,dP)
def c(count):
    print(count)
height = int(input())
moveP(height,'a','b','c','d')
c(count)





#递归——分形
def carpet(N,l,x,y):
    if N//3 >= 3 :
        draw(N,l,x,y)
        carpet(N//3,l,x,y)
        carpet(N//3,l,x+N//3,y)
        carpet(N//3,l,x+2*N//3,y)
        carpet(N//3,l,x,y+N//3)
        carpet(N//3,l,x+2*N//3,y+N//3)
        carpet(N//3,l,x,y+2*N//3)
        carpet(N//3,l,x+N//3,y+2*N//3)
        carpet(N//3,l,x+2*N//3,y+2*N//3)

    pass

def draw(N, L, x, y):
    for i in range(x + N // 3, x + 2 * N // 3):
        for j in range(y + N // 3, y + 2 * N // 3):
            square[i][j] = ' ' * L

n = int(input())
c = input()
square = [[c for i in range(n)] for i in range(n)] # 生成实心的正方形
l = len(c) # 所给字符串的长度等于挖空中间时所要填充的空格个数
carpet(n, l, 0, 0)
for i in range(n):
    for j in range(n):
        print(square[i][j], end='')
    print()




# 递归——动态规划最优解
tr = {(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w = 20
m ={}
def thief(tr,w):
    if tr == set() or w ==0 :
        m[(tuple(tr),w)] = 0
        print('c')
        return 0
    elif (tuple(tr),w) in m:
        print(m[(tuple(tr),w)])
        return m[(tuple(tr),w)]

    else:
        vmax =0
        for t in tr:
            if t[0] <= w:
                print(vmax,tr,t[0])
                v = thief(tr-{t},w-t[0])+ t[1]
                print('a',vmax,v,tr,t[0])
                vmax = max(vmax,v)

        m[(tuple(tr),w)] = vmax
        print(m[(tuple(tr),w)])
        return vmax 

print(thief(tr,max_w))




#递归——一个数的组成方式的个数
ll = [1,2,3,4]
aa={}
def st(m,ll,know):
    if m  ==0:
        return 1
    elif know[m] != 0:
        return know[m]
    else:
        ways = 0
        for j in [c for c in ll if c <=m]:
            ways += st(m-j,ll,know)
            know[m] = ways
    return ways
print(st(5,[1,2,3,4],[0]*6))




#递归——按规则分配，使用最少的糖果
def candy(ll):
    aa = [1]*len(ll)
    sum = 0
    for i in range(1,len(ll)):
        if ll[i] > ll[i-1]:
            aa[i] = aa[i-1]+1

    for i in range(len(ll)-2,-1,-1):
        if ll[i]> ll[i+1] and aa[i]<=aa[i+1]:
            aa[i] = aa[i+1]+1
        
    for i in aa:
        sum += i
    return sum

ll = eval(input())

print(candy(ll))




#递归——表达式加括号结果的个数
def findWays(expr):
    nums, ops = [], []
    num = 0
    for c in expr:
        if '0' <= c <= '9':
            num = num * 10 + ord(c) - 48
        else:
            ops.append(c)
            nums.append(num)
            num = 0
    else:
        nums.append(num)
    print(nums,ops)

    def calc(nums,ops):
        if not ops:
            return [nums[0]]
        elif len(ops) == 1:
            if ops[0] == '+':
                return [nums[0] + nums[1]]
            if ops[0] == '-':
                return [nums[0] - nums[1]]
            else:
                return [nums[0] * nums[1]]
        else:
            result = []
            for i in range(len(ops)):
                for num1 in calc(nums[:i+1],ops[:i]):
                    for num2 in calc(nums[i + 1:], ops[i + 1:]):
                        print(num1,num2)
                        result.append(calc([num1, num2], [ops[i]])[0])
            print('a',result)
            return list(set(result))

    return calc(nums, ops)

findWays('2*3-4*5')





# 快速排序——中值（中值将数据列按索引分为两部分，然后依次递归
# 指针从两头分别与中值比较，左指针碰到大的停，右指针碰到小的停，相互交换位置交换）
aa = input()
d_list = aa.split()
n =[]
#需要考虑输入的数据只有一个
def isMain(l):
    if len(l) ==1:
        print(1)
        print(l[0])
    else:
        for i in range(len(l)):
            if i == 0:
                if min(l[i+1:])> l[i]:
                    n.append(l[i])
            elif i == len(l)-1:
                if max(l[:i]) < l[i]:
                    n.append(l[i])
            elif max(l[:i]) < l[i] and min(l[i+1:])> l[i] :
                n.append(l[i])
            else:
                pass
    n.sort()
    r = ' '.join(m for m in n)
    r.strip()
    print(len(n))
    print(r)

isMain(d_list)




# 分半排序——找到第一个大小符合要求的数
N = int(input())
isBadVersion = eval(input())
def firstBadVersion(n):
    left = 1
    right = n
    while (left < right):
        mid = (left+right)//2
        if(isBadVersion(mid)):
            right =mid
        else:
            left = mid+1
    return left

print(firstBadVersion(N))