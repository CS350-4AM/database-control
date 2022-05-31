import firebase_admin
import serial
import random
import time
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

class Position:
    def __init__(self, latitude = 0, longitude = 0, t = ''):
        self.latitude = latitude
        self.longitude = longitude
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'latitude': self.latitude,
            u'longitude': self.longitude
        }
        return dest

class Heart:
    def __init__(self, heart_rate = 0, t = ''):
        self.heart_rate = heart_rate
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'heart_rate': self.heart_rate
        }
        return dest

class Light:
    def __init__(self, inpersity = 0, t = ''):
        self.inpersity = inpersity
        self.time = t

    def to_dict(self):
        dest = {
            u'created_at': self.time,
            u'inpersity': self.inpersity
        }
        return dest

class Breath:
    def __init__(self, breath = 0, t = ''):
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

while (ser.readable()):
    data = ser.readline().decode().strip(',')
    t = time.strftime('%X')

    db1 = firestore.client()
    heart_col = db1.collection(u'heart sensor')
    heart = Heart(u'%d' %1, t)
    heart_col.add(heart.to_dict())

    # db2 = firestore.client()
    # breath_col = db2.collection(u'breath sensor').document(u'a').set({'1':2})
    # breath = Breath(latitude= u'%d' %1, longitude = u'a', t = time.strftime('%X'))
    # breath_col.add(breath.to_dict())

    # db3 = firestore.client()
    # light_col = db3.collection(u'light sensor').document(u'a').set({'1':2})
    # light = Light(latitude= u'%d' %1, longitude = u'a', t = time.strftime('%X'))
    # light_col.add(light.to_dict())

    db4 = firestore.client()
    GPS_col = db4.collection(u'GPS sensor')
    pos = Position(u'%d' %1, u'a', t)
    GPS_col.add(pos.to_dict())

    time.sleep(1)

#'databaseURL' : 'https://smart-pet-collar-4am-default-rtdb.firebaseio.com'