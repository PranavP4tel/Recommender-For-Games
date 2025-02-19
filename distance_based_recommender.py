#This is the script to recommend games to users based on content based filtering (Using distance measures)

#Importing necessary libraries
import pandas as pd
from math import sqrt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity, euclidean_distances, manhattan_distances
