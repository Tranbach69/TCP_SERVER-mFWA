import socket
import threading
import json
import time
from datetime import datetime
import psycopg2
from lib.be_request_handler import be_request_handler
from lib.device_request_handler import device_request_handler


try:
    connectionSql = psycopg2.connect(user="postgres",


                                  password="1",
                                  host="localhost",
                                  port="5432",
                                  database="DATN")
    cursor = connectionSql.cursor()
except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into AccountAdmin table", error)

my_clients = []                             # mảng chứa client và imei
my_all_clients = []                         # mảng chứa tất cả các client 
flag_config=[]                              # mảng chứa trạng thái cấu hình của 
deviceImeiCheck=[]

def back_end_request():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:                                    # tạo đối tượng socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)             
        s.bind(('0.0.0.0', 3023))                                           
        s.listen()
        print('Server For BE is listening')
        while True:
            conn, addr = s.accept()         
            print('Connected with', addr[0], ':', str(addr[1]))
            threading.Thread(target=be_request_handler, args=(conn, addr)).start()                  # tạo thread khi có connect
        s.close()       

def device_request():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 3022))
        s.listen()
        print('Server For Device is listening')
        while True:
            conn, addr = s.accept()      
            print('Connected with', addr[0], ':', str(addr[1]))
            threading.Thread(target=device_request_handler, args=(conn, addr)).start() 
        s.close()   
         

def main():
    threading.Thread(target=back_end_request, args=()).start()          # thread cho BE
    threading.Thread(target=device_request, args=()).start()            # thread cho device


if __name__ == '__main__':                      # thread chính
    main()

