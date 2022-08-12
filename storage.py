# Importing csv
import csv

# Creating an empty array named all_articles
all_articles = []

# Opening and reading articles.csv
with open('articles.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    all_articles = data[1:]

# Creating other variables
liked_articles = []
disliked_articles = []