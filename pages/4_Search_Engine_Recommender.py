import streamlit as st
import sys
import pandas as pd

# Setting path to parent Folder
sys.path.append('../ETDS Project')
from scripts.search_engine_script import search_games

df_recommender = pd.read_csv('./exports/recommender_file_main.csv')

#Page config
st.set_page_config(
    page_title="Game Recommender",
    page_icon="https://img.icons8.com/?size=48&id=zNqjI8XKkCv0&format=png",
)


#Page data
st.markdown("""# Search Engine Based Recommender""")

st.markdown("""Working: The BM25 Search Engine is used to search for the user's game description in the game corpus. 
            The games are suggested to the user based on the top scores returned by the engine.""")

st.markdown(""" To learn more about the Rank-BM25 search engine, visit: https://pypi.org/project/rank-bm25/""")

#Taking game title
desc = st.text_input("What are we looking for today?",key = "title")
values = st.slider("Price Range", 0, 999, (25,75))
n_recommends = st.slider("No of Recommendations", 0, 100, 10)

#Button Click Definition
if st.button("Search!"):
    df = search_games(desc, values, n_recommends)
    st.dataframe(df)