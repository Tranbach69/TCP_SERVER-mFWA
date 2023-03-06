from lib.device_err import handle_remove_imei_in_check_device_imei
import lib.handle_device_disconnect
def handle_feedback_config(conn,statusIndex,deviceIm,message):
    global flag_config
    flag_config.pop(statusIndex)
    flag_config.remove(deviceIm)
    conn.sendall(message.encode('utf-8'))
    
def be_request_handler(conn, addr):
    global my_clients  
    global my_all_clients                                                                               # khai báo biến toàn cục
    global flag_config
    global deviceImeiCheck
    with conn:
        print(conn, addr)
        while True:
            try:
                try:            
                    data = conn.recv(2048).decode('utf-8')
                except:                  
                    return                                              # nhận dữ liệu từ BE
                print("data receive from Back-End:\n",data) 
                      
                jsonObjectString=data.replace("'", '"')                                             # thay thế " --> '  
                try:
                    jsonObject=json.loads(jsonObjectString)                                         # convert sang json object
                    if jsonObject['Index']==4:
                        print('my client all',my_all_clients)
                        for client in my_all_clients:
                            try:
                                
                                client.sendall(data.encode('utf-8'))
                                client.close()
                            except:
                                print("\n error when sendAll(updateOta) client.\n")
                                try:
                                    # print("trc khi xóa  my all client \n ")
        
                                    my_all_clients.remove(client)
                                    print("xóa thành công my all client \n ")
                                except:
                                    print("Error when deleting each client of my_all_client.\n")
                        print('\n my client all\n ',my_all_clients)
                        
                        return
                    deviceIm=jsonObject['Imei']
                    if deviceIm in deviceImeiCheck:
                        print('Device busy.\n')
                        conn.sendall("failure99".encode('utf-8'))
                    else:
                        print('Device is idle\n')
                        if deviceIm in my_clients:                                                      # kiểm tra xem thiết bị có số imei được user cấu hình có tồn tại trong mảng chứa các client không
                            print('Device is currently connected.\n')   
                            # print('my_clients  print in  be request.\n',my_clients)
                            try:                             
                                ret=my_clients[(my_clients.index(deviceIm)-1)].sendall(data.encode('utf-8'))       # có connect thì gửi dữ liệu về 
                                print("ret: ",ret)
                                deviceImeiCheck+=[deviceIm]
                                my_clients[(my_clients.index(deviceIm)-1)].close()  
                            except :
                                print("error when sendall(Configution) to device.\n")
                                my_clients[(my_clients.index(deviceIm)-1)].close()
                                conn.sendall("failure".encode('utf-8'))
                                return
                            print("waiting feedback.\n")
                            timeout = time.time() + 30                                                #timeout 30s 
                            while True:  
                                test = 0                                       
                                if deviceIm in flag_config:                                                    
                                    statusIndex=(flag_config.index(deviceIm)+1)
                                    if flag_config[statusIndex]=="00":                                                              
                                        print('config Wifi Failure.\n')                                
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure0")
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break
                                    elif flag_config[statusIndex]=="01":                                # cấu hình wifi thành công 
                                        print('config wifi success.\n')
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success0")
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break
                                    elif flag_config[statusIndex]=="10":   
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure1") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                         
                                        print('config Lte4g Failure.\n')
                                        break
                                    elif flag_config[statusIndex]=="11":  
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success1")# cấu hình lte4g thành công 
                                        handle_remove_imei_in_check_device_imei(deviceIm) 
                                        print('config Lte4g success.\n')
                                        break
                                    elif flag_config[statusIndex]=="20":    
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure2") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                        
                                        print('config Ethernet Failure.\n')                                                                
                                        break
                                    elif flag_config[statusIndex]=="21":                                # cấu hình ethernet thành công  
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success2")  
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        print('config Ethernet success.\n')                                   
                                        break
                                    elif flag_config[statusIndex]=="30": 
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure3")  
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                           
                                        print('config Gps Failure.\n')                                                             
                                        break
                                    elif flag_config[statusIndex]=="31":                                # cấu hình gps thành công 
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success3") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        print('config Gps success.\n')                                                                      
                                        break                            
                                    else:
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break                            
                                if time.time() > timeout:
                                    conn.sendall("failure".encode('utf-8'))
                                    print('timeout 30s.\n')
                                    handle_remove_imei_in_check_device_imei(deviceIm) 
                                    break
                                test = test - 1  
                            conn.close()  
                            return                                                                
                        else:
                            handle_device_disconnect (conn,deviceIm)                                # commit data base
                except ValueError:                                                                  # lỗi khi convert sang json object
                    print('Decoding JSON has failed trong hàm backend request.\n')
                    conn.sendall("Decoding JSON has failed".encode('utf-8')) 
                              
                if not data:                                                                        # BE disconnect thì sẽ break và end thread 
                    print('client BE disconnect.\n')
                    break                                              
            except ConnectionAbortedError:
                conn.close()
                return False 
        conn.close()
 