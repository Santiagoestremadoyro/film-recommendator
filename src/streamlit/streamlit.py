import streamlit as st

st.markdown("<h1 style='text-decoration: underline;'>Film Recommendator!!</h1>", unsafe_allow_html=True)
st.subheader("Discover new movies or series in our collection. Enter your three favorite movies/series")


st.button("Empecemos")
st.slider("Cueantas recomendaciones quieres ver", 0, 50)

st.header(":mailbox: Get In Touch With Me!")
st.markdown(
        '''
           Do you want to propose us ideas or contribute in some way to our community?
           Send us an email with your proposals/ideas and we will reply to you as soon as possible.
        '''
    )

contact_form = """
<form action="https://formsubmit.co/little.big.whales@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""


st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)











st.button("Empecemos")
st.slider("Cueantas recomendaciones quieres ver", 0, 50)
