def a(lst):
	def b():
		def c(x,y):
			return x+y
		return reduce(c,lst,2)
	return b

# m = a([2,4,5])
# print m()
# 13

