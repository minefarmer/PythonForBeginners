'''                 For Loop
>>> range(10)
range(0, 10)
>>> iterable = range(10)
>>> list(iterable)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 


    iterable
range(10)

    item
for i in range(10):
    print(i)
...     
... 
0
1
2
3
4
5
6
7
8
9



>>> list("HelloWorld")
['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
>>> for i in "Hello World":
...     print(i)
... 
H
e
l
l
o
 
W
o
r
l
d
>>> 







'''

def check(password):
    has_number = False
    for i in password:
        if i.isdigit():
            has_number = True
    return has_number

password = input("Password: ")
has_number = check(password)
print(has_number)

Password: ruff5
True
 
