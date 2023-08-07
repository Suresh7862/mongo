import streamlit
import pymongo
conn_obj=pymongo.mongoclient(**streamlit.secrets["mongo"])
print(type(conn_obj))
