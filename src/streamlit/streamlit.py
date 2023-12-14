import streamlit as st

<<<<<<< HEAD
st.markdown("<h1 style='text-decoration: underline;'>Film Recommendator!!</h1>", unsafe_allow_html=True)
st.markdown(
        '''
                Discover the best movies, of any genre in our vast catalog of movies and find your new favorite movie/series!!
        '''
    )
=======
>>>>>>> a81706fadadb93c3bc9e0b422257575914dc5b40

st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")


st.slider("Cueantas recomendaciones quieres ver", 0, 50)

selectbox = st.selectbox("What genre would you like to see?", ["Action", "Romance", "Thriler"])





st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)










<<<<<<< HEAD


=======
>>>>>>> a81706fadadb93c3bc9e0b422257575914dc5b40
