import streamlit as st
from database import connection
import os


#conexion a la BD 
conn = connection.Database(
                os.getenv("MONGODB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL"))


st.markdow("<h1 style= 'text-decoration:'>Sign up to our communiy and hel us improve!</h1>", unsafe_allow_html=True)