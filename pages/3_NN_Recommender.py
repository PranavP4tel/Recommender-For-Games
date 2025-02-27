import streamlit as st
import sys
import pandas as pd

# Setting path to parent Folder
sys.path.append('../ETDS Project')
from nn_recommender_script import recommend_game

df_recommender = pd.read_csv('recommender_file_main.csv')

#Page config
st.set_page_config(
    page_title="Game Recommender",
    page_icon="https://img.icons8.com/?size=48&id=zNqjI8XKkCv0&format=png",
)


#Page data
st.markdown("""# Nearest Neighbors Based Recommender""")

st.markdown("""This app allows you to get recommendations, by providing the nearest games to the one entered by the user.""")

#Taking game title
st.selectbox("Select a title", df_recommender['name_translated'] ,key = "title")
st.number_input('Enter number of recommendations', key = 'n_recommendations', step = 1, min_value = 2, max_value = 50)

#Button Click Definition
if st.button("Search!"):   
    df = recommend_game(game_title = st.session_state.title, n_recommendations = st.session_state.n_recommendations)
    st.dataframe(df)