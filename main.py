from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, disliked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    print(all_articles[0][13])
    article_data = {
        "title": all_articles[0][13],
        "url": all_articles[0][12]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/post-liked-articles", methods=["POST"])
def liked_article():
    article = all_articles[1]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/post-unliked-articles", methods=["POST"])
def unliked_article():
    article = all_articles[1]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[0],
            "poster_link": article[1],
            "release_date": article[2] or "N/A",
            "duration": article[3],
            "rating": article[4],
            "overview": article[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[0],
            "poster_link": recommended[1],
            "release_date": recommended[2] or "N/A",
            "duration": recommended[3],
            "rating": recommended[4],
            "overview": recommended[5]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()