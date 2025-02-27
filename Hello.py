import streamlit as st

st.set_page_config(
    page_title="Game Recommender",
    page_icon="https://img.icons8.com/?size=48&id=zNqjI8XKkCv0&format=png",
)

st.write("# Welcome to our game recommender!")
st.write("### Ready To Play?")

st.sidebar.success("Select a page from above.")

st.markdown(
    """
This project allows one to get recommendations for the game title entered by the user.
Different approaches for the recommenders are:
1. Filter Based - A simple solution that provides games that have similar titles as entered by the user, by fuzzy searching.
2. Distance Based - Provides recommendations using the TF-IDF vectorizer and a distance measure as selected by the user.
3. Nearest Neighbors Based - Provides suggestions as the closest neighbors of the user input in the dataset.

To have a peek under the hood, check out the GitHub Repository!
"""
)