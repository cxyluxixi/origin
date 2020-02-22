Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def a(lst):
	def b():
	    def c(x,y):
		return x+y
	    return reduce(c,lst,2)
	return b

>>> m = a([2,4,5])
>>> print m()
13
>>> 
