import requests

def number_of_subscribers(subreddit):
    # Define the URL for the subreddit's about page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define the headers with a custom User-Agent
    headers = {
        "User-Agent": "python:subreddit.subscriber.count:v1.0 (by /u/yourusername)"
    }
    
    try:
        # Make a GET request to the subreddit's about page
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data["data"]["subscribers"]
        else:
            # If the subreddit does not exist, return 0
            return 0
    except requests.RequestException:
        # In case of any network errors, return 0
        return 0

