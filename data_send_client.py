import socket, pickle

HOST = '192.168.10.104'
PORT = 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr = raw_input("enter x coordinates")

print arr
data_string = pickle.dumps(arr,-1)
s.send(data_string)

data = s.recv(4096)
data_arr = pickle.loads(data)
s.close()
print 'Received', repr(data_arr)
