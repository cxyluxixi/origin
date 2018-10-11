#textProBar.py
# 第一种无法刷新的多行文本条
import time
scale =10
print("{:-^20}".format("start"))
for i in range(scale+1):
    a = '*'* i
    b = '.'* (scale-i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)

# 第二种单行刷新的文本条
import time 
for i in range(101):
    print("\r{:3}%".format(i))
    time.spleey(0.1)

#第三种单行刷新的文本条
# TextProBarV3.py
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))

