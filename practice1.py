#pip install pymongo[srv]
import streamlit
import pymongo
conn_obj=pymongo.Mongoclient("mongodb+srv://streamlit.secrets.db_username:streamlit.secrets.db_pswd@streamlit.secrets.cluster_name.chzeolz.mongodb.net/?retryWrites=true&w=majority")
