import twitter,json,csv

CONSUMER_KEY = "nxwgrAxA28vXNY4bAhuUStvQe"
CONSUMER_SECRET = "26DWQPiS4gkRl8iVjJLpWLpfwempNQOUXLGiW0stAa6iCUfz5E"

OAUTH_TOKEN = "881541088867106817-MqAPoFz4BsVCNEvzsTDwABJBGpmJquz" 
OAUTH_TOKEN_SECRET = "SV9r3Qg1SdDbwmsS1cKa4K2KYyHKR2F50fDMYNmKKI1pi"


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth, retry=True)

# setup a file named elon_musk.csv to contain the data I get
csvfile = open('elon_musk_3.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter='|')

#  heres a function that takes out characters that can break
#  our import into Excel and replaces them with spaces
#  it also does the unicode bit
def getVal(val):
    clean = ""
    if val:
        val = val.replace('|', ' ')
        val = val.replace('\n', ' ')
        val = val.replace('\r', ' ')
        clean = val
    return clean

#  these two are for elonMusk and boredElonMusk
# u = "44196397, 1666038950"
u = "44196397,  1666038950"

print ('Filtering the public timeline for track="%s"' % (u,))

twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)

stream = twitter_stream.statuses.filter(follow=u)

for tweet in stream:

    if tweet['truncated']:
        tweet_text = tweet['extended_tweet']['full_text']
    else:
        tweet_text = tweet['text']
    # write the values to file
    csvwriter.writerow([
        tweet['id_str'],
        tweet['created_at'],
        getVal(tweet['user']['screen_name']),
        getVal(tweet_text),
        getVal(tweet['user']['location']),
        tweet['user']['statuses_count'],
        tweet['user']['followers_count'],
        tweet['user']['friends_count'],
        tweet['user']['created_at']
        ])
    # print something to the screen, mostly so we can see what is going on...
    print (tweet['user']['screen_name'], tweet['text'])
