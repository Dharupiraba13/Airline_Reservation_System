import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Ticket Charges")
st.title("Total Charges")


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

    return df
"## Total price of a ticket"
"The total price of a ticket given its Ticket ID is displayed by adding the actual price of the ticket and any additional charges present for that Ticket."
#st.write("The total charge of ticket including the ticket price and any additional charges is displayed")
sql_ticket_ids = "SELECT Ticket_id FROM Tickets;"
try:
    ticket_ids = query_db(sql_ticket_ids)["ticket_id"].tolist()
    Ticket_id = st.selectbox("Choose a Ticket ID", ticket_ids)
    #st.write(f"the ticket id is {Ticket_id}")
except:
    st.write("Sorry! Something went wrong with your query, please try again.")
if Ticket_id:
        sql_order = f"""
             SELECT {Ticket_id} as Ticket_ID,Co.Amount as Ticket_price,Ch.charge_amount as Additional_Charges,
             (Co.Amount+Ch.charge_amount) as Total_price
             from Costs Co,Charges Ch, Tickets T,Tickets_have_Charges T1
             where T.Cost_id=Co.Cost_id and {Ticket_id}=T1.Ticket_id
             and T1.Charge_id=Ch.Charge_id;"""
st.write("The total price for the Ticket is:")
try:
        ticket_info = query_db(sql_order).loc[0]
        st.dataframe(ticket_info)
        if (ticket_info.empty):
            st.write(f"There are no charges for the ticket id {Ticket_id}.")
except:
        st.write("Sorry! Something went wrong with your query, please try again.")

"## Estimation of Ticket Prices"
"The price of a ticket can be estimated based on the passenger type, class, seat location and additional charges like baggage, cancellation fees etc. The estimation of a ticket price is calculated by adding the minimum price of the particualr seat,class and location and the minimum price of the additional charges for a particular charge type. "
sql_all_types = "SELECT distinct C.Type as type FROM Costs C;"
sql_all_class = "SELECT distinct C.Class as class FROM Costs C;"
sql_all_location = "SELECT distinct C.Location as location FROM Costs C;"
sql_all_chargetype = "SELECT distinct C.Charge_type as charge_type FROM Charges C;"
try:
    all_types = query_db(sql_all_types)["type"].tolist()
    type_name= st.selectbox("Choose a passenger type", all_types)
    all_class = query_db(sql_all_class)["class"].tolist()
    class_name= st.selectbox("Choose a class", all_class)
    all_location = query_db(sql_all_location)["location"].tolist()
    location_name= st.selectbox("Choose a passenger type", all_location)
    all_chargetype = query_db(sql_all_chargetype)["charge_type"].tolist()
    charge_name= st.selectbox("Choose a additional charge type", all_chargetype)

except:
    st.write("Sorry! Something went wrong with your query, please try again.")

st.write("The estimated ticket price of a passenger is displayed.")
sql_est=f"SELECT C.Type,C.Class,C.Location,Ch.Charge_type,(MIN(C.Amount)+MIN(Ch.charge_amount)) as Estimated_price from Costs C,Charges Ch where C.type='{type_name}' and C.class='{class_name}' and C.Location='{location_name}' and Ch.charge_type='{charge_name}' group by C.Type,C.Class,C.Location,Ch.Charge_type;"
#sql_time=f"SELECT f.flight_id, f.flight_name,f.departure_time, CASE WHEN EXTRACT(HOUR FROM f.departure_time) BETWEEN 0 AND 6 OR EXTRACT(HOUR FROM f.departure_time) BETWEEN 18 AND 23 THEN 'night' ELSE 'day' END AS time_of_day from flights f group by f.flight_id order by time_of_day asc,f.departure_time;"
try:
            df = query_db(sql_est)
            if df.shape[0]==0:
                st.success("Sorry! There are currently no flights from "+source_airport_name+" to "+destination_airport_name)
            else:
                st.dataframe(df)
            #st.dataframe(df)

except:
            st.write("Sorry! Something went wrong with your query, please try again.")
