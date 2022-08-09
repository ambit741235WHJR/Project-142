# Importing Flask, request, jsonify and csv
import json
from flask import Flask, request, jsonify
import csv

# Creating an empty array named all_articles
all_articles = []

# Opening and reading articles.csv
with open('articles.csv', encoding='UTF-8') as csvfile:
    data = list(csv.reader(csvfile))
    all_articles = data[1:]

# Creating other variables
liked_articles = []
disliked_articles = []

# Creating a Flask App
app = Flask(__name__)

# Creating Flask API
@app.route('/get-article', methods=['GET'])
def get_article():
    return jsonify({'Data': all_articles[0], 'Status': 'OK'})

# Creating Flask API for Liked Articles
@app.route('/post-liked-articles', methods=['POST'])
def post_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({'Status': 'OK'}), 201

# Creating Flask API for Disliked Articles
@app.route('/post-disliked-articles', methods=['POST'])
def post_disliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({'Status': 'OK'}), 201

# Code for running the Flask App
if __name__ == '__main__':
    app.run()