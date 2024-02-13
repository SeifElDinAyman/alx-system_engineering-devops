#!/usr/bin/python3
'''
A module containing functions for working with the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'
'''
Reddit's base API URL.
'''

def number_of_subscribers(subreddit):
    '''
    Retrieves the number of subscribers in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    '''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': ' '.join([
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'AppleWebKit/537.36 (KHTML, like Gecko)',
            'Chrome/97.0.4692.71',
            'Safari/537.36',
            'Edg/97.0.1072.62'
        ])
    }
    res = requests.get(
        '{}/r/{}/about/.json'.format(BASE_URL, subreddit),
        headers=api_headers,
        allow_redirects=False
    )
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    elif res.status_code == 404:
        # Subreddit not found (invalid subreddit)
        print(f"Subreddit '{subreddit}' not found. Returning 0.")
        return 0
    else:
        # Other error occurred
        print(f"Error: {res.status_code}. Returning 0.")
        return 0
