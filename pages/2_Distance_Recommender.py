import streamlit as st
import sys

# Setting path to parent Folder
sys.path.append('../ETDS Project')
#from distance_recommender_script import recommend_game

#Page config
st.set_page_config(
        page_title="Game Recommender",
        layout="wide",
    )

#Page data
st.markdown("""# Distance Based Recommender""")

st.markdown("""This app allows you to get recommendations to the Steam titles that you provide or the filter selected. However, the articles may take some time to load, and the data is not up to date.""")

#Taking keyword to search news by
st.text_input("Enter a title",key = "title")

#Button Click Definition
if st.button("Search!"):
    #df = recommend_game(title = st.session_state.title, genre = st.session_state.genre, category = st.session_state.category)
    #if df is None:
    #    st.write('Please provide some input!')
    #else:
    #    st.dataframe(df)

    st.write('Reached!')