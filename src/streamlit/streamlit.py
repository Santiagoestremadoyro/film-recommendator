import streamlit as st

st.markdown("<h1 style='text-decoration: underline;'>Film Recommendator!!</h1>", unsafe_allow_html=True)
st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")

st.button("Empecemos")
st.slider("Cueantas recomendaciones quieres ver", 0, 50)









