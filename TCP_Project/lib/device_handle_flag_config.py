from lib.device_err import handle_remove_imei_in_check_device_imei
from lib.device_data import handle_wifi_data
from lib.device_data import handle_lte4g_data
from lib.device_data import handle_ethernet_data
from lib.device_data import handle_gps_data



def handle_flagConfig_0(deviceIm,jsonObject,conn):
    global my_clients
    handle_remove_imei_in_check_device_imei(deviceIm)
    try:                     
        sqlUpdate='''UPDATE "Device"
            SET "SocketConnection"='1'                      
            WHERE "Imei"= '%s'  '''%(deviceIm)
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
        print('update SocketConnection:1 of Device table success.\n')
        
    except (Exception, psycopg2.Error) as error:
        print("Failed to update  SocketConnection:1 of Device table.\n", error)
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưa
        print('Already exists.  \n')
    else:
        my_clients += [conn,jsonObject['Imei']] 
        print('Does not exist. \n')
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
        print('invalid index.\n')   

def handle_flagConfig_1(deviceIm,conn,jsonObject):
    global my_clients
    global flag_config                                 # chưa tồn tại thì thêm mới vào mảng, thêm cùng số imei vào ngay sau
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
        print('\nthe Device already exists in my_client array. Print in  handle_flagConfig_1. \n')
    else:
        my_clients += [conn,deviceIm] 
    if deviceIm in flag_config:                        
        print("The device already exist in the flag_config array.\n")
    else:                          
        if "ChannelWifi1" in jsonObject:                             
            try:    
                flag_config+=[deviceIm,jsonObject['Status']]                                                 
                sqlUpdate='''UPDATE "Wifi"
                    SET "ChannelWifi1"='%d',"ChannelModeWifi1"='%d'                     
                    WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi1']),(jsonObject['ChannelModeWifi1']), (jsonObject['Imei']))
                cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
                print('update ChannelWifi1 and ChannelModeWifi1 of Wifi table success.\n')                           
            except (Exception, psycopg2.Error) as error:
                print("Failed to update  ChannelWifi1 and ChannelModeWifi1 of Device table.\n", error)
            connectionSql.commit()
        elif "ChannelWifi2" in jsonObject :
            flag_config+=[deviceIm,jsonObject['Status']]
            try:                     
                sqlUpdate='''UPDATE "Wifi"
                    SET "ChannelWifi2"='%d',"ChannelModeWifi2"='%d'                     
                    WHERE "Imei"= '%s'  '''%((jsonObject['ChannelWifi2']),(jsonObject['ChannelModeWifi2']), (jsonObject['Imei']))
                cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect
                print('update ChannelWifi2 and ChannelModeWifi2 of Wifi table success.\n')                           
            except (Exception, psycopg2.Error) as error:
                print("Failed to update  ChannelWifi2 and ChannelModeWifi2 of Device table.\n", error)
            connectionSql.commit()
        else:
            flag_config+=[deviceIm,jsonObject['Status']] 
    handle_remove_imei_in_check_device_imei(deviceIm)
       

def handle_flagConfig_2(deviceIm,conn,jsonObject):
    global my_clients

    handle_remove_imei_in_check_device_imei(deviceIm)
    print('\nre-connect package, print in handle_flagConfig_2\n ')
    try:    
        sqlUpdate='''UPDATE "Device"
            SET "UpTime"='%s'                    
            WHERE "Imei"= '%s'  '''%((jsonObject['UpTime']), (jsonObject['Imei']))
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
        print('update UpTime  of Device table success.\n') 
        connectionSql.commit()                          
    except (Exception, psycopg2.Error) as error:
        print("Failed to update UpTime  of Device table.\n", error)
    try:    
        sqlUpdate='''UPDATE "Wifi"
            SET "TotalDataWifi1"='%d',"TotalDataWifi2"='%d'                     
            WHERE "Imei"= '%s'  '''%((jsonObject['TotalDataWifi1']),(jsonObject['TotalDataWifi2']), (jsonObject['Imei']))
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
        print('update TotalDataWifi  of Device table success.\n') 
        connectionSql.commit()                          
    except (Exception, psycopg2.Error) as error:
        print("Failed to update TotalDataWifi  of Device table.\n", error)
    try:    
        sqlUpdate='''UPDATE "Ethernet"
            SET "TotalDataEthernet"='%d'                    
            WHERE "Imei"= '%s'  '''%((jsonObject['TotalDataEthernet']), (jsonObject['Imei']))
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái connect lên database mõi khi có connect                                 
        print('update TotalDataEthernet  of Device table success.\n') 
        connectionSql.commit()                          
    except (Exception, psycopg2.Error) as error:
        print("Failed to update TotalDataEthernet of Device table.\n", error)
    if deviceIm in my_clients:                                                      # kiểm tra Client đã tồn tại trong mảng client chưad
        print('the Device already exists in my_client array. Print in  handle_flagConfig_2.\n')
    else:
        my_clients += [conn,deviceIm]                   
        print('the Device does not exist in my_client array. Print in  handle_flagConfig_2. \n')    

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
    
