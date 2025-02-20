import pandas as pd
import numpy as np
import pickle

df_recommender = pd.read_csv('recommender_file_main.csv')

# Load the vectorizer using pickle
with open('tfidf_vectorizer.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

#Loading the model using pickle
model = pickle.load(open('NN_Model.sav', 'rb'))

# Function to get recommendations
def recommend_game(game_title, n_recommendations):
    if game_title =='':
        return None

    game_id = df_recommender.loc[df_recommender['name_translated'] == game_title].index[0]
    
    # Ensure the input matrix slice is 2D (one game, all features)
    game_vector = tfidf_matrix[game_id].reshape(1, -1)
    distances, indices = model.kneighbors(game_vector, n_neighbors=n_recommendations)
    df_return = df_recommender.loc[df_recommender.index.isin(indices.flatten()[1:]), df_recommender.columns != 'tags']
    df_return['distances'] = distances.flatten()[1:]
    
    return df_return
