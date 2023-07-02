import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
       return conn
   except Error as e:
       print(e)

def execute_sql(conn, sql):
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

if __name__ == "__main__":

   create_clean_stations_sql = """
   -- clean_stations table
   CREATE TABLE IF NOT EXISTS clean_stations (
      id integer PRIMARY KEY,
      station text NOT NULL,
      latitude text NOT NULL,
      longitude text NOT NULL,
      elevation text NOT NULL,
      name text NOT NULL,
      country text NOT NULL,
      state text NOT NULL
   );
   """

   create_clean_measure_sql = """
   -- clean_measure table
   CREATE TABLE IF NOT EXISTS clean_measure (
      id integer PRIMARY KEY,
      station_id text NOT NULL, 
      date text NOT NULL,
      precip text NOT NULL,
      tobs text NOT NULL,
      FOREIGN KEY (station_id) REFERENCES clean_stations (station)
   );
   """

   db_file = "przetestujmy.db"

   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_clean_stations_sql)
       execute_sql(conn, create_clean_measure_sql)
       conn.close()
