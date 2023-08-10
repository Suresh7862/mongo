import streamlit
import pymongo
conn_obj=pymongo.Mongoclient(**streamlit.secrets["mongo"])
db_obj=conn_obj['Demo']
collection_obj=db_obj['Employee']
