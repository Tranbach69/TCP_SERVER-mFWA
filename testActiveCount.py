import random
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

def get_device_table():
  sqlGetDevice='''SELECT "Imei" FROM "Device" '''
  cursor.execute(sqlGetDevice)
  result=cursor.fetchall()
  return len(result)
def get_wifi_table():
  sqlGetWifi='''SELECT "WifiOpen" FROM "Wifi" '''
  cursor.execute(sqlGetWifi)
  counter=0
  result=cursor.fetchall()
  for i in result:
    if i==(1,):
      counter=counter+1  
  return counter
def insert_chartNumberDeviceActive_table(totalDevice,totalDeviceActive,test):
  try:                
      sqlInsertInto='''INSERT INTO "ChartNumberDeviceActives"
          VALUES ('%d',%d,%d,'0',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00','%s')
          '''%((random.randint(0,100000000000000000)),(totalDevice),(totalDeviceActive),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(test))
      cursor.execute(sqlInsertInto)
      print('insert into chartNumberDeviceActive success')
  except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into chartNumberDeviceActive table", error)
  connectionSql.commit()
def main():
#   totalDevice=get_device_table()
#   totalDeviceActive=get_wifi_table()
  insert_chartNumberDeviceActive_table(1450,982,'1673574307')


  # get_wifi_table()
            # thread cho device

if __name__ == '__main__':                      # thread chính
    main()