#This script contains the logic for the filter based recommendation system
#Function for fuzzy searching
import pandas as pd
from thefuzz import fuzz, process
import numpy as np

def recommend_game(title, category, genre):
    df = pd.read_csv('Steam_Cleaned.csv')
    df.drop(columns = ['Unnamed: 0'], inplace = True)
    df = df.loc[df['steam_appid'] != 2639280]
    df.drop(columns = ['steam_appid','lang','name_translated', 'dev_translated', 'pub_translated', 'n_achievements','review_score','review_score_desc', 'positive_percentual','metacritic', 'is_free', ], inplace = True)

    #Search with all 3
    if title!='' and category!='None' and genre!='None':
        df['similarity'] = df['name'].apply(lambda x: fuzz.token_sort_ratio(title, x))
        return df.loc[(df['categories'].str.contains(category.lower(), case=False)) & (df['genres'].str.contains(genre.lower(), case=False))].sort_values(by = 'similarity', ascending=False)[:10]
    
    #Search with only 2 parameters
    if title!='' and category!='None' and genre=='None':
        df['similarity'] = df['name'].apply(lambda x: fuzz.token_sort_ratio(title, x))
        return df.loc[df['categories'].str.contains(category.lower(), case=False)].sort_values(by = 'similarity', ascending=False)[:10]
    
    if title!='' and category=='None' and genre!='None':
        df['similarity'] = df['name'].apply(lambda x: fuzz.token_sort_ratio(title, x))
        return df.loc[df['genres'].str.contains(genre.lower(), case=False)].sort_values(by = 'similarity', ascending=False)[:10]

    if title=='' and category!='None' and genre!='None':
        return df.loc[(df['categories'].str.contains(category.lower(), case=False)) & (df['genres'].str.contains(genre.lower(), case=False))]
    
    #Search with only a single parameter
    #Search with only title
    if title !='':
        df['similarity'] = df['name'].apply(lambda x: fuzz.token_sort_ratio(title, x))
        return df.sort_values(by = 'similarity', ascending=False)[:10]

    #If only category is provided
    if category != 'None':
        return df.loc[df['categories'].str.contains(category.lower(), case=False)]

    #If only genre is provided
    if genre != 'None':
        return df.loc[df['genres'].str.contains(genre.lower(), case=False)]

    #Return None if user does not enter anything
    if title == '' and category =='None' and genre == 'None':
        return None