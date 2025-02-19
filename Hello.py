import streamlit as st

st.set_page_config(
    page_title="Game Recommender",
    page_icon="https://img.icons8.com/?size=48&id=zNqjI8XKkCv0&format=png",
)

st.write("# Welcome to our game recommender!")
st.write("### Ready To Play?")

st.sidebar.success("Select a page from the above.")

st.markdown(
    """
This project allows one to get recommendations for a title entered by the user (As long as the title is present in the dataset!).
Options available for the user are:
1. Filter Based - A simple filter based solution that provides games similar to the one entered by the user.
2. Distance Based - Provides recommendations using TF-IDF vectorizer and a distance measure as selected by the user. (Check the GitHub to see under the hood)
3. Nearest Neighbors Based - Provides suggestions based on games most closest in the cluster.
"""
)