#!/usr/bin/env python3
"""Contains all functions relating to the api"""
import requests
from dotenv import load_dotenv
import os

def get_listen_notes_api_key():
    """Gets the listen notes API"""
    load_dotenv()
    return os.getenv("LISTEN_NOTES_API_KEY")

def get_podcast_info(api_key, podcast_name, episode_number):
    """Gets the podcast episode name and episode url"""
    headers = {
        'X-ListenAPI-Key': api_key
    }

    response = requests.get('https://listen-api.listennotes.com/api/v2/search', headers=headers, params={
        'q': podcast_name,
        'type': 'podcast',
        'only_in': 'title'
    })

    data = response.json()
    podcast_id = data['results'][0]['id']

    response = requests.get(f'https://listen-api.listennotes.com/api/v2/podcasts/{podcast_id}', headers=headers)
    data = response.json()
    episode_url = data['episodes'][episode_number - 1]['audio']
    episode_name = data['episodes'][episode_number - 1]['title']

    return episode_url, episode_name
