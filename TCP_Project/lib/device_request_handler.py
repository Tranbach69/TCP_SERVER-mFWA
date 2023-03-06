from lib.device_err import handle_receive_error_data
from lib.device_err import handle_if_not_data
from lib.device_handle_flag_config import handle_flagConfig_0
from lib.device_handle_flag_config import handle_flagConfig_1
from lib.device_handle_flag_config import handle_flagConfig_2


def device_request_handler(conn, addr):
    global my_clients
    global my_all_clients
    global flag_config
    global deviceImeiCheck
    with conn:
        print(conn, addr)
        while True:
            try: 
                try:            
                    data = conn.recv(2048).decode('utf-8')
                    print("original data from Device: \n",data)
                except:
                    handle_receive_error_data(conn)
                    return
                if conn in my_all_clients:
                    print("client Already exists in my_all_client")
                else:
                    my_all_clients += [conn]
                if not data:
                    handle_if_not_data(conn)                   
                    break                          
                jsonObjectString=data.replace("'", '"')
                if "}{" in data :  
                    x=data.replace("}{","},{")
                    # print('sau khi thay thế "}{","},{": \n',x)
                    x="["+x+"]"
                    # print('sau khi thêm [ ] vào 2 đầu : \n',x)
                    z=json.loads(x)
                    for i in z:
                        if i['FlagConfig'] == 1:
                            conn.sendall("server receive success ".encode('utf-8'))
                            jsonObject=i
                            deviceIm=jsonObject['Imei']
                            print('config package + re-connect package.\n ')
                            handle_flagConfig_1(deviceIm,conn,jsonObject)
                        if i['FlagConfig'] == 3:
                            # conn.sendall("server receive success ".encode('utf-8'))
                            # jsonObject=i
                            # deviceIm=jsonObject['Imei']
                            # print('config package + re-connect package.\n ')
                            # handle_flagConfig_1(deviceIm,conn,jsonObject)
                            print("thông báo update ota ",i)
                            break                                 
                    continue                            
                try:
                    jsonObject=json.loads(jsonObjectString)
                    deviceIm=jsonObject['Imei']                  
                    if jsonObject['FlagConfig']==0:
                        handle_flagConfig_0(deviceIm,jsonObject,conn)
                    elif jsonObject['FlagConfig']==1:
                        handle_flagConfig_1(deviceIm,conn,jsonObject)                                
                    elif jsonObject['FlagConfig']==2:
                        handle_flagConfig_2(deviceIm,conn,jsonObject)
                    # elif jsonObject['FlagConfig']==3:
                    #     handle_flagConfig_3(deviceIm,conn,jsonObject)
                    else:
                        print("loi cu phap json") 
                except ValueError:  
                    print('Decoding JSON has failed trong hàm device connect.\n')
            except ConnectionAbortedError:
                return
        conn.close()