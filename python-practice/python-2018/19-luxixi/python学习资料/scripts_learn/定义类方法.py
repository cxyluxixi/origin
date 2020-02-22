Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Person(object):
    count = 0
    @classmethod
    def fx(cls):
        return cls.count
    def __init__(self,name):
        self.name = name
        Person.count = Person.count+1

>>> print Person.fx()
0
>>> class Person(object):
	count = 0
	@classmethod
	def __init__(self,name):
	    self.name=name
	    Person.count = Person.count + 1

	    
>>> class Person(object):
	count = 0
	@classmethod
	def fx(cls):
		return cls.count
	def __init__(self,name):
	    self.name=name
	    Person.count = Person.count + 1

	    
>>> print Person.fx()
0
>>> 
