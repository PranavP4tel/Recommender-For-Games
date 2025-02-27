import streamlit as st
import sys
import pandas as pd

# Setting path to parent Folder
sys.path.append('../ETDS Project')
from distance_recommender_script import recommender_distance

df_recommender = pd.read_csv('recommender_file_main.csv')

#Page config
st.set_page_config(
    page_title="Game Recommender",
    page_icon="https://img.icons8.com/?size=48&id=zNqjI8XKkCv0&format=png",
)


#Page data
st.markdown("""# Distance Based Recommender""")

st.markdown("""This app allows you to get recommendations as the closest games to the one entered by the user, based on user selected similarity measure.""")

#Taking game title
st.selectbox("Select a title", df_recommender['name_translated'] ,key = "title")

st.selectbox(
    "Select a similarity measure",
    ['Cosine Similarity','Manhattan Distance','Euclidean Distance'],    
 key = 'category'
    )

#Button Click Definition
if st.button("Search!"):
    df = recommender_distance(title = st.session_state.title, similarity=st.session_state.category.split(' ')[0])
    st.dataframe(df)