import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Charges Analysis")
st.title("Extra Charges Analysis")


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

    return df

"There are many reasons for why people have to pay extra charges for their tickets. By doing this analysis on it, people would be better prepared whenever they book their flights. The following can be used to rank flight companies, Seat Class and Seat Location based on the reason for the extra charges."
# A dictionary to make it easier for user to understand the charge types
all_charge_types = {"Ticket Cancellation":"Cancellation","Not Showing up for the flight":"No-show","Changes made to the ticket":"Changes","Extra baggage": "Extra"}
all_ranking_types = {"Flight Name":'F.flight_name',"Seat Location":'C.Location',"Seat Class": 'C.Class'}
rank_type = st.selectbox("Choose what ranking is needed", all_ranking_types)
charge_type = st.selectbox("Choose the Charge on which the ranking should be based on", all_charge_types.keys())
if charge_type and rank_type:
    charge_val = all_charge_types[charge_type]
    rank_val = all_ranking_types[rank_type]
    sql_table = f"SELECT {rank_val}, count(CH.charge_type) as Number_Of_Charges FROM flights F, Tickets T, Tickets_have_Charges TC, Charges CH, Costs C, have_Seats S where C.Cost_id = S.Cost_id and S.seat_number = T.seat_number and S.flight_id = T.flight_id and F.flight_id = T.flight_id and T.ticket_id = TC.ticket_id and TC.Charge_id = CH.charge_id and CH.charge_type like '{charge_val}%' group by {rank_val} order by count(CH.charge_type) desc;"
    # print(sql_table)
    try:
        df = query_db(sql_table)
        f"Most frequently the fee for {charge_type} is charged whenever {rank_type} is as {df.iloc[0,0]}."
        f"Display the Ranking for {rank_type}"
        st.dataframe(df)
        if df.empty:
            st.success("Sorry! There are no such charges!")
    except:
        st.write(
            "Sorry! Something went wrong with your query, please try again."
        )

st.sidebar.success("Select pages here!")
