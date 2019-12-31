#!/usr/bin/python3

import sys
#  to create a empty files 
file_names=sys.argv[1:]
for  i  in  file_names:
	f=open(i,'w')
#	f.write("hello world")
	f.close()
#  alternate  way 

for  i  in  file_names:
	with open(i,'w')  as  f:
		f.write("hey python \n")

#  like appending in a file
with open("aa.txt",'a') as f:
	f.write("this line is appended \n")


