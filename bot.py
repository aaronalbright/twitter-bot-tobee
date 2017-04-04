#!/usr/bin/env python

import twitter
import time
import random
from keys import *
api = twitter.Api(C_key, C_secret, A_token, A_secret)

#Possibel tweets
tweet_replies = [".@%s Don't sweat it, %s. Everything is going tobee alright.",
".@%s You got this, %s!",
".@%s I believe in you %s. Everything will be OK.",
".@%s %s, everything is going to be OK!",
".@%s Believe in yourself, %s!",
".@%s Don't give up. Great things are in store for you, %s.",
".@%s Evertyhing is going to be OK, %s.",
".@%s Evertyhing is going to be alirght, %s.",
".@%s When the going gets tough, the tough get going, %s!"]

# Last mention responded to (very rudimentary)
lastMention = 849089983633915904

while True:

    global lastMention

    # Get most recent mention
    mentions = api.GetMentions(count=1)

    # Get Handle, ID and Name of a user who tweets at Toby
    for i in mentions:
        global userName, userID, userNick
        userName = i.user.screen_name
        userID = i.id
        userNick = i.user.name
        mostRecentMention = i.id
        print userName, userID, userNick

    #Compose and send tweet if new mentioned is detected
    tweet = random.choice(tweet_replies) % (userName, userNick)
    if mostRecentMention != lastMention:
        api.PostUpdate(status=tweet,in_reply_to_status_id=userID)
        print("I tweeted")

    #Sets most recent mentioned as the last mentioned tweeted
    lastMention = mostRecentMention

    time.sleep(30)
