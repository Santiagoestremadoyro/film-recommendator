import streamlit as st


st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")


st.button("Empecemos")
st.slider("Cueantas recomendaciones quieres ver", 0, 50)



st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)










