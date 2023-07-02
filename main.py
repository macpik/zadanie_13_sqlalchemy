from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///przetestujmy.db')

meta = MetaData()

clean_stations = Table (
    'clean_stations', meta,
    Column('id', Integer, primary_key = True),
    Column('station', String),
    Column('latitude', String),
    Column('longitude', String),
    Column('elevation', String),
    Column('name', String),
    Column('country', String),
    Column('state', String),
)

clean_measure = Table (
    'clean_measure', meta,
    Column('id', Integer, primary_key = True),
    Column('station_id', String),
    Column('date', String),
    Column('precip', String),
    Column('tobs', String),
)

meta.create_all(engine)

ins = clean_stations.insert()

ins = clean_stations.insert().values(station="USC00519397", latitude="21.2716", longitude="-157.8168", elevation="3.0", name="WAIKIKI 717.2", country="US", state="HI")

conn = engine.connect()
result = conn.execute(ins)

ins_2 = clean_measure.insert()

ins_2 = clean_measure.insert().values(station_id="USC00519397", date="2010-01-01", precip="0.08", tobs="65")

conn = engine.connect()
result = conn.execute(ins_2)

conn = engine.connect()
selector_clean_stations = clean_stations.select().where(clean_stations.c.id>0)
result = conn.execute(selector_clean_stations)

for row in result:
    print(row)
