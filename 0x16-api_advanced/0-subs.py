import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid issues with Reddit API
    headers = {'User-Agent': 'YourAppName/1.0'}

    try:
        # Make the API request
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers from the response
            subscribers = data['data']['subscribers']
            
            return subscribers
        elif response.status_code == 404:
            # If subreddit not found, return 0
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            # Handle other error cases
            print(f"Error {response.status_code}: Unable to retrieve subreddit information.")
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
subreddit_name = "python"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit '{subreddit_name}' has {subscribers_count} subscribers.")

