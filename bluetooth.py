import sqlite3
import serial

con = sqlite3.connect("C:/database/data.db")

cur = con.cursor()

cur.execute('drop table if exists heartrate')
cur.execute('create table heartrate ( num , value )')

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
)

count = 0

while (ser.readable()):
    count += 1
    data = ser.readline().decode()
    cur.execute("insert into heartrate values ( ? , ? )" , (count,data))
    con.commit()
    if count == 10:
        break

con.close()