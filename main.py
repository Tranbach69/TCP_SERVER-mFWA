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

my_clients = [] 
flag_config=[]



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
    print(lte4gImeiList)
    print(' lte4gImei',lte4gImeiList)
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
    print(ethernetImeiList)
    print(' ethernetImei',ethernetImeiList)
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
    print(gpsImeiList)
    print(' gpsImei',gpsImeiList)
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


def device_request_handler(conn, addr):
    global my_clients
    global flag_config

    with conn:
        print(conn, addr)
        while True:
            try: 
                try:            
                    data = conn.recv(2048).decode('utf-8')
                    print("dđaa",data)
                except:
                    try:
                        print("error conn.recv") 
                        print('befor my_clients in recv \n',my_clients)                              
                        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
                        my_clients.remove(conn)
                        print('after my_clients in recv\n',my_clients)    
                    except :
                        print('error remove my_client in error conn.recv ')                   
                    conn.close()
                    return 
                # data = conn.recv(2048).decode('utf-8')
                if  not data:
                    print('client disconnect')  
                    print('befor my_clients\n',my_clients)
                    print('fileno',conn.fileno())
                    try:                               
                        my_clients.pop((my_clients.index(conn)+1))                                  # khi dũ liệu nhận được là "" đồng nghĩa với việc client hủy connect sẽ xóa client và số imei khỏi mảng   
                        my_clients.remove(conn)
                        print('after my_clients\n',my_clients) 
                    except :
                        print('error remove')                     
                    break
                print('\n',data)                             
                jsonObjectString=data.replace("'", '"')
                if "}{" in data :
                    x=data[data.rfind("}{"):]
                    y=x[1:]
                    print('xxxx',x)
                    
                    print('yyyy',y)
                    try:
                        jsonObject=json.loads(y)
                        deviceIm=jsonObject['Imei']
                        if jsonObject['FlagConfig']==0:
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
                                my_clients += [conn,jsonObject['Imei']]                                 # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
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
                        elif jsonObject['FlagConfig']==1:
                            if deviceIm in flag_config:                        
                                print("đã tồn tại gói tin cấu hình\n")
                            else:
                                print('chưa tồn tại gói tin cấu hình')
                                if "ChannelWifi1" in jsonObject:
                                    try:                     
                                        sqlUpdate='''UPDATE "Wifi"
                                            SET "ChannelWifi1"='%d',"ChannelModeWifi1"='%d'                     
                                            WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi1']),(jsonObject['ChannelModeWifi1']), (jsonObject['Imei']))
                                        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                                        print('update ChannelWifi1 and ChannelModeWifi1 of Wifi table success')                           
                                    except (Exception, psycopg2.Error) as error:
                                        print("Failed to update  ChannelWifi1 and ChannelModeWifi1 of Device table", error)
                                elif "ChannelWifi2" in jsonObject:
                                    try:                     
                                        sqlUpdate='''UPDATE "Wifi"
                                            SET "ChannelWifi2"='%d',"ChannelModeWifi2"='%d'                     
                                            WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi2']),(jsonObject['ChannelModeWifi2']), (jsonObject['Imei']))
                                        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                                        print('update ChannelWifi2 and ChannelModeWifi2 of Wifi table success')                           
                                    except (Exception, psycopg2.Error) as error:
                                        print("Failed to update  ChannelWifi2 and ChannelModeWifi2 of Device table", error)                                    
                                else:                              
                                    flag_config+=[deviceIm,jsonObject['Status']]
                        elif jsonObject['FlagConfig']==2:
                            if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
                                print('da ton tai deviceIm print in FlagConfig=2 \n')
                                print('befor my\n',my_clients)
                            else:
                                my_clients += [conn,jsonObject['Imei']]                                     # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
                                print('chua tôn tại \n')
                                print('befor lients\n',my_clients)
                        else:
                            print("loi cu phap jsonssss") 
                        return                                                  
                    except:
                        print('Decoding JSON has failed')
                        return
                try:
                    jsonObject=json.loads(jsonObjectString)
                    deviceIm=jsonObject['Imei']
                    if jsonObject['FlagConfig']==0:
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
                            my_clients += [conn,jsonObject['Imei']]                                 # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
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
                    elif jsonObject['FlagConfig']==1:
                        if deviceIm in flag_config:                        
                            print("đã tồn tại gói tin cấu hình\n")
                        else:
                            print('chưa tồn tại gói tin cấu hình')
                            if "ChannelWifi1" in jsonObject:
                                try:                     
                                    sqlUpdate='''UPDATE "Wifi"
                                        SET "ChannelWifi1"='%d',"ChannelModeWifi1"='%d'                     
                                        WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi1']),(jsonObject['ChannelModeWifi1']), (jsonObject['Imei']))
                                    cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                                    print('update ChannelWifi1 and ChannelModeWifi1 of Wifi table success')                           
                                except (Exception, psycopg2.Error) as error:
                                    print("Failed to update  ChannelWifi1 and ChannelModeWifi1 of Device table", error)
                            elif "ChannelWifi2" in jsonObject:
                                try:                     
                                    sqlUpdate='''UPDATE "Wifi"
                                        SET "ChannelWifi2"='%d',"ChannelModeWifi2"='%d'                     
                                        WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi2']),(jsonObject['ChannelModeWifi2']), (jsonObject['Imei']))
                                    cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                                    print('update ChannelWifi2 and ChannelModeWifi2 of Wifi table success')                           
                                except (Exception, psycopg2.Error) as error:
                                    print("Failed to update  ChannelWifi2 and ChannelModeWifi2 of Device table", error)                                    
                            else:                              
                                flag_config+=[deviceIm,jsonObject['Status']]
                    elif jsonObject['FlagConfig']==2:
                        if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
                            print('da ton tai deviceIm print in FlagConfig=2 \n')
                            print('befor my\n',my_clients)
                        else:
                            my_clients += [conn,jsonObject['Imei']]                                     # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
                            print('chua tôn tại \n')
                            print('befor lients\n',my_clients)
                    else:
                        print("loi cu phap json") 
                except ValueError:  
                    print('Decoding JSON has failed')
                try:         
                    conn.send("server receive success".encode('utf-8')) 
                except:
                    print('error send to client')
            except ConnectionAbortedError:
                return
        conn.close()
def be_request_handler(conn, addr):
    global my_clients                                                                               # khai báo biến toàn cục
    global flag_config
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
                    deviceIm=jsonObject['Imei']
                    if deviceIm in my_clients:                                                      # kiểm tra xem thiết bị có số imei được user cấu hình có tồn tại trong mảng chứa các client không
                        print('Thiết bị đang có kết nối\n')   
                        print('my_clients  print in  be request',my_clients)
                        try:
                                                              
                            my_clients[(my_clients.index(deviceIm)-1)].send(data.encode('utf-8'))       # có connect thì gửi dữ liệu về 
                            my_clients[(my_clients.index(deviceIm)-1)].close()  
                        except:
                            print("loiiiiiii")
                            my_clients[(my_clients.index(deviceIm)-1)].close()  
                        print("waiting feedback")
                        timeout = time.time() + 80                                                  #timeout 40s 
                        while True:  
                            test = 0                                       
                            if deviceIm in flag_config:                                                    
                                statusIndex=(flag_config.index(deviceIm)+1)
                                if flag_config[statusIndex]=="00":                                                              
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config Wifi Failure')
                                                                     
                                    conn.sendall("failure0".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="01":                                # cấu hình wifi thành công 
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config wifi success')
                                 
                                    conn.sendall("success0".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="10":                                                             
                                    flag_config.pop(statusIndex)
                                    print('config Lte4g Failure')
                                    flag_config.remove(deviceIm)
                                   
                                    conn.sendall("failure1".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="11":                                # cấu hình lte4g thành công  
                                    flag_config.pop(statusIndex)
                                    print('config Lte4g success')
                                    flag_config.remove(deviceIm)
                                
                                    conn.sendall("success1".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="20":                                                             
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config Ethernet Failure') 
                                                               
                                    conn.sendall("failure2".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="21":                                # cấu hình ethernet thành công  
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config Ethernet success')
                                   
                                    conn.sendall("success2".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="30":                                                             
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config Gps Failure') 
                                                             
                                    conn.sendall("failure3".encode('utf-8'))
                                    break
                                elif flag_config[statusIndex]=="31":                                # cấu hình gps thành công 
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                    print('config Gps success')   
                                                                   
                                    conn.sendall("success3".encode('utf-8'))
                                    break                            
                                else:
                                    flag_config.pop(statusIndex)
                                    flag_config.remove(deviceIm)
                                 
                                    conn.sendall("failure".encode('utf-8'))
                                    break                            
                            if time.time() > timeout:
                                conn.sendall("failure".encode('utf-8'))
                                print('timeout 80s')
                              
                                break
                            test = test - 1  
                        conn.close()  
                        return                                                                
                    else:
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
                        connectionSql.commit()                                                      # commit data base
                except ValueError:                                                                  # lỗi khi convert sang json object
                    print('Decoding JSON has failed')
                    conn.sendall("Decoding JSON has failed".encode('utf-8')) 
                                            
                if not data:                                                                        # BE disconnect thì sẽ break và end thread 
                    print('client disconnect')
                    break                                              
            except ConnectionAbortedError:
                conn.close()
                return False 
        conn.close()
                   
def back_end_requets():

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

def device_requets():

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
    threading.Thread(target=back_end_requets, args=()).start()          # thread cho BE
    threading.Thread(target=device_requets, args=()).start()            # thread cho device


if __name__ == '__main__':                      # thread chính
    main()




#     connectionSql = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#             "Server=LAPTOP-ID8TN73Q;"
#             "Database=DATN;"
#             "UID=sa;"
#             "PWD=1234;")
