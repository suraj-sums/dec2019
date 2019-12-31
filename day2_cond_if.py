#!/usr/bin/python3
import  subprocess,time
import  webbrowser  #  it will open default browser 
options="""
Press  1  to  start your default web browser :- 
Press  2  to  check your internet connection speed :- 
Press  3  to check your internet status  :- 
Press  4  to check current date and  time:- 
Press  5   to check current temperature in your city :- 
Press  6   to check current public IP :- 
Press  7   to create  a directory in your OS :- 
Press  8   to reboot your system :- 
Press  9   to play song in you tube  :- 
Press  10   to search something in google search engine  :- 
"""
print(options)
#  to accept input from user
choice=input()
#  input  function will accept in string form only
print("you have entered  "+choice)
#  conditional statements
if  choice  ==  '4'  :
	print("current time is ",subprocess.getoutput("date +%T"))

elif  choice  ==  '1'  :
	print("opening  browser plz wait...")
	time.sleep(3)
	#  opening  default browser
	webbrowser.open_new_tab('https://www.google.com')
elif  choice  ==  '3'  :
	output=subprocess.getstatusoutput('ping -c 2 8.8.8.8')
	if output[0] == 0 :
		print("your Internet is Working Fine..")
	else :
		print("Your internet is not working..")

elif  choice  ==  '7'  :
	#  asking for directory name 
	dir_name=input("Please enter name of Directory :- ")
	dir_output=subprocess.getstatusoutput("mkdir  "+dir_name)
	if dir_output[0]  ==  0 :
		print("your directory  "+dir_name+" Successfully created ")
	else :
		print("Please choose another directory name ")

elif  choice  ==  '10'  :
#   taking user input 
	msg=input("please enter your message to search on Google :- ")
	time.sleep(2)
	#  opening  default browser
	webbrowser.open_new_tab('https://www.google.com/search?q='+msg)



else :
	print("wrong option")
