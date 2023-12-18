import streamlit as st



st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")


st.slider("Cueantas recomendaciones quieres ver", 0, 50)


selectbox = st.selectbox("What genre would you like to see?", ["Action", "Romance", "Thriler"])












