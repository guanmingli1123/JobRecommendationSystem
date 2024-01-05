import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    df_job = pd.read_csv('finaljob.csv')
    return df_job

# Load the saved logistic regression model
lrg_model = joblib.load('logistic_regression_model.joblib')

# Load the vectorizer from the saved model
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def filter_jobs(df, qualification=None, work=None, country=None):
    if qualification:
        df = df[df['Qualifications'] == qualification]
    if work:
        df = df[df['Work Type'] == work]
    if country:
        df = df[df['Country'] == country]
    return df

def job():

    # Streamlit app
    st.markdown("# Job Recommendation🎯")
    st.markdown("Select your education level, preferred work type, country and enter skills acquired to get your job recommendation!")

    df_job = load_data()
    qualification = st.selectbox('Education Level', df_job['Qualifications'].unique())
    work = st.selectbox('Preferred Work Type', df_job['Work Type'].unique())
    country = st.selectbox('Country', df_job['Country'].unique())
    # Apply filters
    filtered_df = filter_jobs(df_job, qualification, work, country)
    
    user_input = st.text_input("Skills Acquired:")

    start_recommendation = st.button("Recommend")

    if start_recommendation:

        # Vectorize user input using the loaded vectorizer
        pred = vectorizer.transform([user_input.lower()])

        # Predict the label using the logistic regression model
        output = lrg_model.predict(pred)
        
        labelData = filtered_df[filtered_df['label'].astype(str).str.lower() == str(output[0]).lower()]
        cos = []

        for index, row in labelData.iterrows():
            skills = [row['skills']]
            skillsVec = vectorizer.transform(skills)
            cos_lib = cosine_similarity(skillsVec, pred)
            cos.append(cos_lib[0][0])

        labelData['cosine_similarity'] = cos  # Fix column name here

        # Sort the DataFrame by cosine similarity and show top 5 recommendations
        recommended = labelData.sort_values('cosine_similarity', ascending=False).head(20)[['Job Title', 'Qualifications', 'Job Description', 'Company', 'Work Type', 'skills', 'Responsibilities', 'Benefits', 'location', 'Country', 'Contact Person', 'Contact']]

        # Display filtered results
        for index, row in recommended.iterrows():
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
    job()
