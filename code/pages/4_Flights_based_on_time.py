import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Display Flights based on time")
st.title("Display Flights based on time")


@st.cache
def get_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}


@st.cache
def query_db(sql: str):
    # print(f"Running query_db(): {sql}")

    db_info = get_config()

    # Connect to an existing database
    conn = psycopg2.connect(**db_info)

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute(sql)

    # Obtain data
    data = cur.fetchall()

    column_names = [desc[0] for desc in cur.description]

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    df = pd.DataFrame(data=data, columns=column_names)
    if 'departure_time' in df.columns and df.shape[0]!=0:
            df['departure_time'] = pd.to_datetime(df['departure_time'],format='%H:%M:%S').dt.strftime('%H:%M')
    return df

"The details of flights available between a particular source and destination is taken and sorted based on the departure time of the flight. All flights between 6 AM to 6 PM refers as day time flights and the remaining flights as night time flights."
sql_all_source_names = "SELECT distinct A.City as source FROM departfrom_routes_arriveto R, Airports A where A.Airport_name = R.Source;"

try:
    all_source_names = query_db(sql_all_source_names)["source"].tolist()
    source_name= st.selectbox("Choose a source", all_source_names)
    if source_name:
            sql_all_destination_names = f"SELECT distinct A1.City as destination FROM departfrom_routes_arriveto R, Airports A1, Airports A2 where A1.Airport_name = R.destination and A2.airport_name = R.source and A2.city = '{source_name}'"
            all_destination_names = query_db(sql_all_destination_names)["destination"].tolist()
            destination_name= st.selectbox("Choose a destination", all_destination_names)
except:
    st.write("Sorry! Something went wrong with your query, please try again.")


if source_name and destination_name:
    #f"Display the flights available with the time"
    st.write("The details of flights available during day and night time are displayed.")
    sql_time=f"SELECT F.flight_id, F.flight_name,F.departure_time, CASE WHEN EXTRACT(HOUR FROM F.departure_time) BETWEEN 0 AND 6 OR EXTRACT(HOUR FROM F.departure_time) BETWEEN 18 AND 23 THEN 'night' ELSE 'day' END AS time_of_day from flights F,departfrom_routes_arriveto R, Airports A1, Airports A2 where F.route_id = R.route_id and R.source = A1.airport_name and A1.city = '{source_name}' and R.destination = A2.airport_name and A2.city = '{destination_name}'group by F.flight_id order by time_of_day asc,F.departure_time;"
    #sql_time=f"SELECT f.flight_id, f.flight_name,f.departure_time, CASE WHEN EXTRACT(HOUR FROM f.departure_time) BETWEEN 0 AND 6 OR EXTRACT(HOUR FROM f.departure_time) BETWEEN 18 AND 23 THEN 'night' ELSE 'day' END AS time_of_day from flights f group by f.flight_id order by time_of_day asc,f.departure_time;"
    try:
                df = query_db(sql_time)
                if df.shape[0]==0:
                    st.success("Sorry! There are currently no flights from "+source_airport_name+" to "+destination_airport_name)
                else:
                    st.dataframe(df)
                #st.dataframe(df)

    except:
                st.write("Sorry! Something went wrong with your query, please try again.")
