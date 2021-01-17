def mul3(x):
	return x * 3  # mul3(5) # 15

def sub3(x):
	return x - 3  # sub3(6)  # 3

def prod(x, y):
	return x * y  # prod(3, 5)  # 15

def add(x, y):  # add(3, 9)  # 8
	return x + y

def prod(x, y, a):
	return(x * y * a)  # prod(3, 5, 7)  # 105

def gt3(a):  #
	return a > 3  # gt3(15)  # gt3(15) # true

def lt10(b):
	return b < 10  # lt10(14)  # False

def both_gt_3(x, y):
	return(x > 3, y > 3)  # both_gt_3(1, 5) # (False, True)

def sum3(lst):
	return sum(lst) * 3  # sum3([1,2,3,4])  # 30

def sumv(dictionary):
	return sum(dictionary.values())  # sumv({"a": 1, "b": 2})  # 3

def is_jack_one(dictionary):
	return dictionary["jack"] == 1  # is_jack_one({"jack": 1})
									#  True
									# is_jack_one({"jack": 2})
									#  False

def add3_jack(dictionary):
	return dictionary["jack"] + 3  # add3_jack({"jack": 1})
									# 4
									# add3_jack({"jack": 2})
									# 5