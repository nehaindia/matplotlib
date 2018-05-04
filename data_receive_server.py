import socket
import matplotlib.pyplot as plt
import socket
import matplotlib.pyplot as plt
import pickle

HOST = '192.168.10.104'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(4096)
    print data
    data=pickle.listen(data)
    plt.plot(data)
    # naming the x axis
    plt.xlabel('x - axis')
    #naming the y axis
    plt.ylabel('y - axis')
 
    # giving a title to my graph
    plt.title('My first graph!')
 
    # function to show the plot
    plt.show()	
    if not data: break
    conn.send(data)
conn.close()
