# 亲密数对
# 对于两个不同的整数A和B，如果整数A的全部因子（包括1，不包括A本身）之和等于B；
# 且整数B的全部因子（包括1，不包括B本身）之和等于A，则将A和B称为亲密数。
# 自定义函数fac(x)计算x包括1但不包括本身的所有因子和并返回。从键盘输入整数n，
# 调用fac()函数寻找n以内的亲密数并输出。注意每个亲密数对只输出一次，小的在前大的在后，例如220-284。

def fac(m):
	s=0
	for i in range(1,int(m/2)+1):
		if m%i==0:
			s+=i
	return s

def hhh(n):
	for i in range(1,n):
		res=fac(i)
		if i!=res and fac(res)==i and i < res:                             #因子和不等于本身，且是亲密数，输出
			print("{}-{}".format(i, res))

n = int(input())
hhh(n)