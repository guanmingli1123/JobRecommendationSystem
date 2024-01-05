import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud

st.set_option('deprecation.showPyplotGlobalUse', False)

def load_data():
    df_job = pd.read_csv('C:/Users/User/Desktop/WIH3001/Datasets/finaljob.csv')
    return df_job

def filter_position(df, qualification=None, work=None, country=None):
    if qualification:
        df = df[df['Qualifications'] == qualification]
    if work:
        df = df[df['Work Type'] == work]
    if country:
        df = df[df['Country'] == country]
    return df

def filter_job1(df, position1=None):
    if position1:
        df = df[df['Job Title'] == position1]
    return df

def filter_job2(df, position2=None):
    if position2:
        df = df[df['Job Title'] == position2]
    return df

def filter_job3(df, position3=None):
    if position3:
        df = df[df['Job Title'] == position3]
    return df

def eda():
    st.markdown("# Visualization📊")
    df_job = load_data()

    tab1, tab2, tab3, tab4 = st.tabs(["Positions", "Skills Required", "Locations", "Qualifications"])

    with tab1: 

        # Filters
        apply_qualification_filter = st.checkbox("Apply Qualification Filter", key="qualification_filter")
        apply_work_filter = st.checkbox("Apply Work Type Filter", key="work_filter")
        apply_country_filter = st.checkbox("Apply Country Filter", key="country_filter")

        if apply_qualification_filter:
            qualification = st.selectbox('Education', df_job['Qualifications'].unique(), key="qualification_dropdown")
        else:
            qualification = None

        if apply_work_filter:
            work = st.selectbox('Work Type', df_job['Work Type'].unique(), key="work_dropdown")
        else:
            work = None

        if apply_country_filter:
            country = st.selectbox('Country', df_job['Country'].unique(), key="country_dropdown")
        else:
            country = None

        # Apply filters
        filtered_df = filter_position(df_job, qualification, work, country)

        if not filtered_df.empty:
            st.markdown("### Positions with Most Job Postings")
            position_int = filtered_df['Job Title'].value_counts()
            position_int_counts = position_int.sort_values(ascending=False)
            top5_position_int = position_int_counts.head(5)
            fig = px.bar(top5_position_int, x=top5_position_int.index, y=top5_position_int, labels={'y': 'Count'}, color=top5_position_int)
            st.plotly_chart(fig)
        else:
            st.warning("No data available with selected filters.")
    
    with tab2:

        apply_position_filter = st.checkbox("Apply Position Filter", key="position1_filter")
        if apply_position_filter:
            position1 = st.selectbox('Position', df_job['Job Title'].unique(), key="position1_dropdown")
        else:
            position1 = None

        # Apply filters
        filtered_df1 = filter_job1(filtered_df, position1)

        if not filtered_df1.empty:
            st.markdown("### Skills Required")
            df_job['skills'].astype(str)
            skills = ' '.join(filtered_df1['skills'])
            wordcloud = WordCloud(width=600, height=400, background_color='#E3D5CA').generate(skills)
            st.image(wordcloud.to_array())
        else:
            st.warning("No data available with selected filters.")

    with tab3:   

        apply_position_filter2 = st.checkbox("Apply Position Filter", key="position2_filter")
        if apply_position_filter2:
            position2 = st.selectbox('Position', df_job['Job Title'].unique(), key="position2_dropdown")
        else:
            position2 = None

        # Apply filters
        filtered_df2 = filter_job2(filtered_df, position2)

        if not filtered_df2.empty:
            st.markdown("### Locations with Most Job Postings")
            loc = filtered_df2['location'].value_counts()
            loc_counts = loc.sort_values(ascending=False)
            top5_loc = loc_counts.head(5)
            fig = px.bar(top5_loc, x=top5_loc.index, y=top5_loc, labels={'y': 'Count'}, color=top5_loc)
            st.plotly_chart(fig)
        else:
            st.warning("No data available with selected filters.")
        
    with tab4:

        apply_position_filter3 = st.checkbox("Apply Position Filter", key="position3_filter")
        if apply_position_filter3:
            position3 = st.selectbox('Position', df_job['Job Title'].unique(), key="position3_dropdown")
        else:
            position3 = None

        # Apply filters
        filtered_df3 = filter_job3(filtered_df, position3)

        if not filtered_df3.empty:
            st.markdown("### Qualification Level")
            qua = filtered_df3['Qualifications'].value_counts()
            qua_counts = qua.sort_values(ascending=False)
            fig = px.bar(qua_counts, x=qua_counts.index, y=qua_counts, labels={'y': 'Count'}, color=qua_counts)
            st.plotly_chart(fig)
        else:
            st.warning("No data available with selected filters.")

if __name__ == "__main__":
    eda()
