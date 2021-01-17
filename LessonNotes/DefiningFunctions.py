'''                 Defining Functions:
         input # a.k.a.  argument
def square(x):
    function
    name
    
    return x * x
            expression

'''
from urllib.request import urlopen

def square(x):
    return x*x 

def get_temperature(city):
    url = "http://wttr.in/" + city + "format=%t"
    page = urlopen(url)
    raw = page.read()
    temp = raw.decode("utf-8")
    return temp

city = input("City: ")
temp = get_temperature(city)
print(temp)