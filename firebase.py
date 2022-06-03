import firebase_admin
import serial
import time
from firebase_admin import credentials
from firebase_admin import firestore

class Position:
    def __init__(self, latitude = 0, longitude = 0, t = 0):
        self.latitude = latitude
        self.longitude = longitude
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'latitude': self.latitude,
            u'longitude': self.longitude,
        }
        return dest

class Heart:
    def __init__(self, heart_rate = 0, t = 0):
        self.heart_rate = heart_rate
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'heart_rate': self.heart_rate
        }
        return dest

class Light:
    def __init__(self, inpersity = 0, t = 0):
        self.inpersity = inpersity
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'inpersity': self.inpersity
        }
        return dest

class Breath:
    def __init__(self, breath = 0, t = 0):
        self.breath = breath
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'breath': self.breath
        }
        return dest

cred = credentials.Certificate('smart-pet-collar-4am-firebase-adminsdk-mg4bv-590a0331b7.json')
firebase_admin.initialize_app(cred,{
    'projectID' : 'smart-pet-collar-4am'
})

ser = serial.Serial(
    port='COM6',
    baudrate=9600,
)

count = 0
while (count != 100):
    data = ser.readline().decode().split(',')

    heartrate = float(data[1])
    lat = float(data[3])
    lon = float(data[5])
    luxlen = len(data[7])
    lux = float(data[7][0: luxlen-2])

    t1 = time.time()

    db1 = firestore.client()
    heart_col = db1.collection(u'heart sensor')
    heart = Heart(u'%.3f' %heartrate, t1)
    heart_col.add(heart.to_dict())

    low_value = 60
    high_value = 120
    color = ''
    if (low_value >= heartrate or heartrate >= high_value) :
        color = 'R'
    else:
        color = 'G'
    color = color.encode('utf-8')
    ser.write(color)

    db2 = firestore.client()
    breath_col = db2.collection(u'breath sensor')
    breath = Breath(u'%.3f' %breath, t1)
    breath_col.add(breath.to_dict())

    db3 = firestore.client()
    light_col = db3.collection(u'light sensor')
    light = Light(u'%.3f' %lux, t1)
    light_col.add(light.to_dict())

    db4 = firestore.client()
    GPS_col = db4.collection(u'GPS sensor')
    pos = Position(u'%.3f' %lat, u'%.3f' %lon, t1)
    GPS_col.add(pos.to_dict())

    t2 = time.time()

    count += 1
    if(t2-t1 > 1):
        continue
    else:
        time.sleep(1-(t2-t1))

#'databaseURL' : 'https://smart-pet-collar-4am-default-rtdb.firebaseio.com'