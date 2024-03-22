
import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("nearest_asteroid", type=GSheetsConnection)

df = conn.read()

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
