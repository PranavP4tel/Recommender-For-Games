import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances

#Importing & Preprocessing
df = pd.read_csv('Recommender_File.csv')

df_recommender = df[['name_translated', 'categories', 'genres', 'platforms', 'price_initial (USD)']].copy()

df_recommender['tags'] = df['name_translated'] + ' '+df['categories'] + ' ' + df['genres'] + ' ' + df['platforms'] + ' ' + df['is_free'].apply(lambda x: str(x)) + ' '+df['price_initial (USD)'].apply(lambda x: str(x))
df_recommender['tags'].replace(', ', ' ', regex=True, inplace=True)

#print(df_recommender['tags'].head())
#print(df_recommender['tags'].isna().sum())  # Check for missing values

# Fill missing values in the 'tags' column with an empty string
df_recommender['tags'] = df_recommender['tags'].fillna('')

#----------
# Initialize and fit the TF-IDF Vectorizer on the 'tags' column
tfidf = TfidfVectorizer()
tfidf_gameid = tfidf.fit_transform(df_recommender['tags'])

# Check the shape of the resulting matrix
#print("Shape of TF-IDF matrix:", tfidf_gameid.shape)

from sklearn.metrics.pairwise import cosine_similarity

#----------
#Creating the function
def recommender_distance(title, tfidf_gameid = tfidf_gameid, similarity='Cosine'):
    # Find the index of the game based on the title
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

#Testing
print(recommender_distance('the legendary hero of the hero', similarity='Cosine'))

    