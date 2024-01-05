import streamlit as st
from home import home
from list import listing
from recommendation import job
from eda import eda
from about import about


# Define the navigation menu
pages = {
    "🏠 Home": home,
    "🔎 Job Postings": listing,
    "🎯 Recommendation": job,
    "📊 Visualization": eda,
    "📝 About": about
}

# Display the navigation menu in the sidebar
st.sidebar.title("Menu")
selected_page = st.sidebar.selectbox("", list(pages.keys()))

# Display content based on the selected page
pages[selected_page]()
