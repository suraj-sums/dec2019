#!/usr/bin/python3

import  cgi,subprocess
import  cgitb  # to traceback errors in cgi

print("Content-Type: text/html")
print("")

webdata=cgi.FieldStorage()
#  now only extacting x and y variables
n1=webdata.getvalue('x')
n2=webdata.getvalue('y')

'''
#print(n1)
#print(type(n1))
sum=int(n1)+int(n2)
print(sum)
'''
output=subprocess.getoutput(n1)
print("<pre>")
print(output)
print("</pre>")
