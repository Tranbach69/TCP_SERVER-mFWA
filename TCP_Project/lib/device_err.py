def handle_receive_error_data(conn):
    global my_clients
    global my_all_clients
    try:
        # print("error when receiving data (conn.recv) my_clientmy_clientmy_clientmy_clientmy_clientmy_clientmy_client\n") 
        # print('before my_clients print in error conn.recv \n',my_clients)                              
        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        my_clients.remove(conn) 
        # print('after my_clients in recv\n',my_clients)    
    except :
        print('error remove my_client in handle_receive_error_data\n ')     
    try:
        # print("error when receiving data (conn.recv) my_all_clientmy_all_clientmy_all_clientmy_all_clientmy_all_client\n") 
        my_all_clients.remove(conn)
        # print('after my_clients in recv\n',my_clients)    
    except :
        print('error remove my_all_client in handle_receive_error_data\n ')               
    conn.close()   

def handle_if_not_data(conn):
    global my_clients
    global my_all_clients
    print('client disconnect\n')  
    # print('before my_clients print if not data\n',my_clients)
    try:                               
        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        my_clients.remove(conn)
        # print('after my_clients\n',my_clients) 
    except :
        print('error remove my_client in if not data\n ') 
    try:
        # print("if not data my_all_client\n") 
        my_all_clients.remove(conn)
        # print('after my_clients in recv\n',my_clients)    
    except :
        print('error remove my_all_client in error conn.recv\n ')

def handle_remove_imei_in_check_device_imei(deviceIm):
    global deviceImeiCheck
    try:  
        # print('before deviceImeiCheck\n',deviceImeiCheck)                                                               # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        deviceImeiCheck.remove(deviceIm)
        # print('after deviceImeiCheck\n',deviceImeiCheck) 
    except :
        print('error remove deviceImeiCheck \n ')