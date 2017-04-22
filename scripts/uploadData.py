from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os.path
import csv

Base = declarative_base()
engine = create_engine('mysql+pymysql://root@localhost/ivms', echo=True)
Session = sessionmaker(bind=engine)

alert_path = '../../../data/IVMS Challenge/DATA/IVMS/Alert/'
trip_path = '../../../data/IVMS Challenge/DATA/IVMS/Trip/'
event_path = '../../../data/IVMS Challenge/DATA/IVMS/Event/'
gps_path = '../../../data/IVMS Challenge/DATA/IVMS/GPS/'

alert_file = 'ND_Alerts_12_months.csv'
gps_file = 'OriginQLDAU.GPSData.2016-11.csv'
event_corner_file = 'ND_Event_Cornering _Nov_2016.csv'
event_speed_file = 'ND_Event_road_speeds_Nov_2016.csv'
event_other_file = 'ND_Nov_16_Events_others.csv'
trip_file = 'trips_1.csv'


class Alert(Base):
    __tablename__ = 'Alerts'

    AlertId = Column(Integer, primary_key=True)
    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    Drivers_ID = Column(Integer)
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    EventType = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Float)
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


alert_headers = {'AlertId': 'int',
                 'AssetSiteName': 'string',
                 'ReportGroup': 'string',
                 'AssetName': 'string',
                 'AssetExtra': 'string',
                 'Drivers_ID': 'int',
                 'Asset2SiteName': 'string',
                 'Asset2ReportGroup': 'string',
                 'AssetName2': 'string',
                 'AssetExtra2': 'string',
                 'AssetID2': 'int',
                 'EventKey': 'int',
                 'EventDescription': 'string',
                 'EventType': 'string',
                 'EventStartDate': 'string',
                 'EventStartTime': 'string',
                 'EventEndDate': 'string',
                 'EventEndTime': 'string',
                 'TimeZone': 'string',
                 'TotalOccurs': 'int',
                 'EventValue': 'float',
                 'Textbox20': 'string',
                 'RoadSpeedLimit': 'string',
                 'OverspeedLocation': 'string',
                 'TotalDuration': 'string',
                 'StartOdo': 'float',
                 'EndOdo': 'float',
                 'F_StartStreet': 'string',
                 'F_StartSuburb': 'string',
                 'F_EndStreet': 'string',
                 'F_EndSuburb': 'string',
                 'StartLocation': 'string',
                 'EndLocation': 'string',
                 'StartLongLat': 'string',
                 'EndLongLat': 'string',
                 'FuelUsed': 'float',
                 'Distance': 'float'}

alert_order = ['AlertId',
               'AssetSiteName',
               'ReportGroup',
               'AssetName',
               'AssetExtra',
               'Drivers_ID',
               'Asset2SiteName',
               'Asset2ReportGroup',
               'AssetName2',
               'AssetExtra2',
               'AssetID2',
               'EventKey',
               'EventDescription',
               'EventType',
               'EventStartDate',
               'EventStartTime',
               'EventEndDate',
               'EventEndTime',
               'TimeZone',
               'TotalOccurs',
               'EventValue',
               'Textbox20',
               'RoadSpeedLimit',
               'OverspeedLocation',
               'TotalDuration',
               'StartOdo',
               'EndOdo',
               'F_StartStreet',
               'F_StartSuburb',
               'F_EndStreet',
               'F_EndSuburb',
               'StartLocation',
               'EndLocation',
               'StartLongLat',
               'EndLongLat',
               'FuelUsed',
               'Distance']

event_other_header = {
                 'AssetSiteName': 'string',
                 'ReportGroup': 'string',
                 'AssetName': 'string',
                 'AssetExtra': 'string',
                 'Drivers_ID': 'int',
                 'Asset2SiteName': 'string',
                 'Asset2ReportGroup': 'string',
                 'AssetName2': 'string',
                 'AssetExtra2': 'string',
                 'AssetID2': 'int',
                 'EventKey': 'int',
                 'EventDescription': 'string',
                 'EventType': 'string',
                 'EventStartDate': 'string',
                 'EventStartTime': 'string',
                 'EventEndDate': 'string',
                 'EventEndTime': 'string',
                 'TimeZone': 'string',
                 'TotalOccurs': 'int',
                 'EventValue': 'float',
                 'Textbox20': 'string',
                 'RoadSpeedLimit': 'string',
                 'OverspeedLocation': 'string',
                 'TotalDuration': 'string',
                 'StartOdo': 'float',
                 'EndOdo': 'float',
                 'F_StartStreet': 'string',
                 'F_StartSuburb': 'string',
                 'F_EndStreet': 'string',
                 'F_EndSuburb': 'string',
                 'StartLocation': 'string',
                 'EndLocation': 'string',
                 'StartLongLat': 'string',
                 'EndLongLat': 'string',
                 'FuelUsed': 'float',
                 'Distance': 'float'}

event_other_order = [
               'AssetSiteName',
               'ReportGroup',
               'AssetName',
               'AssetExtra',
               'Drivers_ID',
               'Asset2SiteName',
               'Asset2ReportGroup',
               'AssetName2',
               'AssetExtra2',
               'AssetID2',
               'EventKey',
               'EventDescription',
               'EventType',
               'EventStartDate',
               'EventStartTime',
               'EventEndDate',
               'EventEndTime',
               'TimeZone',
               'TotalOccurs',
               'EventValue',
               'Textbox20',
               'RoadSpeedLimit',
               'OverspeedLocation',
               'TotalDuration',
               'StartOdo',
               'EndOdo',
               'F_StartStreet',
               'F_StartSuburb',
               'F_EndStreet',
               'F_EndSuburb',
               'StartLocation',
               'EndLocation',
               'StartLongLat',
               'EndLongLat',
               'FuelUsed',
               'Distance']


class GPS(Base):
    __tablename__ = 'GPS'

    liGPSID = Column(Integer, primary_key=True)
    iVehicleID = Column(Integer)
    iDriverID = Column(Integer)
    iOriginalDriverID = Column(Integer)
    liBlockSeq = Column(String(512))
    dtTime = Column(String(1024))
    fLatitude = Column(Float)
    fLongitude = Column(Float)
    iAltitude = Column(Integer)
    iHeading = Column(Integer)
    ucSatellites = Column(Integer)
    fHDOP = Column(Integer)
    liAgeOfReading = Column(Integer)
    liDistanceSinceReading = Column(Integer)
    ucVelocity = Column(Integer)


gps_headers = {'liGPSID': 'int',
               'iVehicleID': 'int',
               'iDriverID': 'int',
               'iOriginalDriverID': 'int',
               'liBlockSeq': 'string',
               'dtTime': 'string',
               'fLatitude': 'float',
               'fLongitude': 'float',
               'iAltitude': 'int',
               'iHeading': 'int',
               'ucSatellites': 'int',
               'fHDOP': 'int',
               'liAgeOfReading': 'int',
               'liDistanceSinceReading': 'int',
               'ucVelocity': 'int'}

gps_order = ['liGPSID',
             'iVehicleID',
             'iDriverID',
             'iOriginalDriverID',
             'liBlockSeq',
             'dtTime',
             'fLatitude',
             'fLongitude',
             'iAltitude',
             'iHeading',
             'ucSatellites',
             'fHDOP',
             'liAgeOfReading',
             'liDistanceSinceReading',
             'ucVelocity']


class EventOther(Base):
    __tablename__ = 'EventOther'

    EventOtherId = Column(Integer, primary_key=True)
    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    Drivers_ID = Column(Integer)
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    EventType = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Float)
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


class EventSpeed(Base):
    __tablename__ = 'EventSpeed'

    AlertId = Column(Integer, primary_key=True)
    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    Drivers_ID = Column(Integer)
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    EventType = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Float)
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


class EventCorner(Base):
    __tablename__ = 'EventCorner'

    EventCornerId = Column(Integer, primary_key=True)
    AssetSiteName = Column(String(512))
    ReportGroup = Column(String(512))
    AssetName = Column(String(512))
    AssetExtra = Column(String(512))
    AssetID = Column(String(512))
    Asset2SiteName = Column(String(512))
    Asset2ReportGroup = Column(String(512))
    AssetName2 = Column(String(512))
    AssetExtra2 = Column(String(512))
    AssetID2 = Column(Integer)
    EventKey = Column(Integer)
    EventDescription = Column(String(512))
    Month = Column(String(512))
    EventStartDate = Column(String(512))
    EventStartTime = Column(String(512))
    EventEndDate = Column(String(512))
    EventEndTime = Column(String(512))
    TimeZone = Column(String(512))
    TotalOccurs = Column(Integer)
    EventValue = Column(Float)
    Cat = Column(String(512))


class Trip(Base):
    __tablename__ = 'Trips'

    TripUID = Column(Integer, primary_key=True)
    Date = Column(String(512))
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
    ActivityStartDateTime = Column(String(512))
    DepartureTime = Column(String(512))
    ArrivalTime = Column(String(512))
    ActivityEndDateTime = Column(String(512))
    TimeZone = Column(String(512))
    DrivingTimePercentage = Column(String(512))
    StandingTimePercentage = Column(String(512))
    IdleTimePercentage = Column(String(512))
    TotalDrivingTime = Column(String(512))
    TotalStandingTime = Column(String(512))
    TotalDuration = Column(String(512))
    TotalIdleTime = Column(String(512))
    ParkingTime = Column(String(512))
    StartOdometer = Column(Float)
    EndOdometer = Column(Float)
    TotalDistanceTravelled = Column(Float)
    TotalFuelUsed = Column(Float)
    FuelConsumptionMeasured = Column(Float)
    TotalCO2Emission = Column(Float)
    TotalEngineSeconds = Column(String(512))
    AverageSpeed = Column(Float)
    MaxSpeed = Column(Float)


event_corner_headers = {
                        'AssetSiteName': 'string',
                        'ReportGroup': 'string',
                        'AssetName': 'string',
                        'AssetExtra': 'string',
                        'AssetID': 'string',
                        'Asset2SiteName': 'string',
                        'Asset2ReportGroup': 'string',
                        'AssetName2': 'string',
                        'AssetExtra2': 'string',
                        'AssetID2': 'int',
                        'EventKey': 'int',
                        'EventDescription': 'string',
                        'Month': 'string',
                        'EventStartDate': 'string',
                        'EventStartTime': 'string',
                        'EventEndDate': 'string',
                        'EventEndTime': 'string',
                        'TimeZone': 'string',
                        'TotalOccurs': 'int',
                        'EventValue': 'float',
                        'Cat': 'string'}

event_corner_order = [
                      'AssetSiteName',
                      'ReportGroup',
                      'AssetName',
                      'AssetExtra',
                      'AssetID',
                      'Asset2SiteName',
                      'Asset2ReportGroup',
                      'AssetName2',
                      'AssetExtra2',
                      'AssetID2',
                      'EventKey',
                      'EventDescription',
                      'Month',
                      'EventStartDate',
                      'EventStartTime',
                      'EventEndDate',
                      'EventEndTime',
                      'TimeZone',
                      'TotalOccurs',
                      'EventValue',
                      'Cat']


trips_header = {'TripUID': 'int',
                'Date': 'string',
                'AssetName': 'string',
                'AssetID': 'int',
                'AssetExtra': 'string',
                'AssetName2': 'string',
                'AssetID2': 'int',
                'AssetExtra2': 'string',
                'SiteName': 'string',
                'OriginalDriverName': 'string',
                'TrailerInfo': 'string',
                'TripID': 'int',
                'ActivityStartDateTime': 'string',
                'DepartureTime': 'string',
                'ArrivalTime': 'string',
                'ActivityEndDateTime': 'string',
                'TimeZone': 'string',
                'DrivingTimePercentage': 'string',
                'StandingTimePercentage': 'string',
                'IdleTimePercentage': 'string',
                'TotalDrivingTime': 'string',
                'TotalStandingTime': 'string',
                'TotalDuration': 'string',
                'TotalIdleTime': 'string',
                'ParkingTime': 'string',
                'StartOdometer': 'float',
                'EndOdometer': 'float',
                'TotalDistanceTravelled': 'float',
                'TotalFuelUsed': 'float',
                'FuelConsumptionMeasured': 'float',
                'TotalCO2Emission': 'float',
                'TotalEngineSeconds': 'string',
                'AverageSpeed': 'float',
                'MaxSpeed': 'float'}

trips_order = ['TripUID',
               'Date',
               'AssetName',
               'AssetID',
               'AssetExtra',
               'AssetName2',
               'AssetID2',
               'AssetExtra2',
               'SiteName',
               'OriginalDriverName',
               'TrailerInfo',
               'TripID',
               'ActivityStartDateTime',
               'DepartureTime',
               'ArrivalTime',
               'ActivityEndDateTime',
               'TimeZone',
               'DrivingTimePercentage',
               'StandingTimePercentage',
               'IdleTimePercentage',
               'TotalDrivingTime',
               'TotalStandingTime',
               'TotalDuration',
               'TotalIdleTime',
               'ParkingTime',
               'StartOdometer',
               'EndOdometer',
               'TotalDistanceTravelled',
               'TotalFuelUsed',
               'FuelConsumptionMeasured',
               'TotalCO2Emission',
               'TotalEngineSeconds',
               'AverageSpeed',
               'MaxSpeed']

Base.metadata.create_all(engine)


def cast_types(col_num, val, order, headers):
    col_type = headers[order[col_num]]
    if val.strip() == '':
        return None
    if col_type == 'int':
        return int(val)
    elif col_type == 'float':
        return float(val.replace(',', ''))
    return val


def upload_csv(csv_path, csv_name, order, headers, model, needs_id=False, has_headers=True, chuck_upload=False):
    with open(os.path.join(csv_path, csv_name)) as csvf:
        session = Session()
        rr = csv.reader(csvf, delimiter=',')
        rows = []
        if has_headers:
            next(rr)
        if chuck_upload:
            chunk_size = 50000
        row_count = 0
        for k, r in enumerate(rr):
            row_dict = {}
            if needs_id:
                r = [str(k)] + r
            for i, c in enumerate(r):
                row_dict[order[i]] = cast_types(i, c, order, headers)
            rows.append(model(**row_dict))
            if row_count > chunk_size:
                print('chunk')
                row_count = 0
                session.add_all(rows)
                session.commit()
                rows = []
                print('chunkuploaded')
            row_count += 1
            print('added')
            session.add(rows.pop())
            session.commit()
        # session.add_all(rows)
        session.commit()
        print('finished upload')


# upload_csv(gps_path, gps_file, gps_order, gps_headers, GPS, chuck_upload=True)
# upload_csv(event_path, event_corner_file, event_corner_order, event_corner_headers, EventCorner, chuck_upload=True, needs_id=False)
# upload_csv(event_path, event_speed_file, alert_order, alert_headers, EventSpeed, chuck_upload=True, needs_id=True)
upload_csv(event_path, event_other_file, event_other_order, event_other_header, EventOther, chuck_upload=True, needs_id=False)
# upload_csv(trip_path, trip_file, trips_order, trips_header, Trip, chuck_upload=True, needs_id=True)
