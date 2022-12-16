
import socket
import json
from _thread import *
import threading
ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 3022
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')

ServerSideSocket.listen(1)
def multi_threaded_client(connection):
    # connection.send(str.encode('Server is working:'))
    print ("Total number of threads", threading.activeCount())
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        jsonObjectString=data.decode("utf-8").replace("'", '"')
        print('string',jsonObjectString)
        print ("Total number of threads", threading.activeCount())
        
        jsonObject=json.loads(jsonObjectString)
        print(jsonObject)
        #print(type (jsonObject))
        print(jsonObject['DeviceId'])
        
        
        
        if not data:
            print('if not')
            break
        connection.sendall(str.encode(response))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    #print('abc',address)
    
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
ServerSideSocket.close()