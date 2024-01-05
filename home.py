import streamlit as st
from recommendation import job

def home():
    
    st.markdown("# Job Recommendation System💼")

    st.markdown("#### Unlock personalized job insights tailored just for you!")

    st.markdown(
        "Welcome to the Job Recommendation System👋🏻 This application provides you with personalized job insights "
        "based on your skills and interests. Enjoy a user-friendly recommendation system that makes job discovery a breeze. "
        "Receive handpicked job recommendations based on your skills and interests!🤩"
    )

    st.image('Image/home_job.png')

    if st.button("Start Recommendation"):
        job()

if __name__ == "__main__":
    home()
