
def handle_device_disconnect (conn,deviceIm):
    print('Device disconnected.  \n')
    conn.sendall("failure".encode('utf-8'))  
    try:                                                                        # không tồn tại thì có nghĩa là thiết bị đang mất kết nối với server
        sqlUpdate='''UPDATE "Device"
            SET "SocketConnection"='0'
            WHERE "Imei"= '%s'  '''%(deviceIm)
        cursor.execute(sqlUpdate)                                               #cập nhật trạng thái lên server
        print('update SocketConnection:0 of Device table success.\n')                          
    except (Exception, psycopg2.Error) as error:                        
        print("Failed to update  SocketConnection:0 of Device table.\n", error)      # in ra lỗi nếu xảy ra khi cập nhật data base           
    connectionSql.commit() 