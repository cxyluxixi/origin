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


def check(lst1,lst2):
    position = 0
    for i in range(len(lst1)-1):
        if lst2[i+1]<lst2[i]:
            position = i+1
            break
    if lst1[position:] == lst2[position:]: # 判断是否为插入排序
        lst2 = sorted(lst2[:position+1])+lst2[position+1:]
        print('Insertion Sort')
        print(' '.join([str(i) for i in lst2]))
    else: # 否则为归并排序
        cnt = 2
        lst = lst2
        while lst == lst2: # 对排序后的列表不断进行归并排序直到列表改变
            lst = [sorted(lst2[i:i+cnt]) for i in range(0,len(lst2),cnt)]
            lst = [num for sub_lst in lst for num in sub_lst]
            cnt *= 2
        print('Merge Sort')
        print(' '.join([str(i) for i in lst]))


lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
check(lst1, lst2)
