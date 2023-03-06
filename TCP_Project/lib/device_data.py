

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