# Importing csv and pandas
import pandas as pd, csv

# Creating an empty array named all_articles
all_articles = []

# Reading articles.csv using pandas
df = pd.read_csv('articles.csv', encoding='UTF-8')

# Filtering the lang column to only include English articles
df = df[df['lang'] == 'en']

# Exporting the csv to a new file
df.to_csv('articles_en.csv', index=False)

# Opening and reading articles_en.csv
with open('articles_en.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    all_articles = data[1:]

# Creating other variables
liked_articles = []
disliked_articles = []