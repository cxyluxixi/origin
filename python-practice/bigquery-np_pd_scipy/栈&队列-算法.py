
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



def plat(uin):
    s = Stack()
    index = 0
    maxn = '9'
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
    print(func(S))



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
