# 找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2^P-1，则称M为默尼森数。
# 例如，P=5，M=2^P-1=31，5和31都是素数，因此31是默尼森数。

import math
def prime(num):
	zz = [2]
	k = math.sqrt(num)
	for i in range(3, int(k+1), 2):
		if num % i ==0:
			return False
	return num

def monisen(no):
	y1 = [2]
	a = 3
	while True :
		P = prime(a)
		if P == False:
			a = a+ 2
			continue
		M = 2**P-1
		if prime(M) == False:
			a = a+2
		else:
			y1.append(M)
			a = a+2
		if len(y1) == no:
			break
	return y1[-1]

print(monisen(int(input())))