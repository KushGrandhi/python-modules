#pip install pyshortners

import pyshorteners

link = input("enter the link to shorten:")
shortener = pyshorteners.Shortener() 

shorten_link = shortener.tinyurl.short(link) 

print(shorten_link)

#Sample Input:
# enter the link:https://github.com/KushGrandhi/python-modules/issues/1

#Sample Output
#http://tinyurl.com/y6jfc7cy
