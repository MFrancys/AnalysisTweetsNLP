from textblob import TextBlob
from api_twitter.preprocessing_text import cleaned_text

def get_user_information(screen_name, api_twitter):
    # Get the User information for twitter
    user = api_twitter.get_user(screen_name)
    account_information = {
        "user_name": user.name,
        "screen_name": user.screen_name,
        "location": user.location,
        "description": user.description,
        "others_nets": user.entities["url"]["urls"][0]["expanded_url"],
        "followers_count": user.followers_count,
        "friends_count": user.friends_count,
        "created_count": str(user.created_at.date()),
        "profile_image_url": user.profile_image_url
    }
    return account_information

def get_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity.round(2)
    except:
        try:
            return TextBlob(text).sentiment.polarity
        except:
            return 0

def get_positive_sentiment(x):
    if x > 0.2:
        return 1
    else:
        return 0

def get_negative_sentiment(x):
    if x < -0.2:
        return 1
    else:
        return 0

def get_information_user_tweets(status):
    if "RT @" not in status.text:
        text_cleaned = cleaned_text(status.text)
        sentiment = get_sentiment(text_cleaned)
        user_tweet = {
            "id_str": [status.id_str],
            "id": [1],
            "created_at": [status.created_at],
            "text": [status.text],
            "text_cleaned": [text_cleaned],
            "hashtags": [[h["text"] for h in status.entities["hashtags"]]], ###Check
            "retweet_count": [status.retweet_count],
            "sentiment": [sentiment],
            'positive_sentiment': [get_positive_sentiment(sentiment)],
            'negative_sentiment': [get_negative_sentiment(sentiment)],
            "created_year": [status.created_at.year],
            "created_month": [status.created_at.month],
#            "created_week": [status.created_at.week],
            "created_day": [status.created_at.day],
        }
        return user_tweet

def get_all_tweets_by_user(api_twitter, screen_name, max_tweets, tweets_per_query ):
    ###Twitter only allows access to users most recent 3240 tweets with this method
    all_tweets = [] #Initialize a list to hold all the tweets
    tweets_count = 0

    #Make initial request for most recent tweets (200 miximum allowed count)
    new_tweets = api_twitter.user_timeline(screen_name=screen_name, count=tweets_per_query)
    max_id = new_tweets[-1].id - 1 #Save the id of the oldest tweet less one

    for status in new_tweets:
        user_tweet_information = get_information_user_tweets(status)
        all_tweets.append(user_tweet_information) #save most recent tweets

    tweets_count += len(new_tweets)

    print("Dowloaded {} tweets of {}".format(len(all_tweets), max_tweets))

    #Keep grabbing tweets until there are no tweets left to grab
    while tweets_count<max_tweets:
        #all subsquent request use ,ax_id param to prevent duplicates
        new_tweets = api_twitter.user_timeline(screen_name=screen_name, count=tweets_per_query, max_id=max_id)
        if len(new_tweets)>0:
            print(new_tweets)
            max_id = new_tweets[-1].id - 1 #Save the id of the oldest tweet less one
            tweets_count += len(new_tweets)

            for status in new_tweets:
                user_tweet_information = get_information_user_tweets(status)
                all_tweets.append(user_tweet_information) #save most recent tweets
            print("Dowloaded {} tweets of {}".format(len(all_tweets), max_tweets ))

    return all_tweets

def get_tweets_search_information(status):
    ###Get information relevant of each twitter
    if "RT @" not in status.full_text:
        tweet_item = {
            "id_str": [status.id_str],
            "username": [status.user.screen_name],
            "text": [status.full_text],
            "cleaned_text": [cleaned_text(status.full_text)],
            "created_at": [status.created_at],
            "polatity": [""],
            "subjetivity": [""],
            "created_month": [status.created_at.month]
        }
        return tweet_item
