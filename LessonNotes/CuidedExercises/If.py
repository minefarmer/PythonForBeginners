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

