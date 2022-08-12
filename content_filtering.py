# Importing required libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

# Reading articles.csv using pandas
df = pd.read_csv('articles.csv')

# Removing NaN values from title column
df = df[df['title'].notna()]

# Using the CountVectorizer to remove stopwords and create a matrix of the words in the title column
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['title'])

# Using the cosine_similarity function to find the similarity between the words in the title column
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

# Resetting the index of the dataframe
#df = df.reset_index() << This is not needed because the index is already 0-based (THIS IS THE ERROR WHICH IS COMING!!!)

# Creating indices for the dataframe
indices = pd.Series(df.index, index=df['contentId'])

# Creating a function to get recommendations
def get_recommendations(contentId, cosine_sim=cosine_sim2):
    # Getting the index of the movie that matches the contentId
    idx = indices[contentId]
    # Getting the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sorting the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Getting the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # Get the article indices
    article_indices = [i[0] for i in sim_scores]
    # Return the top 10 most similar movies and converting to a list
    return df[['title', 'url', 'text', 'lang']].iloc[article_indices].values.tolist()