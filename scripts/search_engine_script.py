from rank_bm25 import BM25Okapi
import pandas as pd
import pickle
from nltk.corpus import stopwords
import nltk
import re
nltk.download('stopwords')

df_recommender = pd.read_csv('./exports/recommender_file_main.csv')

# Load the tokenized corpus from the file
with open('./exports/tokenized_corpus.pkl', 'rb') as file:
    tokenized_corpus = pickle.load(file)

#Setting stopwords to remove from the user input
stopwords = set(stopwords.words('english'))

#Loading the BM25 object from the file
with open('./exports/bm25_model.pkl', 'rb') as file:
    bm25 = pickle.load(file)

def search_games(desc, values, n_recommends, df_recommender = df_recommender):
    min, max = values[0], values[1]
    
    #Initializing the engine
    #bm25 = BM25Okapi(tokenized_corpus)

    desc = desc.lower()
    desc = re.sub(r'http\S+', '', desc)  # Remove URLs
    desc = re.sub(r'[^A-Za-z\s]', '', desc)  # Remove special characters and numbers
    desc = re.sub(r'\\',' ', desc) #Remove backslash characters
    tokens = desc.split(" ")

    #Removing stop words as well as applying lemmatization
    tokens = [word for word in tokens if word not in stopwords]

    #Obtaining similarity scores for the user input
    doc_scores = bm25.get_scores(tokens)
    df_recommender['scores'] = doc_scores

    df_recommender = df_recommender.loc[df_recommender['price_initial (USD)'].between(min, max)]
    return df_recommender[['name_translated','categories','genres','platforms','price_initial (USD)','scores']].sort_values(by = 'scores', ascending = False)[:n_recommends]
