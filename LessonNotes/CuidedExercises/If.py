>>> def gt5(x):
...     if x > 5:
...         return "yay!"
... 
>>> gt5(10)
'yay!'
>>> gt5(2)
>>> 


>>> def reaction(game):
...     if game == "among us":
...         return "yay!"
... 
>>> reaction("tic tac toe")
>>> reaction("among us")
'yay!'
>>> 



def gt5o(x):
	if x > 5:
		return "yay!"
	else:
		return "nu!"

 gt5o(10)
'yay!'
 gt5o(2)
'nu!'
 



def reaction(game):
	if game == "among us":
		return "yay!"
	else:
		return "nu!"

 reaction("among us")
'yay!'
 reaction("tic tack toe")
'nu!'
 



def blackjack(lst):
	if sum(lst) < 21:
		return sum(lst)
	else:
		return 0

 blackjack([20,20])
0
 blackjack([3, 4, 5])
12
 

def can_cook(lst):
	if "lemon" in lst:
		return lst
	else:
		return []

 can_cook(["lemon", "apple"])
['lemon', 'apple']
 can_cook(["apple"])
[]
 


def laugh(lst):
	if any(lst): # if True in lsrt:
		return "haha"
	else:
		return "uh"

 laugh([False, False])
'uh'
 laugh([True, False])
'haha'
 


i = 5
while i < 11:
	print(i)
	i += 1

5
6
7
8
9
10
 

i = 4
while i < 10:
	i += 1
	print(i)

5
6
7
8
9
10
 


i = 5
while i < 16:
	print(i)
	i += 2
 
 5
7
9
11
13
15
 



def print_from_to(x, y):
	i = x
	while i < y + 1:
		print(i)
		i += 1
  
 print_from_to(3, 6)
3
4
5
6
 


i = 5
while i < 11:
	if i % 3 != 0:
		print(i)
	i += 1
 
 5
7
8
10
 



i = 5
while i < 16:
	if i % 6 != 0:
		print(i)
	i += 1
 
 5
7
8
9
10
11
13
14
15
 
 