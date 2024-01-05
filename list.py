import pandas as pd
import streamlit as st

def load_data():
    df_job = pd.read_csv('finaljob.csv')
    return df_job

def filter_jobs(df, qualification=None, work=None, country=None, location=None, position=None, salary=None):
    if qualification:
        df = df[df['Qualifications'] == qualification]
    if work:
        df = df[df['Work Type'] == work]
    if country:
        df = df[df['Country'] == country]
    if location:
        df = df[df['location'] == location]
    if position:
        df = df[df['Job Title'] == position]
    if salary:
        min_salary, max_salary = salary
        df = df[(df['Minimum Salary(k)'] >= min_salary) & (df['Maximum Salary(k)'] <= max_salary)]
    return df

def listing():

    df_job = load_data()

    st.markdown("# Job Postings🔍")

    st.markdown("##### All available job postings are listed here! Discover your interested jobs now.")

    # Sidebar for filters
    st.sidebar.markdown("## Filters")
    apply_qualification_filter = st.sidebar.checkbox("Apply Qualification Filter")
    apply_work_filter = st.sidebar.checkbox("Apply Work Type Filter")
    apply_country_filter = st.sidebar.checkbox("Apply Country Filter")
    apply_location_filter = st.sidebar.checkbox("Apply Location Filter")
    apply_position_filter = st.sidebar.checkbox("Apply Position Filter")
    apply_salary_filter = st.sidebar.checkbox("Set Salary Range")

    if apply_qualification_filter:
        qualification = st.sidebar.selectbox('Education', df_job['Qualifications'].unique())
    else:
        qualification = None

    if apply_work_filter:
        work = st.sidebar.selectbox('Work Type', df_job['Work Type'].unique())
    else:
        work = None

    if apply_country_filter:
        country = st.sidebar.selectbox('Country', df_job['Country'].unique())
    else:
        country = None

    if apply_location_filter:
        location = st.sidebar.selectbox('location', df_job['location'].unique())
    else:
        location = None

    if apply_position_filter:
        position = st.sidebar.selectbox('Job Title', df_job['Job Title'].unique())
    else:
        position = None

    if apply_salary_filter:
        salary = st.sidebar.slider('Year Salary Range(k)', min_value=df_job['Minimum Salary(k)'].min(),
                                    max_value=df_job['Maximum Salary(k)'].max(), value=(0, 150))
    else:
        salary = None
    
    
    # Apply filters
    filtered_df = filter_jobs(df_job, qualification, work, country, location, position, salary)
    # Display filtered results
    for index, row in filtered_df.iterrows():
        expander_label = f"{row['Job Title']} - {row['Company']}"
        with st.expander(expander_label):
            st.markdown(f"**Job Title:** {row['Job Title']}")
            st.markdown(f"**Company:** {row['Company']}")
            st.markdown(f"**Qualification Level:** {row['Qualifications']}")
            st.markdown(f"**Work Type:** {row['Work Type']}")
            st.markdown(f"**Job Description:** {row['Job Description']}")
            st.markdown(f"**Skills Required:** {row['skills']}")
            st.markdown(f"**Responsibilities:** {row['Responsibilities']}")
            st.markdown(f"**Benefits:** {row['Benefits']}")
            st.markdown(f"**Country:** {row['Country']}")
            st.markdown(f"**Location:** {row['location']}")
            st.markdown(f"**Contact Person:** {row['Contact Person']}")
            st.markdown(f"**Contact:** {row['Contact']}")

if __name__ == "__main__":
    listing()
