'''
Created on Dec 25, 2017

@author: safwans
'''
from urllib2 import Request, urlopen, URLError

def display_kitten():
    request = Request('http://placekitten.com/')
    try:
        response = urlopen(request)
        kitten = response.read()
        print(kitten[559:1000])
    except URLError, e:
        "No kittez, Got an error code", e
        
def display_kitten2():
    kittens = urlopen('http://placekitten.com/200/300')
    file = open('kittens.jpg', 'wb')
    file.write(kittens.read())
    file.close()

def main():
    print("test apis...")
    display_kitten()
    display_kitten2()
if __name__ == '__main__':
    main()