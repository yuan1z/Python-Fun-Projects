import tweepy
import time
auth = tweepy.OAuthHandler('osAENGcEgqxT1nk8KinxNTsI5', 'bLrA5EfMZD62L6U89Gt9RqecKRT0h4HKvPpblwOrV0vphJEBL6')
auth.set_access_token('1479840782-2fFdlQpPtGWB5epUYVXBI1jbNYe3xpnyiEn9gIo', 'yyAKvdIhdaDvf2EERFAEvIbetk4m2gyXRLzY0xHdbuKNI')

api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
user = api.me()
print(user.followers_count)

def limit_handler(cursor): # twitter has sever limit
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
#Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name == 'DennisGao':
        follower.follow()
        print('Follow back')

search_string = 'Boston University'
numberofTweets = 10
for tweet in tweepy.Cursor(api.search,search_string).items(numberofTweets):
    try:
        tweet.retweet()
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break