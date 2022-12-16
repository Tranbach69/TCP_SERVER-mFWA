
import socket
import threading
import time
from _thread import *
ServerSideSocket = socket.socket()
host = '0.0.0.0'
port = 3022
ThreadCount = 0
respon='{ "DeviceId": "zxcvbnm", "Index": 1, "WifiOpen": 1, "WifiMode": 2, "CurrentAp": 2, "WifiNat": 0, "Wifi": [ { "Ssid": "11wwwwww", "BoardCast": 1 }, { "Ssid": "22qqqqq", "BoardCast": 2 } ] }'
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')

ServerSideSocket.listen(1)
def multi_threaded_client(connection):
    # connection.send(str.encode('Server is working:'))
    # connection.send(str.encode(respon))
    
    while True:
        data = connection.recv(2048)
        # response = 'Server message: ' + data.decode('utf-8')
        jsonObjectString=data.decode("utf-8").replace("'", '"')
        print('string',jsonObjectString)
        connection.sendall(str.encode('tttatatatat'))
        print ("Total number of threads", threading.activeCount())
        time.sleep(2.4)
        print("Printed after 2.4 seconds.")
        
        # jsonObject=json.loads(jsonObjectString)
        # print(jsonObject)
        # #print(type (jsonObject))
        # print(jsonObject['DeviceId'])
        # connection.send(str.encode(respon))
        
        
        
        if not data:
            print('if not')
            break
        # connection.sendall(str.encode(jsonObjectString))
    connection.close()
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    thread1 = threading.Thread(target=multi_threaded_client, args=(Client,))

    thread1.start()
    #start_new_thread(multi_threaded_client, (Client, ))
    print('abc',Client)
   
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
ServerSideSocket.close()