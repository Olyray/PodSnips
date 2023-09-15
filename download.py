#!/usr/bin/env python3
"""Contains functions relating to downloading and clipping the podcast episode."""


import os
from uuid import uuid4
from pydub import AudioSegment
from clint.textui import progress
import requests

def sanitize_filename(filename):
    return "".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip()

def download_podcast_episode(episode_url, episode_name):
    episode_name = sanitize_filename(episode_name)
    
    if not os.path.exists('downloaded_episodes'):
        os.makedirs('downloaded_episodes')
    
    response = requests.get(episode_url, stream=True)
    file_path = os.path.join('downloaded_episodes', f"{episode_name}.mp3")
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            total_length = int(response.headers.get('content-length'))
            for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
                if chunk:
                    file.write(chunk)
                    file.flush()
        return file_path
    return file_path

def clip_podcast_episode(file_path):
    """Clips the podcast episode"""
    if not os.path.exists('clips'):
        os.makedirs('clips')
    start_time = input("Enter the start time for the clip (in format HH:MM:SS): ")
    end_time = input("Enter the end time for the clip (in format HH:MM:SS): ")

    start_time_in_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], start_time.split(':')))
    end_time_in_ms = sum(x * int(t) for x, t in zip([3600000, 60000, 1000], end_time.split(':')))

    audio = AudioSegment.from_mp3(file_path)
    clip = audio[start_time_in_ms:end_time_in_ms]
    clip_name = str(uuid4())
    clip.export(os.path.join('clips', f"{clip_name}.mp3"), format='mp3')
    print(f"The clip has been saved as 'clips/{clip_name}.mp3'.")
