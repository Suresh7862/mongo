import streamlit
import pymongo
conn_obj=pymongo.mongoclient(**streamlit.secrets["mongo"])
