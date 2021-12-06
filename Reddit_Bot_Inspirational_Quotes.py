"""
Reddit Bot by Wyatt B

We had to sign up a NEW account on Reddit.com and we named this Bot: Jim-Bot

Reddit/prefs/app make sure to make it a script not a web app!

Goal of application: 
    * To look at top level 'hot' comments of a specific r/subreddit
    * Look for a specific word: ' sad '
    * Reply with an inspirational quote
    
Application(s) for the future:
    * Promote and Advertise a business or brand to a specific reddit (if they allow it)
    
Note before running:
'pip install praw' in the console:
"""
import praw
import random
import time

reddit = praw.Reddit(
    client_id="PERSONAL USE SCRIPT",
    client_secret="SECRET",
    user_agent="<console:XXX:1.0>",
    username= "",
    password = "",
)

# reddit.subreddit is how to grab a specific subreddit we chose r/television
subreddit = reddit.subreddit('television')

#We are making a list of quotes for our bot to respond to people with, stored in a list
sad_quotes = [ 'One must not let oneself be overwhelmed by sadness. -Jacqueline Kennedy Onassis ',
              'The word ‘happy’ would lose its meaning if it were not balanced by sadness. - Carl Jung',
              'It doesn’t hurt to feel sad from time to time. - Willie Nelson',
              'I (You )have the choice of being constantly active and happy or introspectively passive and sad. - Sylvia Plath',
              'Tears come from the heart and not from the brain. - Leonardo Da Vinci'    
    ]

# For loop to loop through the sub reddit:
# .hot is going to filter by hot posts, there's .hot, .new, and .top like you normally see on reddit
# Limit to the first 10 results
for submission in subreddit.hot(limit = 10):
    #Added to see the submission more clearly in the console
    print('\n*******************\n')
    #We are grabbing the title of each submission
    print(submission.title)
    
    #Another for loop to go over every comment in each those 10 submissions
    for comment in submission.comments:
        #If statement to print if the comment HAS a body, hassattr will check (comment, body)
        if hasattr(comment, 'body'):
            #We are treating our 'key word' the same whether it's upper or lowercase by turning them all lowercase in a new var            
            comment_lower = comment.body.lower()
            if ' sad ' in comment_lower:
                print('\n*******************\n')
                #Comment alone will give us comment object data 'hash', we need the '.body' attribute
                print(comment.body)
                # New var = picking a random number from index 0 to the length of list - 1 to properly index.
                random_index = random.randint(0, len(sad_quotes) -1)
                # Our reply
                comment.reply(sad_quotes[random_index])
                # Sleep program after 11 minutes
                time.sleep(660)

