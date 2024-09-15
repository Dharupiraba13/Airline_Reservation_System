import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Statistical Descriptions")
st.title("Statistical Descriptions")


@st.cache
def get_config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}


@st.cache(allow_output_mutation=True)
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
    df = df.round(1)
    return df

"Understanding the min, max values could help passenger make choices with their trip."
# A dictionary to make it easier for user to understand the choices
min_choices = {'Number of Stops':'MIN(R.stops) as min_number_of_stops','Cost':'MIN(C.amount) as min_cost','Capacity': 'MIN(A.capacity) as min_total_seat_capacity'}
max_choices = {'Number of Stops':'MAX(R.stops) as max_number_of_stops','Cost':'MAX(C.amount) as max_cost','Capacity': 'MAX(A.capacity) as max_total_seat_capacity'}
groupby_choices = {'Flight names': 'F.flight_name','Source Airport':'R.source','Destination Airport':'R.destination'}
"These are the current options available to check the aggregates - Number of Stops, Costs of a flight and Total Seat capacity."
min_options = st.multiselect('Minimum of What should be checked?',['Number of Stops','Cost','Capacity'],['Capacity'])
max_options = st.multiselect('Maximum of What should be checked?',['Number of Stops','Cost','Capacity'],['Capacity'])
"Select what values to visualize along with the aggregates. Currently the choices are Flight names, Source airport, Destination airport."
groupby_options = st.multiselect("Which values should be used to see the aggregates independently",['Flight names','Source Airport','Destination Airport'],['Flight names'])
if min_options or max_options:
    query_str = ""
    groupby_str = ""
    for i in groupby_options:
        query_str = query_str+groupby_choices[i] + ","
        groupby_str = groupby_str+groupby_choices[i]+","
    for i in min_options:
        query_str = query_str +min_choices[i] + ","
    for i in max_options:
        query_str = query_str +max_choices[i] + ","
    query_str = query_str[:-1]
    groupby_str = groupby_str[:-1]
    sql_table = f"SELECT {query_str} FROM flights F, Aircrafts A, departfrom_Routes_arriveto R, Costs C,have_Seats S where C.Cost_id = S.Cost_id and S.flight_id = F.flight_id and A.aircraft_id = F.aircraft_id and R.route_id = F.route_id group by {groupby_str};"
    try:
        df = query_db(sql_table)
        f"Display the Aggregates"
        st.write(df)
        if df.empty:
            st.success("Sorry! There are no such aggregates available!")
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again."
        )

st.sidebar.success("Select pages here!")
