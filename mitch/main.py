from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, create_engine, desc
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from copy import deepcopy
import re

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

class Event(Base):
    __abstract__ = True

    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Integer)

class Alert(Event):
    __tablename__ = 'Alerts'

    AlertId = Column(Integer, primary_key=True)
    Drivers_ID = Column(Integer)
    EventType = Column(String(512))
    Textbox20 = Column(String(512))
    RoadSpeedLimit = Column(String(512))
    OverspeedLocation = Column(String(512))
    TotalDuration = Column(String(512))
    StartOdo = Column(Float)
    EndOdo = Column(Float)
    F_StartStreet = Column(String(512))
    F_StartSuburb = Column(String(512))
    F_EndStreet = Column(String(512))
    F_EndSuburb = Column(String(512))
    StartLocation = Column(String(512))
    EndLocation = Column(String(512))
    StartLongLat = Column(String(512))
    EndLongLat = Column(String(512))
    FuelUsed = Column(Float)
    Distance = Column(Float)

class Other(Event):
    __tablename__ = 'EventOther'
    
    EventOtherId = Column(Integer, primary_key=True)
    Drivers_ID = Column(Integer)

class Corner(Event):
    __tablename__ = 'EventCorner'
    
    EventCornerId = Column(Integer, primary_key=True)
    AssetID = Column(Integer)
    Cat = Column(String(512))

class Speed(Event):
    __tablename__ = 'EventSpeed'
    
    EventSpeedId = Column(Integer, primary_key=True)
    Drivers_ID = Column(Integer)

class Year(Event):
    __tablename__ = 'EventYear'
    
    EventYearId = Column(Integer, primary_key=True)
    Drivers_ID = Column(Integer)


def add_event(events, eventType, event, eventDateTime):
    if not event:
        return False

    events[eventType].append(eventDateTime)
    return True

events = [('Cat 1', 'cornering_1'),
          ('Cat 2', 'cornering_2'),
          ('Cat 3', 'cornering_3'),
          ('Speeding in Geofence Cat1', 'geofence_speeding_1'),
          ('Speeding in Geofence Cat2', 'geofence_speeding_2'),
          ('Speeding in Geofence Cat3', 'geofence_speeding_3'),
          ('Cat 1', 'public_speeding_1'),
          ('Cat 2', 'public_speeding_2'),
          ('Cat 3', 'public_speeding_3'),
          ('Journey Management', 'journey_management'),
          ('Harsh Acceleration', 'harsh_acceleration'),
          ('Harsh Breaking', 'harsh_breaking'),
          ('Harsh Breaking Excessively', 'excessive_breaking'),
          ('Night Driving', 'night_driving'),
          ('No Go Zone', 'no_go_zone'),
          ('Seat Belt LSR - Driver', 'seat_belt_driver'),
          ('Seat Belt LSR - Passenger', 'seat_belt_passenger')]

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


####################################################################################
#       GET ALL DAT DRIVER DATA
####################################################################################

session = Session()
drivers = {}

for i in session.query(Alert).order_by('Drivers_ID'):
    if not datetime.strptime(i.EventStartDate, '%d/%m/%Y').month == 11:
        continue

    driver = int(i.Drivers_ID)
    if driver not in drivers:
        drivers[driver] = deepcopy(emptyInfo)

    dt = datetime.strptime(i.EventStartTime + ' ' + i.EventStartDate, '%H:%M:%S %d/%m/%Y')

    event = i.EventDescription
    for eventPattern, eventType in events:
        if add_event(drivers[driver], eventType, re.search(eventPattern, event), dt):
            break

for i in session.query(Corner).order_by('EventCornerId'):
    if not datetime.strptime(i.EventStartDate, '%d/%m/%Y').month == 11:
        continue

    driver = int(i.AssetID)
    if driver not in drivers:
        drivers[driver] = deepcopy(emptyInfo)

    dt = datetime.strptime(i.EventStartTime + ' ' + i.EventStartDate, '%H:%M:%S %d/%m/%Y')

    event = i.Cat
    for eventPattern, eventType in events:
        if add_event(drivers[driver], eventType, re.search(eventPattern, event), dt):
            break

for i in session.query(Speed).order_by('EventSpeedId'):
    if not datetime.strptime(i.EventStartDate, '%d/%m/%Y').month == 11:
        continue

    driver = int(i.Drivers_ID)
    if driver not in drivers:
        drivers[driver] = deepcopy(emptyInfo)

    dt = datetime.strptime(i.EventStartTime + ' ' + i.EventStartDate, '%H:%M:%S %d/%m/%Y')

    event = i.EventDescription
    for eventPattern, eventType in events:
        if add_event(drivers[driver], eventType, re.search(eventPattern, event), dt):
            break

for i in session.query(Year).order_by('EventYearId'):
    if not datetime.strptime(i.EventStartDate, '%d/%m/%Y').month == 11:
        continue

    driver = int(i.Drivers_ID)
    if driver not in drivers:
        drivers[driver] = deepcopy(emptyInfo)

    dt = datetime.strptime(i.EventStartTime + ' ' + i.EventStartDate, '%H:%M:%S %d/%m/%Y')

    event = i.EventDescription
    for eventPattern, eventType in events:
        if add_event(drivers[driver], eventType, re.search(eventPattern, event), dt):
            break

for i in session.query(Other).order_by('EventOtherId'):
    if not datetime.strptime(i.EventStartDate, '%d/%m/%Y').month == 11:
        continue

    driver = int(i.Drivers_ID)
    if driver not in drivers:
        drivers[driver] = deepcopy(emptyInfo)

    dt = datetime.strptime(i.EventStartTime + ' ' + i.EventStartDate, '%H:%M:%S %d/%m/%Y')

    event = i.EventDescription
    for eventPattern, eventType in events:
        if add_event(drivers[driver], eventType, re.search(eventPattern, event), dt):
            break


####################################################################################
#       OKAY ITS TRIP TIME
####################################################################################


driverTrips = {}
tripCount = 0
for i in session.query(Trip).yield_per(8192):
    if not datetime.strptime(i.Date, '%m/%d/%Y').month == 11:
        continue

    driver = i.AssetID
    if driver not in driverTrips:
        driverTrips[driver] = []

    start = datetime.strptime(i.Date + ' ' + i.ActivityStartDateTime, '%m/%d/%Y %H:%M:%S')
    end = datetime.strptime(i.ActivityEndDateTime, '%m/%d/%Y %H:%M')
    
    newTrip = deepcopy(tripInfo)
    newTrip['start'] = start
    newTrip['end'] = end
    newTrip['TripID'] = i.TripID;
    newTrip['TotalDuration'] = start - end
    newTrip['TotalDistanceTravelled'] = i.TotalDistanceTravelled
    newTrip['AverageSpeed'] = i.AverageSpeed
    newTrip['MaxSpeed'] = i.MaxSpeed

    driverTrips[driver].append(newTrip)
    tripCount += 1

print('Total trips = {}'.format(tripCount))
print('Total trip ids = {}'.format(len(driverTrips.keys())))
print('Total driver ids = {}'.format(len(drivers.keys())))
print('Intersect = {}'.format(len(set(list(driverTrips.keys())).intersection(list(drivers.keys())))))

for driverID,eventTypes in drivers.iteritems():
    if driverID not in driverTrips:
        continue

    for eventType,eventList in eventTypes.iteritems():
        for eventTime in eventList:
            for trip in driverTrips[driverID]:
                if trip['start'] <= eventTime and eventTime <= trip['end']:
                    trip[eventType].append(eventTime)
                    break

for eventType in emptyInfo.keys():
    print('{0}: {1}'.format(eventType, len([1 for event in trip[eventType] for trip in driverTrips[349]])))
