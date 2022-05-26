import firebase_admin
import serial
import random
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

# ser = serial.Serial(
#     port='COM6',
#     baudrate=9600,
# )

count = 0

cred = credentials.Certificate('smart-pet-collar-4am-firebase-adminsdk-mg4bv-590a0331b7.json')
firebase_admin.initialize_app(cred,{
    'projectID' : 'smart-pet-collar-4am'
})

db = firestore.client()

doc_ref = db.collection(u'sensor').document(u'heartrate')

# while (ser.readable()):
#     count += 1
#     data = ser.readline().decode()
doc_ref.set({u'1': 1})
for i in range(50):
    doc_ref.update({'%d' %i : (random.randint(100,120),1)})
#ref = db.reference()

#ref = db.reference('heartrate')
#for i in range(50):
#    ref.update({i : random.randint(90,120)})

#'databaseURL' : 'https://smart-pet-collar-4am-default-rtdb.firebaseio.com'

class Position:
    def __init__(self, latitude = 0, longitude = 0):
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude