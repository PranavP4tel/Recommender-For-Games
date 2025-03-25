#Importing & Preprocessing
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle
from rank_bm25 import BM25Okapi

#----------
#Saving the processed csv file
df = pd.read_csv('Recommender_File.csv')

df_recommender = df[['name_translated', 'categories', 'genres', 'platforms', 'price_initial (USD)']].copy()

df_recommender['tags'] = df['name_translated'] + ' '+df['categories'] + ' ' + df['genres'] + ' ' + df['platforms'] + ' ' +df['price_initial (USD)'].apply(lambda x: str(x))
df_recommender['tags'] = df_recommender['tags'].replace(', ', ' ', regex=True)

# Fill missing values in the 'tags' column with an empty string
df_recommender['tags'] = df_recommender['tags'].fillna('')

df_recommender.to_csv('./exports/recommender_file_main.csv', index = False)


#----------
# Initialize and fit the TF-IDF Vectorizer on the 'tags' column
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df_recommender['tags'])

# Save the vectorizer using pickle
with open('./exports/tfidf_vectorizer.pkl', 'wb') as file:
    pickle.dump(tfidf_matrix, file)

#----------
# Initialize the Nearest Neighbors model
model = NearestNeighbors(metric="cosine", algorithm="brute", n_neighbors=25)
model.fit(tfidf_matrix)

# Freezing the model and exporting it
pickle.dump(model, open('./exports/NN_Model.sav', 'wb'))


#----------
#Saving the tags corpus for the search engine based recommendation system
df_recommender['tags1'] = df['name_translated'] + ' '+df['categories'] + ' ' + df['genres'] + ' ' + df['platforms']
df_recommender['tags1'] = df_recommender['tags1'].replace(', ', ' ', regex=True)

# Fill missing values in the 'tags' column with an empty string
df_recommender['tags1'] = df_recommender['tags1'].fillna('')

corpus = df_recommender['tags1'].str.lower().str.replace("-"," ")
tokenized_corpus = [doc.split(" ") for doc in corpus]
with open('./exports/tokenized_corpus.pkl', 'wb') as file:
    pickle.dump(tokenized_corpus, file)


#----------
#Creating the BM25 model and saving it.
bm25 = BM25Okapi(tokenized_corpus)
with open('./exports/bm25_model.pkl', 'wb') as file:
    pickle.dump(bm25, file)