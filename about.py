import streamlit as st

def about():

    st.markdown("# About📝")

    tab1, tab2, tab3= st.tabs(["How to Use?", "Pages Overview", "Project Overview"])

    with tab2:

        st.markdown("#### ")

        st.markdown("##### 🏠 Home")
        st.markdown(
            "The entry point which provides a brief overview of the application and invites users "
            "to explore personalized job recommendations."
        )
        st.markdown("##### ")

        st.markdown("##### 💡 User Guide")
        st.markdown(
            "This page serves as a guide to help users "
            "navigate through the application and understand its features."
        )
        st.markdown("##### ")

        st.markdown("##### 🎯 Recommendation")
        st.markdown(
            "Users receive personalized job recommendations based on their skills and preferences. "
        )
        st.markdown("##### ")

        st.markdown("##### 📊 Visualization")
        st.markdown(
            "This page illustrates various visualization to gain valuable insights "
            "into the characteristics of the datasets."
        ) 
        st.markdown("##### ")
        
        st.markdown("##### 📝 About")
        st.markdown(
            "An overview of the project and the application."
        )  
        st.markdown("##### ") 
    
    with tab1: 

        st.markdown("##### ") 
        
        st.markdown("##### Step 1")
        st.markdown("Select the **Start Recommendation** button in the home page or select **🎯 Recommendation** from the side menu.")
        st.markdown("##### ") 

        st.markdown("##### Step 2")
        st.markdown("Enter the position you're interested in and the skills you've acquired or choose from the available options.")
        st.markdown("##### ") 

        st.markdown("##### Step 3")
        st.markdown("Select the **Recommend** button to proceed.")
        st.markdown("##### ") 

        st.markdown("##### Step 4")
        st.markdown("You will receive personalized job recommendations! Dive deeper into the job details by expanding the listings.")

    with tab3: 

        st.markdown("##### ") 

        st.markdown("The Job Recommendation System is designed to provide users with personalized job recommendations based on their skills and interests.")

        st.markdown("##### ") 
        st.markdown("##### Author")
        st.markdown("Guan Ming Li")
        st.markdown("Bachelor of Computer Science(Data Science)")
        st.markdown("University of Malaya")

        st.markdown("##### ") 
        st.markdown("##### Dataset Source")
        st.markdown("The job postings datasets used in this project are sourced from https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset")


if __name__ == "__main__":
    about()
