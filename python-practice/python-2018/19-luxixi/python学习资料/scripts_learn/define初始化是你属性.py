Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Person(object):
    #增加属性和对应的值
	def __init__(self,name,gender,**kw):
        self.name = name
        self.gender = gender
        for k,v in kw.iteritems():
            setattr(self,k,v)

            
>>> a = Person('wer','male',age = 19,course = 'R')
>>> print a.age
19
>>> print a.age()

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print a.age()
TypeError: 'int' object is not callable
>>> print a.course
R
>>> print a.age
19
>>> def f(z):
#map()函数的使用
    return z[0].upper() + z[1:].lower()
print map(f,['wer','c','dfh','sdfbc','sfgb'])

#reduce函数的使用
def f(n,m):
    return m*n
print reduce(f,[3,25,63])


#filter函数的使用
def f(y):
    x = int(y/10)
    return x*10 == y
print filter(f,range(0,101))

#闭包中的变量不要使用循环变量，使用嵌套，最基本的三层函数嵌套
def count():
    fs=[]
    for i in range(1,4):
        def f1(j):
            def f2():
                return j*j
            return f2
        m =f1(i)
        fs.append(m)
    return fs
print fs


#任意参数的装饰器的使用
#装饰器是一种对功能的封装
import time
def performance(f):
    def fn(*args,**kw):
        t1 = time.time()
        r = f(*args,**kw)
        t2 = time.time()
        print 'call %s() in %fs' %(f.__name__,(t2-t1))
        return r
    return fn
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print factorial(10)

#返回函数，返回函数值
def f1(f):
    def f2():
        def f3(a,b):
            return a+b
        return reduce(f3,f,0)
    return f2
m = f1([1,4,5,6])
print m()


def f1(f):
    def f2():
        def f3(a,b):
            return a*b+5
        return reduce(f3,f,1)
    return f2
m = f1([1,2,5.3])
print m()

#有参数的decorator
import time

def performance(prefix):
    def log_decorator(f):
        def log_performance(*args,**kw):
            t1 = time.time()
            r = f(*args,**kw)
            t2 = time.time()
            t = (t2 -t1)*1000 if prefix =='ms'else(t2-t1)
            print 'call %s()in %f %s' % (f.__name__, t,prefix)
            return r
        return log_performance
    return log_decorator
@performance('oo')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)

#完善装饰器
import time, functools

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args,**kw):
            t1=time.time()
            r=f(*args,**kw)
            t2=time.time()
            print 'call %s() in %f %s...'%(f.__name__,t2-t1,unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
print factorial.__name__

#偏函数的编写
import functools

sorted_ignore_case = functools.partial(sorted,cmp = lambda x,y: cmp(x.upper(),y.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

import functools
f1 =functools.partial(sorted,cmp = lambda x,y:cmp (x.upper(),y.upper()))
print f1(['a','t','d'])

#class is used to make a definition.实例化一个类，并添加属性数值
class Score:
	pass
a1 = Score()
a2 = Score()
a1.x = 2
a1.y = 3
a2.x = 4
a2.y = 5

print (a1.x,a1.y,a2.x,a2.y)

class Point:
	def reset(self):
		self.a = 3
		self.b = 3
p = Point()
p.reset()#equal to : Point.reset(p)
print (p.a,p.b)

#让类做一些事情，比如移动点，计算点与点之间的距离
import math
class Point:
	def move(self,x,y):
		self.x = x 
		self.y = y 
	def reset(self)
		self.move(0,0)
	def calculate_dictance(self,other_point):
		return math.sqrt(
		(self.x - self.other_point.x)**2+
		(self.y - self.other_point.y)**2)
>>> point1 = Point()
>>> point2 = Point()
>>> point1.reset()
>>> point2.move(5,0)
>>> print (point2.calculate_distance(point1))
5.0
>>> point1.move(3,2)
>>> print (point2.calculate_distance(poin1))

#初始化，也就是说在创建类的时候，就设置实例，并且要求必须输入实例的参数
class Point:
	def __init__(self,x,y)
		self.move(x,y)
	def move(self,x,y)
		self.x = x
		self.y = y 
	def reset(self):
		self.move(0,0)
#这样，在实例化一个对象的时候，就必须同时提供x，y的值，如下：
point = Point(3,5)#如果不写3,5，写成Point(),会报错

#导入模块中的类或函数：from database(模块) import Database(函数)  import math.sqrt
#导入模块的函数或类并改名：from 模块 import 函数 as new name

#模块相当一个单一或多功能元件，相当于一个文件，里面包含直接的物件
#包相当于文件夹，多个模块放到一起的集合就是包。建立文件夹时，必须要先放一个__init__.py文件，如下：
parent_directory/
	main.py
	ecommerce/
			__init__.py
			database.py
			products.py 
			payments/
					__init__.py
					paypal.py
					customsname.py
			contact/
					email.py


#绝对导入，需要指明这个模块、函数的完整路径。
import ecommerce.products
product = ecommerce.products.Product()
#or
from ecommerce.products import Product 
product = Product()
#or 
from ecommerce import products
product = products.Product()

#相对导入，就是在当前模块所在的包(ecommerce包）导入同级别模块（database，payments等）里的类或者函数，如下：
	#我们现在在products模块下工作，想从database模块里导入Database类
	from .database import Database
	#如果我们正在编辑ecommerce.payments包里的paypal模块，想导入Database：
	from ..database import Database
	#也就是说使用更多的点来访问当前编辑位置的上一级和上上一级。
	#当前在payments的paypal模块，想导入contact.email中的send_email函数:
	from ..contact.email import send_email #使用..先回到ecommerce,然后获取contact，再通过点获取email，用import获取send_email
	#此时database看起来是这样的：
		class Database：
			pass
		database = Database()
		#这样调用的Database，在第一次导入Database模块时，就立即创建了database对象,会减缓程序启动
		#我们想要减缓对象的创建，从而快速启动程序。如下：
		class Database：
			pass
		database = None
		def initialize_database():
			global database
			database = Database()
		#global is a key word ，表示在这里创建一个全局变量，只有当initialize这个函数被调用时，才会创建一个全局变量。
		
'''如下：__name__变量，当导入这个模块的时候，这个变量指明了模块的名字，
但是当模块直接通过文件执行（而不是被导入到其他模块执行）的时候，就不会导入这个变量。'''
def main():
	print(something)
if __name__ == "__main__":
	main()
	#这样把编写的代码包在if __name__ =="__main__":limian ,便成了一个策略，非常有用
	
#类通常在模块级别里定义，但是他们也可以在一个函数或者方法内部定义：
def format_string(string,formatter = None):
	'''Format a string using the formatter object,which
	is expected to have a format() method that accepts
	a string '''
	class DefaultFormatter:
		def format(self,string):
			return str(string).title()
	
	if not formatter:
		formatter = DefaultFormatter()
	return formatter.format(string)
>>>print("output:"+ format_string(hello_string))
output:Hello World,How Are You Today?

#简单的记事本应用，首先搭建文件模块结构：一个parent_directory/，包含三个模块：notebook.py,menu.py,command_option.py
import datatime
last_id = 0 #为备注储存id，起始id为0，使用id+=1
class Note:
#创建Note这个类，里面是一条一条的notes
	def __inite__(self,memo,tags =''):
		self.memo = memo 
		self.tags = tags
		self.creation_data = datatime.data.today()
		global last_id#创建一个全局变量，使得在别的模块也可以调用和使用这个变量
		last_id += 1
		self.id = last_id
	def match(self,filter)
		return filter in self.memo or filter in self.tags
		
class Notebook:
	#创建Notebook这个功能集合，里面有各种方法（函数），
	def __init__(self):
		self.notes = []
	def new_note(self,memo,tags = ''):
		self.notes.append(Note(memo,tags))
	def modify_memo(self,note_id,memo):
		for note in self.notes:
			if note.id = note_id :
				note.memo = memo
				break
	def modify_tags(self,note_id,tags):
		for note in self.notes:
			if note.id = note_id:
				note.tags = tages
				break
	def search(self,filter):
	#定义一个查找并判断是否匹配的方法
		return [note for note in self.notes if note.match(filter)]
	
	#通过id来定位备注的方法，find_note可以加下划线开头，这样这个方法就仅供内部使用
	def _find_note(self,note_id):
		for note in self.notes:
		if note.id == note_id:# if str(note.id) ==str(note_id):return note  else:return None
			return note
		return None
	def modify_memo(self,note_id,memo):
	#if note:note.memo ==memo return True else:return False
		self._find_note(note_id).memo = memo 
	#menu接口，只需要简单的提供一个菜单并允许用户输入关键词
	import sys
	from notebook import Notebook,Note
	class menu:
		def __init__(self):
		self.notebook = Notebook()
		self.choices = {
		"1":self.show_notes,
		"2":self.search_notes,
		"3":self.add_note,
		"4":self.modify_note.
		"5":self.quit
		}
		
		def display(self):
			print ('''
			Notebook Menu
			1.show all Notes
			2.Search Notes
			3.Add Note
			4.Modify Note
			5.Quit
			''')
		def run(self):
			while True:
				self.display_menu():
				choice = input('enter an option')
				action = sef.choice.get(choice)
				if action:
					action()
				else:
				print ("{0}is not a valid choice".format(choice))
			
		def show_notes(self,note = None):
			if not notes:
				notes = self.notebook.notes
			for note in notes:
			print('{0}:{1}\n{2}".format(
				note.id,note.tags,note.memo))
		def search_notes(self):
			filter = input('search for:')
			notes = self.notebook.search(filter)
			self.show_notes(notes)
		def add_note(self):
			memo = input('enter a memo:')
			self.notebook.new_note(memo)
			print ('your note has been added.')
		def modify_note(self):
			id = input('enter a note id:')
			memo = input('enter a memo:')
			tags = input('enter  tags:')
			if memo:
				self.notebook.modift_memo(id,memo)
			if tags:
				self.motebookl.modify_tags(id,tags)
		def quit(self):
			print ('sdf')
			sys.exit(0)
	if __name__ ==" __main__":
		Menu().run()
		'''#这段代码首先通过一个绝对导入语句导入笔记本对象，
		不能使用相对导入，因为我们还没有把我们的代码放到一个包里。
		menu 的run方法会重复地现实菜单选项（dict），用户输入一个choice，就从dict里检索这个对象
		action实际上是调用一个特定方法的接口，通过action（）来调用这个方法。
		当用户输入不存在的选项时，返回错误提示语句，所以action里面需要一个判断检查。'''
		
class Contact:
#类的继承
	all_contacts = []
	def __init__(self,name,email):
		self.name = name
		self.email = email 
		Contact.all_contacts.append(self)		
class Supplier(Contact):
	def order(self,order):
		print ('the order of {} is {}'.format(order,self.name))
c = Contact('a','email')
s = Supplier('v','emails')
s.order('your order')

'''创建一个新的类来扩展list，然后实例化这个子类（Contactlist）作为列表（all_contacts = Contactlist（））,
和上面不同（上面是实例化一个list作为一个类）'''
class Contactlist(list):#list这个内置语法，我们创建一个空的列表，[] == list()（相同的语法），然后这个就可以扩展，
	def search(self,name):#拓展内置类最典型的就是给它增加功能。扩展一个search方法，通过名字来搜索联系人
		matching_contacts = []
		for contact in self:
			if name in Contact.name:
				maching_contacts.append(contact)
			return matching_contacts
class Contact:
	all_contacts = Contactlist()#联系上面的class Contactlist（list），list可以扩展，（）里也可以用dict，但是dict语法很繁琐。
	def __init__(self,name,email):
	self.name = name
	self.email = email 
	self.all_contacts.append(self)
a1 = Contact('sdf','aw')
a2 = Contact('asdf','fag')
a.name for a in Contact.all_contacts.search('df')

class fx(dict):#dict的扩展
	def f2(self):
		longest = None
		for key in self:
			if not longest or len(key) > len(longest):
				longest = key
			return longest

		
>>> longkeys = fx()
>>> longkeys['hello'] = 1
>>> longkeys['longest yet'] = 5
>>> longkeys['hello2'] = 'world'
>>> longkeys.f2()
'longest yet'
>>> longkeys['wefadsgsfds'] = 2
>>> longkeys.f2()
'wefadsgsfds'

#重写和super：就是在子类里想要添加新方法或者改变或者覆盖父类（超类）里的方法，使得整个父类都可以用这个功能
class Friend(Contact):
	def __init__(self,name,email,phone):
		super().__init__(name,email)
		self.phone = phone
		#上面的super().__init__(name,email) 相当于复制父类里面的属性的简写 ：
		''' self.name = name
			self.email = email'''
		#然后再加上自己的属性，self.phone = phone
		
#super的使用，super表示调用下一个（index），父类总是排在派生类之后，所以object最后被调用。
class Baseclass：
	num_base_calls = 0
	def call_me(self):
		print 'calling method on the base class'
		self.num_base_calls +=1
		
class LeftSubClass(Baseclass):
	num_left_calls = 0
	def call_me(self):
		super().call_me()
		print 'calling method on the left subclass'
		self.num_left_calls +=1 
		
class RightSubClass(Baseclass):
	num_right_calls = 0 
	def call_me(self):
		super().call_me()
		print 'calling method on the right subclass'
		self.num_right_calls +=1 
class SubClass(LeftSubClass,RightSubClass):
	num_sub_class = 0 
	def call_me(self):
		super().call_me()
		print 'calling method on the subclass'
		self.num_sub_calls +=1
		
s = Subclass()
s.call_me()

#最终super使用的版本
>>> class Contact(object):
	all_contacts = []
	def __init__(self,name='',email='',**kw):
		super().__init__(**kw)
		self.name = name
		self.email = email
		self.all_contacts.append(self)

>>> class AddressHolder(object):
	def __init__(self,street='',city='',state='',code='',**kw):
		super().__init__(**kw)
		self.street = street
		self.city = city
		self.state = state
		self.code = code

>>> class Friend(Contact,AddressHolder):
	def __init__(self,phone='',**kw):
		super().__init__(**kw)
		self.phone = phone
		
		
#多态，不用管对象时哪一个子类，只管调用方法，多态地让对象去处理实际细节
>>> class fx:
	def __init__(self,filename):
		if not filename.endswith(self.ext):
			raise Exception('invalid file format')
		self.filename = filename

		
>>> class mp3file(fx):
	ext = 'mp3'
	def play(self):
		print 'playing {}as mp3'.format(self.filename)

		
>>> class wavfile(fx):
	ext = 'wav'
	def play(self):
		print ' playing {}as wav'.format(self.filename)

		
>>> mp3 = mp3file('thisisawar.mp3')
>>> mp3.play()
playing thisisawar.mp3as mp3

#一个房地产应用程序（用来管理购买或者租赁房产）
class Property:#录入参数并储存房产信息
	def __init__(self,square_feet='',beds='',baths='',**kw):
		super().__init__(**kw)
		self.square_feet = square_feet
		self.num_beds = beds 
		self.num_baths = baths
		
	def display(self):#呈现房产信息
		print ('Property Details')
		print ('================')
		print ('square footage:{}'.format(self.square_feet))
		print ('bedrooms:{}'.format(self.num_beds))
		print ('bathrooms:{}'.format(self.num_baths))
		print ()
		
	def promptt_init():#静态方法，给用户输入做一些提示
	#静态方法纸盒一个类（累的变量）关联，而不是和一个具体的对象实例关联。
	#所以它没有self函数，super关键字不起作用（没有父类对象，只有父类），所以在父类里直接调用这个静态方法
	#通过函数创建可以传递到__init__方法中的dict，dict中的键值通过input方法来提示输入。
		return dict(square_feet=input('enter the square feet:'),beds=input('enter the number of bedrooms:'),baths=input('enter the number of bathrooms:'))
	prompt_init = staticmethod(prompt_init)
	
class Apartment(Property):
	valid_laundries = ('coin','ensuite','none')
	valid_balconies = ('yes','no','solarium')
	def __init__(self,balcony='',laundry='',**kw):
		super().__init__(**kw)
		self.balcony = balcony
		self.laundry = laundry
		
	def display(self):
	super().display()
	print ('Apartment Details')
	print ('laundry: %s' % self.laundry)
	print ('balcony: %s' % self.balcony)
	
	parent_init = Property.prompt_init()
	laundry=''
	while laundry.lower()not in \
			Apartment.valid_laundries:
		laundry = input('what laundry facilities does the property have?({})'.format(','.join(Apartment.valid_laundries))
	balcony=''
	while balcony.lower() not in \
			Apartment.valid_balconies:
		balcony = input('does the property have a balcony?.format(','.join(Apartment.valid_balconies))
		parent_init.update({'laundry':laundry,'balcony':balcony})
		return parent_init
	prompt_init = staticmethod(prompt_init)
	
	#or prompt_init可以这么写
	def prompt_init():
		parent_init = Property.prompt_init()
		laundry = get_valid_input('what laundry facilities does the property have?',Apartment.valid_laundries)
		balcony = get_valid_input('does the property have a balcony?',Apartment.valid_balconies)
		parent_init.update({'laundry':laundry,'balcony':balcony})
		return parent_init
	prompt_init = staticmethod(prompt_init)
	
class House(Property):
	valid_garage = ('attached','detached','none')
	valid_fenced = ('yes','no')
	def __init__(self,num_stories='',garage='',fenced='',**kw):
		super().__init__(**kw)
		self.garage = garage
		self.fenced = fenced
		self.num_stories = num_stories
		
	def display(self):
		super().display()
		print ('House Details')
		print ('# of stories:{}'.format(self.num_stories))
		print ('garage:{}'.format(self.garage))
		print ('fenced:{}'.format(self.fenced))
		
	def prompt_init():
		parent_init = Property.prompt_init()
		fenced = get_valid_input('is the yard fenced?',House.valid_fenced)
		garage = get_valid_input('is there a garage?',House.valid_garage)
		num_stories = input('how many stories?')
		parent_init.update({'fenced':fenced,'garage':garage,'num_stories':num_stories})
		
	return parent_init
prompt_init = staticmethod(prompt_init)

class Purchase:
	def __init__(self,price='',taxes='',**kw):
		super().__init__(**kw)
		self.price = price
		self.taxes = taxes
		
	def display(self):
		super().display()
		print("PURCHASE DETAILS")
		print ("selling price:{}".format(self.price))
		print ("estimated taxes:{}".format(self.taxes))
		def prompt_int():
			return dict(
				price = input("What is the selling price?"),
				taxes = input("What are the estimated taxes"))
		prompt_init=staticmethod(prompt_init)
		
class Rental:
	def __init__(self,furnished='',utilities='',rent='',**kw):
		super().__Init__(&&kw)
		self.furnished = furnished
		self.rent = rentself.utilities = utilities
	def display(self):
		super().display()
		print ("RENTAL DETAILS")
		print ("rent:{}".format(self.rent))
		print ("estimated:{}".format(self.utilities))
		print ("furnished:{}".format(self.furnished))
	def prompt_init():
		return dict(
			rent=input("What is the monthly rent?"),
			utilities = input("What are the estimated utilities?"),
			furnished = get_valid_input("Is the property furnished?",("yes","no")))
	prompt_init=staticmethod(promp_init)
		
class HouseRental(Rental,House):#这里需要注意顺序，不能用House，Rental，因为super调用顺序的为，House在前将不会调用Rental的super。
	def prompt_init():
		init = House.prompt_init()
		init.updata(Rental.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)
		
		
class ApartmentRental(Rental,Apartment):#开始创建组合子类
	def prompt_init():
		init = Apartment.promp_init()
		init.updata(Rental.promp_init())
		return init
	prompt_init = staticmethod(prompt_init)
	
class ApartmentPurchase(Purchase,Apartment):
	def Prompt_init():
		init = Apartment.promp_init()
		init.updata(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)
	
class HousePurchase(Purchase,House):
	def Prompt_init():
		init = House.prompt_init()
		init.updata(Purchase.prompt_init())
		return init
	prompt_init = staticmethod(prompt_init)
	
class Agent:#创建代理，负责创建新的列表并显示现有列表
	def __init__(self):
		self.property_list = []
	def display_properties(self):
		for property in self.property_list:
		property.display()
		
	def add_property(self):
		property_type= get_valid_input(
		"What type of property?",("house","apartment")).lower()
		payment_type = get_valid_input("What payment_type?",("purchase","rental")).lower()
	PropertyClass = self.type_map[(property_type,payment_type)]
	init _args = PerpertyClass.prompt_init()
	self.property_list.append(PropertyClass(**init_args))
	
	#定义类方法，def分析（cls），使用@classmethod进行装饰
class Person(object):
    __count = 0
    @classmethod
    def fx(cls):
        return cls.__count
    def __init__(self,name):
        self.name = name
        Person.__count = Person.__count+1
print Person.fx()
        
p1 = Person('Bob')

print Person.fx()


#@property的设置，有装饰器把方法变成属性，直接调用。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if score >= 80:
            return 'A'
        elif score < 60:
            return 'C'
        else:
            return 'B'
        self.__score = score
    

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade

L = M = [1, 2] L = L + [3, 4] # L = [1, 2, 3, 4], M = [1, 2] 
L += [3, 4] # L = [1, 2, 3, 4], M = [1, 2, 3, 4]



x|y， x&y， x^y#或，与，异或
x >> y , x<<y, #x左移y位，x右移y位

#简单的身份验证和授权系统
>>> class User:
	def __init__(self,username,password):
		self.username = username
		self.password = self._encrypt_pw(password)
		self.is_logged_in = False
	def _encrypt_pw(self,password):
		hash_string = (self.username + password)
		hash_string = hash_string.encode("uft8")
		return hashlib.sha256(has_string).hexdigest()
	def check_password(self,password):
		encrypted = self._encrypt_pw(password)
		return encrypted == self.password

	
>>> class AuthException(Exception):
	def __init__(self,username,user = None):
		super().__init__(username,user)
		self.username = username
		self.user = user

		
>>> class UsernameAlreadyExist(AuthException):
	pass

>>> class PasswordTooShort(AuthException):
	pass

>>> class Authenticatior:
	def __init__(self):
		self.users = {}
	def add_user(self,username,password):
		if username in self.users:
			raise UsernameAlreadyExist(username)
		if len(password) < 6:
			raise PasswordTooShort(username)
		self.users[username] = User(username,password)
>>> class InvalidUsername(AuthException):
	pass

>>> class InvalidPassword(AuthException):
	pass

>>> class Authenticatior:
	def __init__(self):
		self.users = {}
	def login(self,username,password):
		try:
			user = self.users[username]
		except KeyError:
			raise InvalidUsername(username)
		if not user.check_password(password):
			raise InvalidPassword(username,user)
		user.is_logged_in = True
		return True
	def is_logged_in(self,username):
		if username in self.user:
			return self.users[username].is_logged_in
		return False
>>> authenticatior = Authenticatior()

	
>>> class Authorizor:
	def __init__(self,authenticatior):
		self.authenticatior = authenticatior
		self.permissions = {}
	def add_permission(self,perm_name):
		try:
			perm_set = self.permissionts[perm_name]
		except KeyError:
			self.permissions[perm_name] = set()
		else:
			raise PermissionError("permission Exists")
	def Permit_user(self,perm_name,username):
		try:
			perm_set = self.permissions[per_name]
		except KeyError:
			raise PermissionError("permission does not exist")
		else:
			if username not in self.authenticatior.users:
				raise InvalidUsername(username)
			perm_set.add(username)

>>> class PermissionError(Exception):
	pass

>>> class Authorizor:
	def __init__(self,authenticatior):
		self.authenticatior = authenticatior
		self.permissions = {}
	def check_permission(self,perm_name,username):
		if not self.authenticatior.is_logged_in(username):
			raise NotloggedInError(username)
		try:
			perm_set = self.permissions[perm_name]
		except KeyError:
			raise PermissionError("permission does not exist")
		else:
			if username not in perm_set:
				raise NotPermissionedError(username)
			else:
				return True

			
>>> class NotloggedInError(AuthException):
	pass

>>> class NotPermissionedError(AuthException):
	pass

>>> Authorizor = Authorizor(authenticatior)
#菜单接口的设置
class Editor:
	def __init__(self):
		self.username = None
		self.menu_map = {
		"login":self.login,
		"test":self.test,
		"change":self.change,
		"quit":self.quit}
		
	def login(self):
		logged_in =False
		while not logged_in:
			username = input("username: ")
			password = input("password: ")
			try:
				logged_in = auth.authenticatior.login(username,password)
			except auth.InvalidUsername:
				print "sorry,the username does not exist "
			except auth.InvalidPassword:
				print "sorry,incorrect password"
			else:
			self.username = username
			
	def is_permitted(self,permission):
		try:
			auth.authorizor.check_permission(permission,self.username)
		except auth.NotLoggedInError as e:
			print "{} is not logged in ".format(e.username)
			return False
		except auth.NotPermissionedError as e :
			print "{} cannot {}".format(e.username,permission)
			return False
		else:
			return True
		
	def test(self):
		if self.is_permitted("test program"):
			print"testing program now..."
		
	def change(self):
		if self.is_permitted("change program"):
			print "changing program now..."
		
	def quit(self):
		raise SystemExit()
	def menu(self):
		try:
			answer = ""
			while True:
				print"""please enter a command:
				\tlogin\tlogin
				\ttest\tTest the program
				\tchange\tChange the program
				\tqiut\tQuit
				"""
				answer = input("enter a command: ").lower()
				try:
					func = self.menu_map[answer]
				except KeyError:
					print "{} is not a valid option".format(answer)
				else:
					func()
			finally:
				print "thank you for testing the auth module"
				
Editor().menu()
