import psycopg2
import datetime
try:
    connection = psycopg2.connect(user="postgres",
                                  password="1",
                                  host="103.229.41.235",
                                  port="5432",
                                  database="DATN")
    cursor = connection.cursor()
    sqlInsertInto='''INSERT INTO "Wifi"
        VALUES ('9','wifiOpen','WifiMode','CurAp','WifiNat',
        'ssid1','authType1','enctrMode1','authPwd1','clientcount1','bcast1','iso1','macAdd1','channelMode1','channel1','dhcpIp1','dhcpIpStart1','dhcpIpEnd1','dhcptime1',
        'ssid2','authType2','enctrMode2','authPwd2','clientcount2','bcast2','iso2','macAdd2','channelMode2','channel2','dhcpIp2','dhcpIpStart2','dhcpIpEnd2','dhcptime2',
        'sta','StaSsidExt','StaSecurity','StaProtocol','StaPassword',false,'0001-01-01 00:00:00','0001-01-01 00:00:00','0001-01-01 00:00:00')'''
    sqlUpdate='''UPDATE "AccountAdmin"
        SET "UserName"='bach123' WHERE "Id"=4'''
    cursor.execute(sqlInsertInto)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into AccountAdmin table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into Wifi table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
