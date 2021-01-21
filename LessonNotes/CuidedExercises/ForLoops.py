'''                 For Loops

'''
def print_list(lst):
	for string in lst:
		print(string)
  
print_list(["a","b","c"])  # a
                            # b
                            # c



# def print_gt3(lst):
#     for number in list:
#         print(number > 3)

#  print_gt3([1, 3, 5])
# False
# False
# True
#  
    
    

# def print_add3(lst):
# 	for number in lst:
# 		print(number + 3)

#  print_add3([3, 5, 7])
# 6
# 8
# 10



# def print_a_names(names):
# 	for name in names:
# 		if name.startswith("R"):
# 			print(name)

# print_a_names(["Anna", "Alvan", "Rich"])  # Rich


# def print_nums_gt3(numbers):
# 	for number in numbers:
# 		if number > 3:
# 			print(number)  # print_nums_gt3([1,2, 3,4, 7])
#                             # 4
#                             # 7


# This gets the first name that starts with 'R'
def get_name(names):
	for name in names:
		if name.startswith("R"):
			return name
 get_name(["Sam", "Rich", "Roger"])
'Rich'


# This gets the first odd number
def get_odd(numbers):
	for number in numbers:
		if number % 2 == 1:
			return number
get_odd([4, 7, 9])
7
