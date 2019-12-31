import   socket
target_ip="192.168.43.63"
target_port=1233

#  Now we are creating  UDP socket -- this is for all sender & receiver both
#              ipv4        , UDP 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#  this is only for receiver 
#s.bind((target_ip,target_port)) 


#  this is for senders 
while True:
	msg=input("plz enter your message  :  ")
#  we have to encode  string to byte like object in python3 only
	newmsg=msg.encode('ascii')
	print(newmsg)
# now we can send to target 
	s.sendto(newmsg,(target_ip,target_port))
	print(s.recvfrom(100))

