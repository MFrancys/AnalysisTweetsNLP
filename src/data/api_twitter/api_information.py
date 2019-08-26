import tweepy

###Replace by your credentials tweeter
ACCESS_API_INFORMATION = {
    "CONSUMER_KEY": 'CONSUMER_KEY',
    "CONSUMER_SECRET": 'CONSUMER_SECRET',
    "ACCESS_TOKEN": 'ACCESS_TOKEN',
    "ACCESS_TOKEN_SECRET": 'ACCESS_TOKEN_SECRET',
}


def auth_api(dict_access_api):
    auth = tweepy.OAuthHandler(
        dict_access_api["CONSUMER_KEY"],
        dict_access_api["CONSUMER_SECRET"]
    )
    auth.set_access_token(
        dict_access_api["ACCESS_TOKEN"],
        dict_access_api["ACCESS_TOKEN_SECRET"]
    )
    api = tweepy.API(auth)
    return api
