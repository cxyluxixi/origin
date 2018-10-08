# time()
import time 
time.time() #当前计算机内部的时间，返回浮点数
time.ctime() #当前时间用人易读的方式表示，周几，几月，几号，几点几分，哪一年，返回字符串
time.gmtime() #形成关于时间的数据，用于计算机使用，形如一个变量存储一个关于时间的数值

# 将时间变量变成格式化的字符串
time.strftime("form比如%Y-%m-%d-%H-%M-%S，其中月份除了m还有全称的B，所写的b，除了日期还有星期A，和星期缩写a，12小时的h，上午下午的p也就是AM PM")
# 要格式化的时间变量(这里这些变量通过time.gmtime()获取）)

# 讲字符串变成时间变量
timeString = 1
time.strftime(timeString,"form %Y-")

# 精准计时器，perf_counter(),多次调用，计算差值
start = time.perf_counter()
end = time.perf_counter()

thisXXX_time = end - start
# 产生时间sleep()
def wait():
    time.sleep(3.3) #调用这个wait()，让程序暂停3.3s