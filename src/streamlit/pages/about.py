import streamlit as st
import os







def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



st.header(":mailbox: Get In Touch With Me!")
st.markdown(
        '''
           Do you want to propose us ideas or contribute in some way to our community?
           Send us an email with your proposals/ideas and we will reply to you as soon as possible.
        '''
    )