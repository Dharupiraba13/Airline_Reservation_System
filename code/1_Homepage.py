import datetime as dt
import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Flights")
st.title("Flights")


@st.cache
def get_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}


@st.cache()
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

"## Flight Schedule"
"People need to check flight schedules to reserve their tickets. Below once the source city is selected, only the available destinations are shown."

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
    f"Display the flight schedules"

    sql_table = f"SELECT F.flight_name, A1.city as source, A1.airport_name as Departure_Airport, F.Departure_date, F.Departure_time, F.Duration,A2.airport_name as Arrival_Airport, A2.city as destination, R.stops FROM flights F, departfrom_routes_arriveto R, Airports A1, Airports A2 where F.route_id = R.route_id and R.source = A1.airport_name and A1.city = '{source_name}' and R.destination = A2.airport_name and A2.city = '{destination_name}';"
    # print(sql_table)
    try:
        df = query_db(sql_table)
        if df.shape[0]==0:
            st.success("Sorry! There are currently no flights from "+source_airport_name+" to "+destination_airport_name)
        else:
            st.dataframe(df)
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again."
        )

st.sidebar.success("Select pages here!")
