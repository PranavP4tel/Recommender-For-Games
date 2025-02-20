import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances

df_recommender = pd.read_csv('recommender_file_main.csv')

# Load the vectorizer using pickle
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_gameid = pickle.load(file)


#----------
#Creating the function
def recommender_distance(title, tfidf_gameid = tfidf_gameid, similarity='Cosine'):
    # Find the index of the game based on the title
    if title =='':
        return None
    
    game_index = df_recommender.loc[df_recommender['name_translated'] == title].index
    
    if len(game_index) == 0:
        return "Game not found in the dataset."
    
    game_index = game_index[0]  # Get the index of the game

    if similarity =='Cosine':
        similarity_scores = cosine_similarity(tfidf_gameid[game_index], tfidf_gameid)
    
    elif similarity == 'Manhattan Distance':
        similarity_scores = manhattan_distances(tfidf_gameid[game_index], tfidf_gameid)
    
    else:
        similarity_scores = euclidean_distances(tfidf_gameid[game_index], tfidf_gameid)
    
        # Get the indices of the top 10 most similar games (highest cosine similarity)
    similar_game_indices = similarity_scores[0].argsort()[::-1][1:11]  # Exclude the input game
    return df_recommender.iloc[similar_game_indices][['name_translated', 'categories', 'genres', 'platforms', 'price_initial (USD)']]
    