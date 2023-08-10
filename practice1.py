import streamlit
#import pymongo
#conn_obj=pymongo.mongoclient(**streamlit.secrets["mongo"])
conn_obj=mongoclient(**streamlit.secrets["mongo"])
db_obj=conn_obj['Demo']
collection_obj=db_obj['Employee']
