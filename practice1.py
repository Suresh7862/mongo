import streamlit
import pymongo
conn_obj=pymongo.mongoclient(**streamlit.secrets["mongo"])
db_obj=conn_obj.list_database_names()
print(db_obj)
