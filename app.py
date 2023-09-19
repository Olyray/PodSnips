#!/usr/bin/env python3
"""The main flask app"""

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)
load_dotenv()

LISTEN_NOTES_API_KEY = os.getenv("LISTEN_NOTES_API_KEY")

@app.route('/')
def home():
    """Returns the home page"""
    return render_template('index.html')

@app.route('/api/search_podcast', methods=['GET'])
def search_podcast():
    """Called with the search button and used to search for podcasts"""
    query = request.args.get('query')
    headers = {
        'X-ListenAPI-Key': LISTEN_NOTES_API_KEY
    }
    response = requests.get('https://listen-api.listennotes.com/api/v2/typeahead', headers=headers, params={
        'q': query,
        'show_podcasts': 1,
        'show_episodes': 0
    })
    data = response.json()
    return jsonify(results=data['podcasts'])


@app.route('/api/podcast_details/<podcast_id>', methods=['GET'])
def podcast_details(podcast_id):
    headers = {
        'X-ListenAPI-Key': LISTEN_NOTES_API_KEY
    }
    response = requests.get(f'https://listen-api.listennotes.com/api/v2/podcasts/{podcast_id}', headers=headers)
    data = response.json()
    return jsonify(details=data)


@app.route('/podcast_details')
def podcast_details_page():
    return render_template('podcast_details.html')


if __name__ == '__main__':
    app.run(debug=True)
