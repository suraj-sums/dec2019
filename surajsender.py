import socket
target_ip="192.168.43.63"
target_port=1233

#Now we are creating UDP Socket
#                  ipv4       ,         UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#this is for recever
s.bindt((target_ip,target_port))
while True:
    client_data=s.recvfrom(100)
    print(client_data)
    time.sleep((2)
    print("now replying to",client_data[1][0])
    s.sendto("hi guys",.encode('ascii'))(client_data[1])
#this is for sender
msg=input("plz enter your msg :")
#we have to encode string to byte like object in python 3 only
newmsg=msg.encode('ascii')
print(newmsg)
#now we can send to target

s.sendto(msg,(target_ip,target_port))
