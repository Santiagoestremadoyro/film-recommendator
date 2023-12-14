import streamlit as st

st.markdown("<h1 style='text-decoration: underline;'>Film Recommendator!!</h1>", unsafe_allow_html=True)
st.markdown(
        '''
                Discover the best movies, of any genre in our vast catalog of movies and find your new favorite movie/series!!
        '''
    )

st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")


st.slider("Cueantas recomendaciones quieres ver", 0, 50)

selectbox = st.selectbox("What genre would you like to see?", ["Action", "Romance", "Thriler"])

















