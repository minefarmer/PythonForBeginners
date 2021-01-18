'''                 If, While: Umbrella Assistant
If {condition is true}, (run code)
   condition
if x < 5:
   x = 10
   expression

else:
    x = 2
    expresion

  
    
 if x < 5:
...   x = 10
... else:
...   x = 2
... 
 x
10
 

 name = "bob"
 if name == "john":
...   print("name verified")
... else:
...   print("unreconized name")
... 
unreconized name



While (condition is true), (run code)  *****************

       condition
while x < 3:
    x = x + 1
    expression




>>> x = 0
>>> while x < 5:
...     print(x)
...     x = x + 1
... 
0
1
2
3
4
>>> 





'''

from urllib.request import urlopen

def get_condition(city):
    url = "http://wttr.in/" + "?format=%C"
    page = urlopen(url)
    raw = page.read()
    condition = raw.decode("utf-8")
    return condition

city = input("City:")
condition = get_condition(city)
if condition == "Clear":
    print("No umbrella needed")
else:
    print("Bring umbrella")
    