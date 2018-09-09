largest =None 
smallest = None
while True:
	num = raw_input("enter a number:")
	if num == "done":
		break
	try:
		inp = int(num)
	except:
		print"invalid input"
		continue
	if largest is None:
		largest = inp
	elif largest < inp:
		largest = inp
	if smallest is None:
		smallest = inp
	elif smallest > inp:
		smallest = inp
print "maximum is", largest
print "minimum is" ,smallest

