import praw

reddit = praw.Reddit(
     client_id="VA6WwVKqa5z2Fg",
     client_secret="k94HzNgIGgXPonMMt_qc_bXbCtCqEg",
     user_agent="<console:Happy!>",
     username="RedditBot",
     password="pass1234")

print(reddit.user.me())
 
subreddit = reddit.subreddit("Guitar")

for submission in subreddit.hot(limit=2):
    print('*********')
    print(submission.title)
    submission.upvote()
    
    for comment in submission.comments:
        if hasattr(comment, "body"):
            comment_lower = comment.body.lower()
            if " beautiful " in comment_lower:
                print("-----")
                print(comment.body)