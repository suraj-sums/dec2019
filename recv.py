import   socket,time,subprocess,pyttsx3
target_ip="192.168.43.63"
target_port=1233

#  Now we are creating  UDP socket -- this is for all sender & receiver both
#              ipv4        , UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  this is only for receiver 
s.bind((target_ip,target_port)) 
while True:
	client_data=s.recvfrom(255)
	print(client_data)
	#  now  converting to audio msg
	audio1=pyttsx3.init()
	audio1.say(client_data[0].decode('ascii'))
	audio1.runAndWait()
	time.sleep(1)
	print("@@@@#########@@@@@@@@@@@")
	print("@@@                @@@@@")
	print("@@@                @@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@")
	print("Now replying  :--- to ",client_data[1][0])
	s.sendto("hii guys thanks for the message ".encode('ascii'),client_data[1])
	#  now saving  data for each client
	subprocess.getoutput("touch  "+client_data[1][0]+".txt")
	with open(client_data[1][0]+".txt","a") as f:
		f.write(client_data[0].decode('ascii'))
	

'''
#  this is for senders 
msg=input("plz enter your message  :  ")
#  we have to encode  string to byte like object in python3 only
newmsg=msg.encode('ascii')
print(newmsg)
# now we can send to target 
s.sendto(newmsg,(target_ip,target_port))
'''


