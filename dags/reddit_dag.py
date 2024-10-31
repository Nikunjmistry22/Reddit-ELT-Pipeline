import os
import praw
import json
import time
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path='reddit.env')

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USER_NAME"),
    password=os.getenv("REDDIT_PASSWORD")

)

def fetch_subreddit_data(subreddit_name="python", delay=3):
    subreddit = reddit.subreddit(subreddit_name)
    data = []

    for submission in subreddit.top(limit=None):
        post_data = {
            "post_id": submission.id,
            "title": submission.title,
            "author": str(submission.author),
            "score": submission.score,
            "num_comments": submission.num_comments,
            "created_utc": datetime.utcfromtimestamp(submission.created_utc).isoformat(),
            "url": submission.url,
            "selftext": submission.selftext
        }
        data.append(post_data)
        print(data)
        

        time.sleep(delay)


fetch_subreddit_data()
