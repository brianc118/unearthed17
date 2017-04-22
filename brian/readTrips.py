from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime
import json
import pickle

# with open('drivers.json') as data_file:    
#     drivers = json.load(data_file)
drivers = {8:{'geofence_speeding_1':[datetime.datetime(2016,5,26,19,25,22),datetime.datetime(2016,5,27,13,31,37),datetime.datetime(2016,9,14,11,57,34),datetime.datetime(2016,6,8,10,44,10),datetime.datetime(2016,7,1,16,13,45),datetime.datetime(2016,7,1,16,16,40),datetime.datetime(2016,7,2,9,31,41),datetime.datetime(2016,7,2,9,34,43),datetime.datetime(2016,9,18,10,53,51),datetime.datetime(2016,9,18,10,53,54),datetime.datetime(2016,10,29,15,15,41),datetime.datetime(2016,10,29,15,36,42)],'geofence_speeding_2':[],'geofence_speeding_3':[],'journey_management':[datetime.datetime(2016,7,26,18,4,35),datetime.datetime(2016,7,26,18,5,52),datetime.datetime(2016,7,26,18,6,3),datetime.datetime(2016,7,26,18,7,41),datetime.datetime(2016,7,26,18,8,14),datetime.datetime(2016,7,26,18,9,40),datetime.datetime(2016,7,26,18,10,3),datetime.datetime(2016,7,26,18,11,48),datetime.datetime(2016,7,29,15,45,11),datetime.datetime(2016,7,29,15,52),datetime.datetime(2016,7,29,15,53,5),datetime.datetime(2016,7,29,15,54,36),datetime.datetime(2016,7,29,15,56,4),datetime.datetime(2016,7,29,15,59,25),datetime.datetime(2016,7,29,15,59,31),datetime.datetime(2016,8,2,14,35,19),datetime.datetime(2016,8,3,8,32,44),datetime.datetime(2016,8,3,8,33,20),datetime.datetime(2016,8,3,8,36,6),datetime.datetime(2016,8,3,8,36,23),datetime.datetime(2016,8,14,10,30,57),datetime.datetime(2016,8,14,10,34,44),datetime.datetime(2016,8,14,10,35,24),datetime.datetime(2016,8,20,6,36,43),datetime.datetime(2016,8,20,17,44,6),datetime.datetime(2016,8,23,17,0,29),datetime.datetime(2016,8,24,18,33,11),datetime.datetime(2016,9,12,16,1,43),datetime.datetime(2016,9,12,16,5,11),datetime.datetime(2016,9,21,18,55,15),datetime.datetime(2016,10,7,8,19,57),datetime.datetime(2016,10,9,16,15,32),datetime.datetime(2016,10,9,18,33,47),datetime.datetime(2016,10,9,18,38,7),datetime.datetime(2016,10,9,18,42,53),datetime.datetime(2016,11,8,17,29,6),datetime.datetime(2016,11,14,15,17,52),datetime.datetime(2016,11,14,17,22,59),datetime.datetime(2016,11,14,19,19,50),datetime.datetime(2016,11,14,19,20,39),datetime.datetime(2016,11,14,19,20,46),datetime.datetime(2016,11,14,19,20,59),datetime.datetime(2016,11,14,19,21,13),datetime.datetime(2016,11,14,19,21,24),datetime.datetime(2016,11,23,17,30,14),datetime.datetime(2016,12,7,12,32,13),datetime.datetime(2016,12,12,15,38,52),datetime.datetime(2016,12,14,18,15,51),datetime.datetime(2017,1,2,9,55,19),datetime.datetime(2017,1,2,10,4,52),datetime.datetime(2017,1,2,10,6,16),datetime.datetime(2017,1,10,12,25,12),datetime.datetime(2017,1,27,15,20,29),datetime.datetime(2017,1,27,15,21,47),datetime.datetime(2017,1,27,15,22,4),datetime.datetime(2017,1,27,17,29,17),datetime.datetime(2017,2,7,12,26,52),datetime.datetime(2017,2,8,18,4,57),datetime.datetime(2017,2,8,18,7,46),datetime.datetime(2017,2,22,18,19,2),datetime.datetime(2017,2,23,8,33,50),datetime.datetime(2017,2,23,8,38,12),datetime.datetime(2017,2,23,8,39,10),datetime.datetime(2017,2,23,8,40,46),datetime.datetime(2017,2,23,8,42,7),datetime.datetime(2017,2,23,8,42,50),datetime.datetime(2017,2,23,18,10,6),datetime.datetime(2017,2,23,18,13,32),datetime.datetime(2017,2,23,18,16,23),datetime.datetime(2017,2,23,18,17,50),datetime.datetime(2017,3,12,11,45,58),datetime.datetime(2017,3,22,17,52,21),datetime.datetime(2017,3,22,17,56,4),datetime.datetime(2017,3,22,17,57,2),datetime.datetime(2017,3,25,15,20,13),datetime.datetime(2017,3,25,15,25,10),datetime.datetime(2016,9,26,10,38,37),datetime.datetime(2016,9,27,17,6,1)],'seat_belt_driver':[datetime.datetime(2016,11,29,9,54,53),datetime.datetime(2016,11,29,12,12,57),datetime.datetime(2016,11,29,13,49,20),datetime.datetime(2016,11,29,13,55,35),datetime.datetime(2016,11,29,13,59,52),datetime.datetime(2016,11,29,13,59,59),datetime.datetime(2016,11,29,15,15,58),datetime.datetime(2016,11,29,15,16,31),datetime.datetime(2016,12,2,8,34,36)],'seat_belt_passenger':[]},9:{'geofence_speeding_1':[datetime.datetime(2016,5,26,19,25,22),datetime.datetime(2016,5,27,13,31,37),datetime.datetime(2016,9,14,11,57,34),datetime.datetime(2016,6,8,10,44,10),datetime.datetime(2016,7,1,16,13,45),datetime.datetime(2016,7,1,16,16,40),datetime.datetime(2016,7,2,9,31,41),datetime.datetime(2016,7,2,9,34,43),datetime.datetime(2016,9,18,10,53,51),datetime.datetime(2016,9,18,10,53,54),datetime.datetime(2016,10,29,15,15,41),datetime.datetime(2016,10,29,15,36,42)],'geofence_speeding_2':[],'geofence_speeding_3':[],'journey_management':[datetime.datetime(2016,7,26,18,4,35),datetime.datetime(2016,7,26,18,5,52),datetime.datetime(2016,7,26,18,6,3),datetime.datetime(2016,7,26,18,7,41),datetime.datetime(2016,7,26,18,8,14),datetime.datetime(2016,7,26,18,9,40),datetime.datetime(2016,7,26,18,10,3),datetime.datetime(2016,7,26,18,11,48),datetime.datetime(2016,7,29,15,45,11),datetime.datetime(2016,7,29,15,52),datetime.datetime(2016,7,29,15,53,5),datetime.datetime(2016,7,29,15,54,36),datetime.datetime(2016,7,29,15,56,4),datetime.datetime(2016,7,29,15,59,25),datetime.datetime(2016,7,29,15,59,31),datetime.datetime(2016,8,2,14,35,19),datetime.datetime(2016,8,3,8,32,44),datetime.datetime(2016,8,3,8,33,20),datetime.datetime(2016,8,3,8,36,6),datetime.datetime(2016,8,3,8,36,23),datetime.datetime(2016,8,14,10,30,57),datetime.datetime(2016,8,14,10,34,44),datetime.datetime(2016,8,14,10,35,24),datetime.datetime(2016,8,20,6,36,43),datetime.datetime(2016,8,20,17,44,6),datetime.datetime(2016,8,23,17,0,29),datetime.datetime(2016,8,24,18,33,11),datetime.datetime(2016,9,12,16,1,43),datetime.datetime(2016,9,12,16,5,11),datetime.datetime(2016,9,21,18,55,15),datetime.datetime(2016,10,7,8,19,57),datetime.datetime(2016,10,9,16,15,32),datetime.datetime(2016,10,9,18,33,47),datetime.datetime(2016,10,9,18,38,7),datetime.datetime(2016,10,9,18,42,53),datetime.datetime(2016,11,8,17,29,6),datetime.datetime(2016,11,14,15,17,52),datetime.datetime(2016,11,14,17,22,59),datetime.datetime(2016,11,14,19,19,50),datetime.datetime(2016,11,14,19,20,39),datetime.datetime(2016,11,14,19,20,46),datetime.datetime(2016,11,14,19,20,59),datetime.datetime(2016,11,14,19,21,13),datetime.datetime(2016,11,14,19,21,24),datetime.datetime(2016,11,23,17,30,14),datetime.datetime(2016,12,7,12,32,13),datetime.datetime(2016,12,12,15,38,52),datetime.datetime(2016,12,14,18,15,51),datetime.datetime(2017,1,2,9,55,19),datetime.datetime(2017,1,2,10,4,52),datetime.datetime(2017,1,2,10,6,16),datetime.datetime(2017,1,10,12,25,12),datetime.datetime(2017,1,27,15,20,29),datetime.datetime(2017,1,27,15,21,47),datetime.datetime(2017,1,27,15,22,4),datetime.datetime(2017,1,27,17,29,17),datetime.datetime(2017,2,7,12,26,52),datetime.datetime(2017,2,8,18,4,57),datetime.datetime(2017,2,8,18,7,46),datetime.datetime(2017,2,22,18,19,2),datetime.datetime(2017,2,23,8,33,50),datetime.datetime(2017,2,23,8,38,12),datetime.datetime(2017,2,23,8,39,10),datetime.datetime(2017,2,23,8,40,46),datetime.datetime(2017,2,23,8,42,7),datetime.datetime(2017,2,23,8,42,50),datetime.datetime(2017,2,23,18,10,6),datetime.datetime(2017,2,23,18,13,32),datetime.datetime(2017,2,23,18,16,23),datetime.datetime(2017,2,23,18,17,50),datetime.datetime(2017,3,12,11,45,58),datetime.datetime(2017,3,22,17,52,21),datetime.datetime(2017,3,22,17,56,4),datetime.datetime(2017,3,22,17,57,2),datetime.datetime(2017,3,25,15,20,13),datetime.datetime(2017,3,25,15,25,10),datetime.datetime(2016,9,26,10,38,37),datetime.datetime(2016,9,27,17,6,1)],'seat_belt_driver':[datetime.datetime(2016,11,29,9,54,53),datetime.datetime(2016,11,29,12,12,57),datetime.datetime(2016,11,29,13,49,20),datetime.datetime(2016,11,29,13,55,35),datetime.datetime(2016,11,29,13,59,52),datetime.datetime(2016,11,29,13,59,59),datetime.datetime(2016,11,29,15,15,58),datetime.datetime(2016,11,29,15,16,31),datetime.datetime(2016,12,2,8,34,36)],'seat_belt_passenger':[]},17:{'geofence_speeding_1':[datetime.datetime(2016,5,26,19,25,22),datetime.datetime(2016,5,27,13,31,37),datetime.datetime(2016,9,14,11,57,34),datetime.datetime(2016,6,8,10,44,10),datetime.datetime(2016,7,1,16,13,45),datetime.datetime(2016,7,1,16,16,40),datetime.datetime(2016,7,2,9,31,41),datetime.datetime(2016,7,2,9,34,43),datetime.datetime(2016,9,18,10,53,51),datetime.datetime(2016,9,18,10,53,54),datetime.datetime(2016,10,29,15,15,41),datetime.datetime(2016,10,29,15,36,42)],'geofence_speeding_2':[],'geofence_speeding_3':[],'journey_management':[datetime.datetime(2016,7,26,18,4,35),datetime.datetime(2016,7,26,18,5,52),datetime.datetime(2016,7,26,18,6,3),datetime.datetime(2016,7,26,18,7,41),datetime.datetime(2016,7,26,18,8,14),datetime.datetime(2016,7,26,18,9,40),datetime.datetime(2016,7,26,18,10,3),datetime.datetime(2016,7,26,18,11,48),datetime.datetime(2016,7,29,15,45,11),datetime.datetime(2016,7,29,15,52),datetime.datetime(2016,7,29,15,53,5),datetime.datetime(2016,7,29,15,54,36),datetime.datetime(2016,7,29,15,56,4),datetime.datetime(2016,7,29,15,59,25),datetime.datetime(2016,7,29,15,59,31),datetime.datetime(2016,8,2,14,35,19),datetime.datetime(2016,8,3,8,32,44),datetime.datetime(2016,8,3,8,33,20),datetime.datetime(2016,8,3,8,36,6),datetime.datetime(2016,8,3,8,36,23),datetime.datetime(2016,8,14,10,30,57),datetime.datetime(2016,8,14,10,34,44),datetime.datetime(2016,8,14,10,35,24),datetime.datetime(2016,8,20,6,36,43),datetime.datetime(2016,8,20,17,44,6),datetime.datetime(2016,8,23,17,0,29),datetime.datetime(2016,8,24,18,33,11),datetime.datetime(2016,9,12,16,1,43),datetime.datetime(2016,9,12,16,5,11),datetime.datetime(2016,9,21,18,55,15),datetime.datetime(2016,10,7,8,19,57),datetime.datetime(2016,10,9,16,15,32),datetime.datetime(2016,10,9,18,33,47),datetime.datetime(2016,10,9,18,38,7),datetime.datetime(2016,10,9,18,42,53),datetime.datetime(2016,11,8,17,29,6),datetime.datetime(2016,11,14,15,17,52),datetime.datetime(2016,11,14,17,22,59),datetime.datetime(2016,11,14,19,19,50),datetime.datetime(2016,11,14,19,20,39),datetime.datetime(2016,11,14,19,20,46),datetime.datetime(2016,11,14,19,20,59),datetime.datetime(2016,11,14,19,21,13),datetime.datetime(2016,11,14,19,21,24),datetime.datetime(2016,11,23,17,30,14),datetime.datetime(2016,12,7,12,32,13),datetime.datetime(2016,12,12,15,38,52),datetime.datetime(2016,12,14,18,15,51),datetime.datetime(2017,1,2,9,55,19),datetime.datetime(2017,1,2,10,4,52),datetime.datetime(2017,1,2,10,6,16),datetime.datetime(2017,1,10,12,25,12),datetime.datetime(2017,1,27,15,20,29),datetime.datetime(2017,1,27,15,21,47),datetime.datetime(2017,1,27,15,22,4),datetime.datetime(2017,1,27,17,29,17),datetime.datetime(2017,2,7,12,26,52),datetime.datetime(2017,2,8,18,4,57),datetime.datetime(2017,2,8,18,7,46),datetime.datetime(2017,2,22,18,19,2),datetime.datetime(2017,2,23,8,33,50),datetime.datetime(2017,2,23,8,38,12),datetime.datetime(2017,2,23,8,39,10),datetime.datetime(2017,2,23,8,40,46),datetime.datetime(2017,2,23,8,42,7),datetime.datetime(2017,2,23,8,42,50),datetime.datetime(2017,2,23,18,10,6),datetime.datetime(2017,2,23,18,13,32),datetime.datetime(2017,2,23,18,16,23),datetime.datetime(2017,2,23,18,17,50),datetime.datetime(2017,3,12,11,45,58),datetime.datetime(2017,3,22,17,52,21),datetime.datetime(2017,3,22,17,56,4),datetime.datetime(2017,3,22,17,57,2),datetime.datetime(2017,3,25,15,20,13),datetime.datetime(2017,3,25,15,25,10),datetime.datetime(2016,9,26,10,38,37),datetime.datetime(2016,9,27,17,6,1)],'seat_belt_driver':[datetime.datetime(2016,11,29,9,54,53),datetime.datetime(2016,11,29,12,12,57),datetime.datetime(2016,11,29,13,49,20),datetime.datetime(2016,11,29,13,55,35),datetime.datetime(2016,11,29,13,59,52),datetime.datetime(2016,11,29,13,59,59),datetime.datetime(2016,11,29,15,15,58),datetime.datetime(2016,11,29,15,16,31),datetime.datetime(2016,12,2,8,34,36)],'seat_belt_passenger':[]}}

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost/ivms', echo=True)
Session = sessionmaker(bind=engine)


class Trip(Base):
    __tablename__ = 'Trips'

    TripUID = Column(Integer, primary_key=True)
    Date = Column(String(512))  #11/1/2016
    AssetName = Column(String(512)) 
    AssetID = Column(Integer)
    AssetExtra = Column(String(512))
    AssetName2 = Column(String(512))
    AssetID2 = Column(Integer)
    AssetExtra2 = Column(String(512))
    SiteName = Column(String(512))
    OriginalDriverName = Column(String(512))
    TrailerInfo = Column(String(512))
    TripID = Column(Integer)
    ActivityStartDateTime = Column(String(512))  #HH:MM:SS
    DepartureTime = Column(String(512))
    ArrivalTime = Column(String(512))
    ActivityEndDateTime = Column(String(512))  #11/1/2016 HH:MM:SS
    TimeZone = Column(String(512))
    DrivingTimePercentage = Column(String(512))
    StandingTimePercentage = Column(String(512))
    IdleTimePercentage = Column(String(512))
    TotalDrivingTime = Column(String(512))
    TotalStandingTime = Column(String(512))
    TotalDuration = Column(String(512)) # ???
    TotalIdleTime = Column(String(512))
    ParkingTime = Column(String(512))
    StartOdometer = Column(Float)
    EndOdometer = Column(Float)
    TotalDistanceTravelled = Column(Float) #
    TotalFuelUsed = Column(Float)
    FuelConsumptionMeasured = Column(Float)
    TotalCO2Emission = Column(Float)
    TotalEngineSeconds = Column(String(512))
    AverageSpeed = Column(Float) #
    MaxSpeed = Column(Float) #



emptyInfo = {'cornering_1': [],
             'cornering_2': [],
             'cornering_3': [],
             'geofence_speeding_1': [],
             'geofence_speeding_2': [],
             'geofence_speeding_3': [],
             'public_speeding_1': [],
             'public_speeding_2': [],
             'public_speeding_3': [],
             'journey_management': [],
             'harsh_acceleration': [],
             'harsh_breaking': [],
             'excessive_breaking': [],
             'night_driving': [],
             'no_go_zone': [],
             'seat_belt_driver': [],
             'seat_belt_passenger': []
            }


tripInfo = {'start': None,
            'end': None,
            'TotalDuration': None,
            'TripID': 0,
            'TotalDistanceTravelled': 0,
            'AverageSpeed': 0,
            'MaxSpeed': 0,
            'cornering_1': [],
            'cornering_2': [],
            'cornering_3': [],
            'geofence_speeding_1': [],
            'geofence_speeding_2': [],
            'geofence_speeding_3': [],
            'public_speeding_1': [],
            'public_speeding_2': [],
            'public_speeding_3': [],
            'journey_management': [],
            'harsh_acceleration': [],
            'harsh_breaking': [],
            'excessive_breaking': [],
            'night_driving': [],
            'no_go_zone': [],
            'seat_belt_driver': [],
            'seat_belt_passenger': []
           };

trips = {};

session = Session()

# l = session.query(Trip).order_by('AssetName').yield_per(3200)
l = session.query(Trip).yield_per(3200)

print("STARTING")

count = 0
for i in l:
    innovember = datetime.datetime.strptime(i.Date, '%m/%d/%Y').month == 12
    if innovember:
        if i.AssetID not in trips:
            trips[i.AssetID] = []

        start = datetime.datetime.strptime(i.Date + " " + i.ActivityStartDateTime, '%m/%d/%Y %H:%M:%S')
        end = datetime.datetime.strptime(i.ActivityEndDateTime, '%m/%d/%Y %H:%M');
        # dur = datetime.strptime(i.TotalDuration, '%H:%M:%S')
        
        blanktrip = tripInfo
        blanktrip['start'] = start;
        blanktrip['end'] = end;
        blanktrip['TripID'] = i.TripID;
        blanktrip['TotalDuration'] = start - end;
        blanktrip['TotalDistanceTravelled'] = i.TotalDistanceTravelled
        blanktrip['AverageSpeed'] = i.AverageSpeed
        blanktrip['MaxSpeed'] = i.MaxSpeed

        trips[i.AssetID].append(blanktrip)
        count += 1

print("SORTED TRIPTIMES")
print('Total rows = {}'.format(count))

for driver_id in drivers.keys():
    driver = drivers[driver_id];
    for k in emptyInfo.keys():
        if k not in driver:
            continue

        for time in driver[k]:
            # find trip
            for trip in trips[driver_id]:
                if trip['start'] >= time and time <= trip['end']:
                    trip[k].append(time)
                    break

print("DUMPING TRIP")
with open('trip.pickle', 'wb') as handle:
    pickle.dump(trip, handle, protocol=pickle.HIGHEST_PROTOCOL)

print("DONE")