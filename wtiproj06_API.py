from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/ratings', methods=['GET'])
def get_ratings():
    return 'ratings'


@app.route('/avg-genre-ratings/<id>', methods=['GET'])
def get_avg_genre_ratings(id):
    return id


@app.route('/avg-genre-ratings/all-users', methods=['GET'])
def get_all_users():
    return 'ratings'


@app.route('/')
def index():
    return "TEST!"

if __name__ == '__main__':
    app.run(debug=True)