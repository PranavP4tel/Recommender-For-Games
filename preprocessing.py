#Importing & Preprocessing
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

#----------
#Saving the processed csv file
df = pd.read_csv('Recommender_File.csv')

df_recommender = df[['name_translated', 'categories', 'genres', 'platforms', 'price_initial (USD)']].copy()

df_recommender['tags'] = df['name_translated'] + ' '+df['categories'] + ' ' + df['genres'] + ' ' + df['platforms'] + ' ' + df['is_free'].apply(lambda x: str(x)) + ' '+df['price_initial (USD)'].apply(lambda x: str(x))
df_recommender['tags'] = df_recommender['tags'].replace(', ', ' ', regex=True)

# Fill missing values in the 'tags' column with an empty string
df_recommender['tags'] = df_recommender['tags'].fillna('')
df_recommender.to_csv('recommender_file_main.csv', index = False)

#----------
# Initialize and fit the TF-IDF Vectorizer on the 'tags' column
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df_recommender['tags'])

# Save the vectorizer using pickle
with open('tfidf_vectorizer.pkl', 'wb') as file:
    pickle.dump(tfidf_matrix, file)

#----------
# Initialize the Nearest Neighbors model
model = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=25)
model.fit(tfidf_matrix)

# Freezing the model and exporting it
pickle.dump(model, open('NN_Model.sav', 'wb'))