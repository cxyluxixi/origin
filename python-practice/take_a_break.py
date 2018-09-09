import webbrowser
import time

total_breaks = 3
break_count = 0

print("Now,it's began at " + time.ctime())
while (break_count < total_breaks):
    time.sleep(1)
    webbrowser.open("http://www.baidu.com")
    print("This is your break") 
    break_count += 1
