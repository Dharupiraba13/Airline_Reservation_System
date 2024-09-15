import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

st.set_page_config(page_title="Recommendation Lists")
st.title("Recommendation Lists")


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

"## Recommedation List based on popularity"
"A recommendation list of flights for passengers is displayed by sorting the Flight name and the most number of bookings made for that particular flight."
st.write("A curated list of flights with the most popularity among passengers.")

sql_pop=f"select F.Flight_name,COUNT(*) as Number_of_bookings_made from Flights F, Tickets T where F.Flight_id=T.Flight_id group by F.Flight_name order by COUNT(*) desc;"
try:
        df = query_db(sql_pop)
        st.dataframe(df)
except:
        st.write("Sorry! Something went wrong with your query, please try again.")

"## Recommedation List based on affordable price"
"A recommendation list of flights for passengers is displayed by sorting the Flight name and the cheapest price for that particular flight."

st.write("A curated list of flights with the most affordable ticket prices.")

sql_price=f"select F.Flight_name,MIN(C.Amount) as Minimum_Cost from Flights F, Tickets T, Costs C where F.Flight_id=T.Flight_id and T.Cost_id=C.Cost_id group by F.Flight_name order by MIN(C.Amount) asc;"
#st.dataframe(df)
try:
        df = query_db(sql_price)
        st.dataframe(df)
except:
        st.write("Sorry! Something went wrong with your query, please try again.")


"## Best Flights to travel"
"A list of best flights for passengers is displayed by the Flight name having the most number of bookings as well as cheapest price for that particular flight."

st.write("A curated list of flights with the best price and more bookings.")

sql_reco = f"select F.Flight_name from Flights F, Tickets T, Costs C where F.Flight_id=T.Flight_id and T.Cost_id=C.Cost_id group by F.Flight_name HAVING COUNT(*) > 0 AND AVG(C.Amount) > 0 order by COUNT(*) desc,AVG(C.Amount) asc;"
#df = query_db(sql_reco)
#st.dataframe(df)
try:
        df = query_db(sql_reco)

        st.dataframe(df)
except:
        st.write("Sorry! Something went wrong with your query, please try again.")
