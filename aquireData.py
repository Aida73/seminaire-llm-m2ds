import os
from dotenv import load_dotenv
import praw
import datetime
import pandas as pd
# import Pyarrow
# Load environment variables from the .env file
load_dotenv()
# Set up your Reddit API credentials
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDDIT_USERNAME = os.environ['REDDIT_USERNAME']
REDDIT_SECRET = os.environ['REDDIT_SECRET']
USER_AGENT = "MyApi/1.0.0"

# Authenticate using OAuth2
reddit = praw.Reddit(
 client_id=CLIENT_ID,
 client_secret=CLIENT_SECRET,
 password=REDDIT_SECRET,
 user_agent=USER_AGENT,
 username=REDDIT_USERNAME,
)


# Search for posts related to RATP in a specific subreddit
subreddit_name = 'france' # specific groupe
scope_query = 'agriculteurs' # You can adjust this query based on your needs use OR to seperate words.
# Get the subreddit instance
subreddit = reddit.subreddit(subreddit_name)
# Retrieve top 10 hot posts containing the scope_query
agro_submissions = subreddit.search(scope_query, sort='hot', limit=20)


# for submission in ratp_submissions:
#  submission = {
#  "submission_id": submission.id,
#  "title": submission.title,
#  "text": submission.selftext,
#  "num_votes": submission.score,
#  "num_comments": submission.num_comments,
#  "date": datetime.datetime.utcfromtimestamp(submission.created).strftime("%d/%m/%Y, %H:%M:%S"),
#  "author":  submission.author_fullname,
#  "author_id":submission.author.id if hasattr(submission.author, 'id') else None,
#  "author_name":  submission.author.name
#  }
#  print(submission)



submissions = []
for submission in agro_submissions:
  submission = {
  "submission_id": submission.id,
  "title": submission.title,
  "text": submission.selftext,
  "num_votes": submission.score,
  "num_comments": submission.num_comments,
  "date": datetime.datetime.utcfromtimestamp(submission.created).strftime("%d/%m/%Y, %H:%M:%S"),
  "author":  submission.author_fullname,
  "author_id":submission.author.id if hasattr(submission.author, 'id') else None,
  "author_name":  submission.author.name
  }
  submissions.append(submission)

submissions_df = pd.DataFrame(submissions)

#submissions_df.to_csv("data.csv")