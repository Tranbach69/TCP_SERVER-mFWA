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
def insert_chartNumberDeviceActive_table(totalDevice,totalDeviceActive):
  try:                
      sqlInsertInto='''INSERT INTO "ChartNumberDeviceActives"
          VALUES ('%d',%d,%d,'0',false,'%s','0001-01-01 00:00:00','0001-01-01 00:00:00','%s')
          '''%((random.randint(0,100000000000000000)),(totalDevice),(totalDeviceActive),(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')),(str(datetime.timestamp(datetime.now()))))
      cursor.execute(sqlInsertInto)
      print('insert into chartNumberDeviceActive success')
  except (Exception, psycopg2.Error) as error:
      print("Failed to insert record into chartNumberDeviceActive table", error)
  connectionSql.commit()
def main():
  totalDevice=get_device_table()
  totalDeviceActive=get_wifi_table()
  insert_chartNumberDeviceActive_table(totalDevice,totalDeviceActive)


  # get_wifi_table()
            # thread cho device

if __name__ == '__main__':                      # thread chính
    main()



# import random
# from datetime import datetime
# import psycopg2
# import logging

# logging.basicConfig(level=logging.DEBUG)

# # Define constants
# WIFI_OPEN = 1
# INSERT_SQL = '''INSERT INTO "ChartNumberDeviceActives"
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''

# connection = None
# cursor = None

# try:
#     connection = psycopg2.connect(user="postgres",
#                                   password="1",
#                                   host="localhost",
#                                   port="5432",
#                                   database="DATN")
#     cursor = connection.cursor()
# except (Exception, psycopg2.Error) as error:
#     logging.error("Failed to connect to the database: %s", error)

# def get_device_count():
#     cursor.execute("SELECT COUNT(*) FROM Device")
#     return cursor.fetchone()[0]

# def get_active_device_count():
#     cursor.execute("SELECT COUNT(*) FROM Wifi WHERE WifiOpen = %s", (WIFI_OPEN,))
#     return cursor.fetchone()[0]

# def insert_chart_data(total_devices, total_active):
#     chart_id = random.randint(0, 1000000000000000000)
#     chart_timestamp = datetime.now()
#     chart_timestamp_str = chart_timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')
#     chart_timestamp_unix = datetime.timestamp(chart_timestamp)
#     values = (chart_id, total_devices, total_active, 0, False, chart_timestamp_str, '0001-01-01 00:00:00', chart_timestamp_unix)
#     cursor.execute(INSERT_SQL, values)
#     logging.info("Inserted data into ChartNumberDeviceActives")
#     connection.commit()

# def main():
#   totalDevice=get_device_count()
#   totalDeviceActive=get_active_device_count()
#   insert_chart_data(totalDevice,totalDeviceActive)

# if __name__ == '__main__':                      # thread chính
#     main()
