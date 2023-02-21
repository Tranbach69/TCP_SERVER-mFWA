import socket
import threading
import json
import time
from datetime import datetime
import psycopg2

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

flag_config=[]
deviceImeiCheck=[]

def handle_wifi_data(jsonObject):
    """The function has the main function is to process the Wifi data received
        from the device and update it into the database.

    Args:
        jsonObject (json Object): a Json object received from the device that includes information about Wifi
    """
    sqlGetWifiImei='''SELECT "Imei" FROM "Wifi" '''
    cursor.execute(sqlGetWifiImei)
    wifiImeiList=cursor.fetchall()
    wifiImei=(jsonObject['Imei'],) 
    if wifiImei in wifiImeiList:
        
        try:                     
            sqlUpdate='''UPDATE "Wifi"
                SET "WifiOpen"='%d',"WifiMode"='%d',"CurrentAp"='%d',"WifiNat"='%d',
                    "SsidWifi1"='%s',"AuthTypeWifi1"='%d',"EncryptModeWifi1"='%d',"AuthPwdWifi1"='%s',"ClientCountWifi1"='%d',"BroadCastWifi1"='%d',"IsolationWifi1"='%d',"MacAddressWifi1"='%s',"ChannelModeWifi1"='%d',"ChannelWifi1"='%d',"DhcpHostIpWifi1"='%s',"DhcpStartIpWifi1"='%s',"DhcpEndIpWifi1"='%s',"DhcpTimeWifi1"='%s',
                    "SsidWifi2"='%s',"AuthTypeWifi2"='%d',"EncryptModeWifi2"='%d',"AuthPwdWifi2"='%s',"ClientCountWifi2"='%d',"BroadCastWifi2"='%d',"IsolationWifi2"='%d',"MacAddressWifi2"='%s',"ChannelModeWifi2"='%d',"ChannelWifi2"='%d',"DhcpHostIpWifi2"='%s',"DhcpStartIpWifi2"='%s',"DhcpEndIpWifi2"='%s',"DhcpTimeWifi2"='%s',
                    "StaIp"='%s',"StaSsidExt"='%s',"StaSecurity"='%d',"StaProtocol"='%d',"StaPassword"='%s',"TimingUpdate"='%s'
                WHERE "Imei"= '%s'  '''%((jsonObject['WifiOpen']),(jsonObject['WifiMode']),(jsonObject['CurrentAp']),(jsonObject['WifiNat']),(jsonObject['SsidWifi1']),(jsonObject['AuthTypeWifi1']),(jsonObject['EncryptModeWifi1']),(jsonObject['AuthPwdWifi1']),(jsonObject['ClientCountWifi1']),(jsonObject['BroadCastWifi1']),(jsonObject['IsolationWifi1']),(jsonObject['MacAddressWifi1']),(jsonObject['ChannelModeWifi1']),(jsonObject['ChannelWifi1']),(jsonObject['DhcpHostIpWifi1']),(jsonObject['DhcpStartIpWifi1']),(jsonObject['DhcpEndIpWifi1']),(jsonObject['DhcpTimeWifi1']),(jsonObject['SsidWifi2']),(jsonObject['AuthTypeWifi2']),(jsonObject['EncryptModeWifi2']),(jsonObject['AuthPwdWifi2']),(jsonObject['ClientCountWifi2']),(jsonObject['BroadCastWifi2']),(jsonObject['IsolationWifi2']),(jsonObject['MacAddressWifi2']),(jsonObject['ChannelModeWifi2']),(jsonObject['ChannelWifi2']),(jsonObject['DhcpHostIpWifi2']),(jsonObject['DhcpStartIpWifi2']),(jsonObject['DhcpEndIpWifi2']),(jsonObject['DhcpTimeWifi2']),(jsonObject['StaIp']),(jsonObject['StaSsidExt']),(jsonObject['StaSecurity']),(jsonObject['StaProtocol']),(jsonObject['StaPassword']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(jsonObject['Imei']))
            cursor.execute(sqlUpdate)
            print('update Wifi success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to update  Wifi table", error)
    else:
        print("bbbbbbbbbb")  
        try:                
            sqlInsertInto='''INSERT INTO "Wifi"
                VALUES ('%s',%d,%d,%d,%d,
                '%s','%d','%d','%s','%d','%d','%d','%s','%d','%d','%s','%s','%s','%s',
                '%s','%d','%d','%s','%d','%d','%d','%s','%d','%d','%s','%s','%s','%s',
                '%s','%s','%d','%d','%s',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00')
                '''%((jsonObject['Imei']),(jsonObject['WifiOpen']),(jsonObject['WifiMode']),(jsonObject['CurrentAp']),(jsonObject['WifiNat']),(jsonObject['SsidWifi1']),(jsonObject['AuthTypeWifi1']),(jsonObject['EncryptModeWifi1']),(jsonObject['AuthPwdWifi1']),(jsonObject['ClientCountWifi1']),(jsonObject['BroadCastWifi1']),(jsonObject['IsolationWifi1']),(jsonObject['MacAddressWifi1']),(jsonObject['ChannelModeWifi1']),(jsonObject['ChannelWifi1']),(jsonObject['DhcpHostIpWifi1']),(jsonObject['DhcpStartIpWifi1']),(jsonObject['DhcpEndIpWifi1']),(jsonObject['DhcpTimeWifi1']),(jsonObject['SsidWifi2']),(jsonObject['AuthTypeWifi2']),(jsonObject['EncryptModeWifi2']),(jsonObject['AuthPwdWifi2']),(jsonObject['ClientCountWifi2']),(jsonObject['BroadCastWifi2']),(jsonObject['IsolationWifi2']),(jsonObject['MacAddressWifi2']),(jsonObject['ChannelModeWifi2']),(jsonObject['ChannelWifi2']),(jsonObject['DhcpHostIpWifi2']),(jsonObject['DhcpStartIpWifi2']),(jsonObject['DhcpEndIpWifi2']),(jsonObject['DhcpTimeWifi2']),(jsonObject['StaIp']),(jsonObject['StaSsidExt']),(jsonObject['StaSecurity']),(jsonObject['StaProtocol']),(jsonObject['StaPassword']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            cursor.execute(sqlInsertInto)
            print('insert into Wifi success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Wifi table", error)
    connectionSql.commit()

def handle_lte4g_data(jsonObject):
    """The function has the main function is to process the Lte4g data received
        from the device and update it into the database.

    Args:
        jsonObject (json Object): a Json object received from the device that includes information about Lte4g
    """
        
    sqlGetLte4gImei='''SELECT "Imei" FROM "Lte4g" '''
    cursor.execute(sqlGetLte4gImei)
    lte4gImeiList=cursor.fetchall()
    lte4gImei=(jsonObject['Imei'],)
    if lte4gImei in lte4gImeiList:
        try:                     
            sqlUpdate='''UPDATE "Lte4g"
                SET "CardStatus"='%d',"AppType"='%d',"AppState"='%d',"Pin"='%d',"SimIccid"='%s',"SimImsi"='%s',"SystemMode"='%s',"OperationMode"='%s',"MobileCountryCode"='%s',"MobileNetworkCode"='%s',"LocationAreaCode"='%s',"ServiceCellId"='%s',"FreqBand"='%s',"Current4GData"='%s',"Afrcn"='%s',"PhoneNumber"='%s',"Rssi4G"='%d',"NetworkMode"='%d',"TimingUpdate"='%s'
                WHERE "Imei"= '%s'  '''%((jsonObject['CardStatus']),(jsonObject['AppType']),(jsonObject['AppState']),(jsonObject['Pin']),(jsonObject['SimIccid']),(jsonObject['SimImsi']),(jsonObject['SystemMode']),(jsonObject['OperationMode']),(jsonObject['MobileCountryCode']),(jsonObject['MobileNetworkCode']),(jsonObject['LocationAreaCode']),(jsonObject['ServiceCellId']),(jsonObject['FreqBand']),(jsonObject['Current4GData']),(jsonObject['Afrcn']),(jsonObject['PhoneNumber']),(jsonObject['Rssi4G']),(jsonObject['NetworkMode']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(jsonObject['Imei']))
            cursor.execute(sqlUpdate)
            print('update Lte4g success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to update Lte4g table", error)
    else:
        try:                
            sqlInsertInto='''INSERT INTO "Lte4g"
                VALUES ('%s','%d','%d','%d','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%d','%d',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00')
                '''%((jsonObject['Imei']),(jsonObject['CardStatus']),(jsonObject['AppType']),(jsonObject['AppState']),(jsonObject['Pin']),(jsonObject['SimIccid']),(jsonObject['SimImsi']),(jsonObject['SystemMode']),(jsonObject['OperationMode']),(jsonObject['MobileCountryCode']),(jsonObject['MobileNetworkCode']),(jsonObject['LocationAreaCode']),(jsonObject['ServiceCellId']),(jsonObject['FreqBand']),(jsonObject['Current4GData']),(jsonObject['Afrcn']),(jsonObject['PhoneNumber']),(jsonObject['Rssi4G']),(jsonObject['NetworkMode']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            cursor.execute(sqlInsertInto)
            print('insert into Lte4g success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Lte4g table", error)
    connectionSql.commit()
    
def handle_ethernet_data(jsonObject):
    """The function has the main function is to process the Ethernet data received
        from the device and update it into the database.

    Args:
        jsonObject (json Object): a Json object received from the device that includes information about Ethernet
    """
    sqlGetEthernetImei='''SELECT "Imei" FROM "Ethernet" '''
    cursor.execute(sqlGetEthernetImei)
    ethernetImeiList=cursor.fetchall()
    ethernetImei=(jsonObject['Imei'],)
    if ethernetImei in ethernetImeiList:
        try:                     
            sqlUpdate='''UPDATE "Ethernet"
                SET "DriverType"='%d',"DriverEn"='%d',"BringUpdownEn"='%d',"IpStaticEn"='%d',"IpAddr"='%s',"Netmask"='%s',"TimingUpdate"='%s'
                WHERE "Imei"= '%s'  '''%((jsonObject['DriverType']),(jsonObject['DriverEn']),(jsonObject['BringUpdownEn']),(jsonObject['IpStaticEn']),(jsonObject['IpAddr']),(jsonObject['Netmask']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(jsonObject['Imei']))
            cursor.execute(sqlUpdate)
            print('update Ethernet success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to update  Ethernet table", error)
    else:
        try:                
            sqlInsertInto='''INSERT INTO "Ethernet"
                VALUES ('%s','%d','%d','%d','%d','%s','%s',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00')
                '''%((jsonObject['Imei']),(jsonObject['DriverType']),(jsonObject['DriverEn']),(jsonObject['BringUpdownEn']),(jsonObject['IpStaticEn']),(jsonObject['IpAddr']),(jsonObject['Netmask']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            cursor.execute(sqlInsertInto)
            print('insert into Ethernet success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Ethernet table", error)
    connectionSql.commit()
    
def handle_gps_data(jsonObject):
    """The function has the main function is to process the Gps data received
        from the device and update it into the database.

    Args:
        jsonObject (json Object): a Json object received from the device that includes information about Gps
    """
    sqlGetGpsImei='''SELECT "Imei" FROM "Gps" '''
    cursor.execute(sqlGetGpsImei)
    gpsImeiList=cursor.fetchall()
    gpsImei=(jsonObject['Imei'],)
    if gpsImei in gpsImeiList:
        try:                     
            sqlUpdate='''UPDATE "Gps"
                SET "Latitude"='%ls',"Longitude"='%ls',"Altitude"='%ls',"Speed"='%f',"Bearing"='%f',"Accuracy"='%f',"Time"='%s',"TimingUpdate"='%s'
                WHERE "Imei"= '%s'  '''%((jsonObject['Latitude']),(jsonObject['Longitude']),(jsonObject['Altitude']),(jsonObject['Speed']),(jsonObject['Bearing']),(jsonObject['Accuracy']),(jsonObject['Time']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(jsonObject['Imei']))
            cursor.execute(sqlUpdate)
            print('update Gps success')
            
        except (Exception, psycopg2.Error) as error:
            print("Failed to update  Gps table", error)
    else:
        try:                
            sqlInsertInto='''INSERT INTO "Gps"
                VALUES ('%s','%f','%f','%f','%f','%f','%f','%s',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00')
                '''%((jsonObject['Imei']),(jsonObject['Latitude']),(jsonObject['Longitude']),(jsonObject['Altitude']),(jsonObject['Speed']),(jsonObject['Bearing']),(jsonObject['Accuracy']),(jsonObject['Time']),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
            cursor.execute(sqlInsertInto)
            print('insert into Gps success')
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into Gps table", error)
    connectionSql.commit()

def handle_receive_error_data(conn):
    global my_clients
    global my_all_clients
    try:
        print("error when receiving data (conn.recv)\n") 
        print('before my_clients print in error conn.recv \n',my_clients)                              
        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        my_clients.remove(conn) 
        my_all_clients.remove(conn)
        print('after my_clients in recv\n',my_clients)    
    except :
        print('error remove my_client in error conn.recv\n ')                   
    conn.close()   

def handle_if_not_data(conn):
    global my_clients
    global my_all_clients
    print('client disconnect\n')  
    print('before my_clients print if not data\n',my_clients)
    try:                               
        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        my_clients.remove(conn)
        my_all_clients.remove(conn)
        print('after my_clients\n',my_clients) 
        print('after my_all_clients\n',my_all_clients) 
    except :
        print('error remove my_client in if not data\n ') 

def handle_remove_imei_in_check_device_imei(deviceIm):
    global deviceImeiCheck
    try:  
        print('before deviceImeiCheck\n',deviceImeiCheck)                                                               # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
        deviceImeiCheck.remove(deviceIm)
        print('after deviceImeiCheck\n',deviceImeiCheck) 
    except :
        print('error remove deviceImeiCheck \n ') 

def handle_flagConfig_0(deviceIm,jsonObject,conn):
    global my_clients
    handle_remove_imei_in_check_device_imei(deviceIm)
    try:                     
        sqlUpdate='''UPDATE "Device"
            SET "SocketConnection"='1'                      
            WHERE "Imei"= '%s'  '''%(deviceIm)
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
        print('update SocketConnection:1 of Device table success')
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to update  SocketConnection:1 of Device table", error)
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưa
        print('da co\n')
    else:
        my_clients += [conn,jsonObject['Imei']] 
        print('chua co \n')
    print(jsonObject)  
    if jsonObject['Index']==0:                                                  # index=0 có nghĩa là gói tin của wifi và sẽ xử lý trong hàm handle_wifi_data
        handle_wifi_data(jsonObject)
    elif jsonObject['Index']==1:                     
        handle_lte4g_data(jsonObject)
    elif jsonObject['Index']==2:
        handle_ethernet_data(jsonObject)
    elif jsonObject['Index']==3:
        handle_gps_data(jsonObject)
    else:
        print('invalid index')   

def handle_flagConfig_1(deviceIm,conn,jsonObject):
    global my_clients
    global flag_config                                 # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
    print('print in handle_flagConfig_1 \n')
    # print('befor lients\n',my_clients) 
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
        print('da ton tai deviceIm print in handle_flagConfig_1 \n')
    else:
        my_clients += [conn,deviceIm] 
                                   
        # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
        print('chua tồn tại trong mảng  print in  handle_flagConfig_1 \n')
    if deviceIm in flag_config:                        
        print("đã tồn tại gói tin cấu hình\n")
    else:
        print('chưa tồn tại gói tin cấu hình')                           
        if "ChannelWifi1" in jsonObject:                             
            try:    
                flag_config+=[deviceIm,jsonObject['Status']]                                                 
                sqlUpdate='''UPDATE "Wifi"
                    SET "ChannelWifi1"='%d',"ChannelModeWifi1"='%d'                     
                    WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi1']),(jsonObject['ChannelModeWifi1']), (jsonObject['Imei']))
                cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
                print('update ChannelWifi1 and ChannelModeWifi1 of Wifi table success')                           
            except (Exception, psycopg2.Error) as error:
                print("Failed to update  ChannelWifi1 and ChannelModeWifi1 of Device table", error)
            connectionSql.commit()
        elif "ChannelWifi2" in jsonObject :
            flag_config+=[deviceIm,jsonObject['Status']]
            try:                     
                sqlUpdate='''UPDATE "Wifi"
                    SET "ChannelWifi2"='%d',"ChannelModeWifi2"='%d'                     
                    WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi2']),(jsonObject['ChannelModeWifi2']), (jsonObject['Imei']))
                cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                print('update ChannelWifi2 and ChannelModeWifi2 of Wifi table success')                           
            except (Exception, psycopg2.Error) as error:
                print("Failed to update  ChannelWifi2 and ChannelModeWifi2 of Device table", error)
            connectionSql.commit()
        else:
            flag_config+=[deviceIm,jsonObject['Status']] 
    handle_remove_imei_in_check_device_imei(deviceIm)
       

def handle_flagConfig_2(deviceIm,conn,jsonObject):
    global my_clients

    handle_remove_imei_in_check_device_imei(deviceIm)
    print('gói tin re-connect print in handle_flagConfig_2\n ')
    try:                                                    
        sqlUpdate='''UPDATE "Device"
            SET "UpTime"='%s'                    
            WHERE "Imei"= '%s'  '''%((jsonObject['UpTime']), (jsonObject['Imei']))
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
        print('update UpTime  of Device table success') 
        connectionSql.commit()                          
    except (Exception, psycopg2.Error) as error:
        print("Failed to update UpTime  of Device table", error)
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
        print('da ton tai deviceIm print in handle_flagConfig_2=2 \n')
    else:
        my_clients += [conn,deviceIm]                   
        print('chua tồn tại trong mảng  print in  handle_flagConfig_2 \n')    

# def handle_flagConfig_3(deviceIm,conn,jsonObject):
#     global my_clients
#     handle_remove_imei_in_check_device_imei(deviceIm)
#     print('gói tin ping\n ') 
#     try:                                                    
#         sqlUpdate='''UPDATE "Device"
#             SET "UpTime"='%s'                    
#             WHERE "Imei"= '%s'  '''%((jsonObject['UpTime']), (jsonObject['Imei']))
#         cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
#         print('update UpTime  of Device table success') 
#         connectionSql.commit()                          
#     except (Exception, psycopg2.Error) as error:
#         print("Failed to update UpTime  of Device table", error)
#     if "ClientCountWifi1" in jsonObject:
#         try:                                                    
#             sqlUpdate='''UPDATE "Wifi"
#                 SET "ClientCountWifi1"='%d',"MacAddressWifi1"='%s'                 
#                 WHERE "Imei"= '%s'  '''%((jsonObject['ClientCountWifi1']),(jsonObject['MacAddressWifi1']), (deviceIm))
#             cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
#             print('update ClientCountWifi1 and MacAddressWifi1  of Wifi table success') 
#             connectionSql.commit()                          
#         except (Exception, psycopg2.Error) as error:
#             print("Failed to update ClientCountWifi1 and MacAddressWifi1  of Wifi table", error)
#     if "ClientCountWifi2" in jsonObject:
#         try:                                                    
#             sqlUpdate='''UPDATE "Wifi"
#                 SET "ClientCountWifi2"='%d',"MacAddressWifi2"='%s'                 
#                 WHERE "Imei"= '%s'  '''%((jsonObject['ClientCountWifi2']),(jsonObject['MacAddressWifi2']), (deviceIm))
#             cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
#             print('update ClientCountWifi2 and MacAddressWifi2  of Wifi table success') 
#             connectionSql.commit()                          
#         except (Exception, psycopg2.Error) as error:
#             print("Failed to update ClientCountWifi2 and MacAddressWifi2  of Wifi table", error)
#     if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
#         print('da ton tai deviceIm print in CheckConnection \n')
#     else:
#         my_clients += [conn,deviceIm]                                     # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
#         print('chua tôn tại \n')
#         print('after add my_clients in CheckConnection\n',my_clients)
    

def device_request_handler(conn, addr):
    global my_clients
    global my_all_clients
    global flag_config
    global deviceImeiCheck
    with conn:
        print(conn, addr)
        if conn in my_all_clients:
            print("client đã tồn tại trong my_all_client")
        else:
            my_all_clients += [conn]
        while True:
            try: 
                try:            
                    data = conn.recv(2048).decode('utf-8')
                    print("original data: \n",data)
                except:
                    handle_receive_error_data(conn)
                    return
                if not data:
                    handle_if_not_data(conn)                   
                    break                          
                jsonObjectString=data.replace("'", '"')
                if "}{" in data :  
                    x=data.replace("}{","},{")
                    print('sau khi thay thế "}{","},{": \n',x)
                    x="["+x+"]"
                    print('sau khi thêm [ ] vào 2 đầu : \n',x)
                    z=json.loads(x)
                    for i in z:
                        if i['FlagConfig'] == 1:
                            conn.sendall("server receive success ".encode('utf-8'))
                            jsonObject=i
                            deviceIm=jsonObject['Imei']
                            print('gói tin config + gói tin re-connect\n ')
                            handle_flagConfig_1(deviceIm,conn,jsonObject)
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
                    print('Decoding JSON has failed trong hàm device connect')
            except ConnectionAbortedError:
                return
        conn.close()
        
def handle_feedback_config(conn,statusIndex,deviceIm,message):
    global flag_config
    flag_config.pop(statusIndex)
    flag_config.remove(deviceIm)
    conn.sendall(message.encode('utf-8'))   

def handle_device_disconnect (conn,deviceIm):
    print('thiết bị mất kết nối \n')
    conn.sendall("failure".encode('utf-8'))  
    try:                                                                        # không tồn tại thì có nghĩa là thiết bị đang mất kết nối với server
        sqlUpdate='''UPDATE "Device"
            SET "SocketConnection"='0'
            WHERE "Imei"= '%s'  '''%(deviceIm)
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái lên server
        print('update SocketConnection:0 of Device table success')                          
    except (Exception, psycopg2.Error) as error:                        
        print("Failed to update  SocketConnection:0 of Device table", error)      # in ra lỗi nếu xảy ra khi cập nhật data base           
    connectionSql.commit() 

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
                print(data) 
                      
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
                                print("error when handle sendAll client")
                                try:
                                    print("trc khi xóa  my all client \n ")
        
                                    my_all_clients.remove(client)
                                    print("xóa thành công my all client \n ")
                                except:
                                    print("lỗi khi xóa client trong khi gửi lỗi")
                        return
                    deviceIm=jsonObject['Imei']
                    if deviceIm in deviceImeiCheck:
                        print('thiết bị đang bận')
                        conn.sendall("failure99".encode('utf-8'))
                    else:
                        print('thiết bị đang rảnh')
                        if deviceIm in my_clients:                                                      # kiểm tra xem thiết bị có số imei được user cấu hình có tồn tại trong mảng chứa các client không
                            print('Thiết bị đang có kết nối\n')   
                            print('my_clients  print in  be request',my_clients)
                            try:                             
                                ret=my_clients[(my_clients.index(deviceIm)-1)].sendall(data.encode('utf-8'))       # có connect thì gửi dữ liệu về 
                                print("ret: ",ret)
                                deviceImeiCheck+=[deviceIm]
                                my_clients[(my_clients.index(deviceIm)-1)].close()  
                            except :
                                print("error when sendall to device")
                                my_clients[(my_clients.index(deviceIm)-1)].close()
                                conn.sendall("failure".encode('utf-8'))
                                return
                            print("waiting feedback")
                            timeout = time.time() + 30                                                #timeout 40s 
                            while True:  
                                test = 0                                       
                                if deviceIm in flag_config:                                                    
                                    statusIndex=(flag_config.index(deviceIm)+1)
                                    if flag_config[statusIndex]=="00":                                                              
                                        print('config Wifi Failure')                                
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure0")
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break
                                    elif flag_config[statusIndex]=="01":                                # cấu hình wifi thành công 
                                        print('config wifi success')
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success0")
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break
                                    elif flag_config[statusIndex]=="10":   
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure1") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                         
                                        print('config Lte4g Failure')
                                        break
                                    elif flag_config[statusIndex]=="11":  
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success1")# cấu hình lte4g thành công 
                                        handle_remove_imei_in_check_device_imei(deviceIm) 
                                        print('config Lte4g success')
                                        break
                                    elif flag_config[statusIndex]=="20":    
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure2") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                        
                                        print('config Ethernet Failure')                                                                
                                        break
                                    elif flag_config[statusIndex]=="21":                                # cấu hình ethernet thành công  
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success2")  
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        print('config Ethernet success')                                   
                                        break
                                    elif flag_config[statusIndex]=="30": 
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure3")  
                                        handle_remove_imei_in_check_device_imei(deviceIm)                                                           
                                        print('config Gps Failure')                                                             
                                        break
                                    elif flag_config[statusIndex]=="31":                                # cấu hình gps thành công 
                                        handle_feedback_config(conn,statusIndex,deviceIm,"success3") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        print('config Gps success')                                                                      
                                        break                            
                                    else:
                                        handle_feedback_config(conn,statusIndex,deviceIm,"failure") 
                                        handle_remove_imei_in_check_device_imei(deviceIm)
                                        break                            
                                if time.time() > timeout:
                                    conn.sendall("failure".encode('utf-8'))
                                    print('timeout 30s')
                                    handle_remove_imei_in_check_device_imei(deviceIm) 
                                    break
                                test = test - 1  
                            conn.close()  
                            return                                                                
                        else:
                            handle_device_disconnect (conn,deviceIm)                                # commit data base
                except ValueError:                                                                  # lỗi khi convert sang json object
                    print('Decoding JSON has failed trong hàm backend request')
                    conn.sendall("Decoding JSON has failed".encode('utf-8')) 
                              
                if not data:                                                                        # BE disconnect thì sẽ break và end thread 
                    print('client BE disconnect')
                    break                                              
            except ConnectionAbortedError:
                conn.close()
                return False 
        conn.close()
                   
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




#     connectionSql = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#             "Server=LAPTOP-ID8TN73Q;"
#             "Database=DATN;"
#             "UID=sa;"
#             "PWD=1234;")
# Uptime để trong gói re-connect bỏ flag config 3