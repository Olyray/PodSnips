#!/usr/bin/env python3
"""The main module"""

from api import get_listen_notes_api_key, get_podcast_info
from download import download_podcast_episode, clip_podcast_episode

def main():
    """Starts by downloading the episode, then calls other functions to clip it"""
    api_key = get_listen_notes_api_key()
    podcast_name = input("Enter the name of the podcast: ")
    episode_number = int(input("Enter the podcast episode number: "))
    episode_url, episode_name = get_podcast_info(api_key, podcast_name, episode_number)
    file_path = download_podcast_episode(episode_url, episode_name)
    clip_podcast_episode(file_path)

if __name__ == "__main__":
    main()
