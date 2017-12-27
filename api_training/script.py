'''
Created on Dec 25, 2017

@author: safwans
'''
from urllib2 import Request, urlopen, URLError


request = Request('http://placekitten.com/')

try:
    response = urlopen(request)
    kittens = response.read()
    print kittens[559:1000]
except URLError, e:
    print 'No Kittez, Got an error code:', e
