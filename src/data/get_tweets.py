import os
import pandas as pd
import numpy as np
from api_twitter.api_information import ACCESS_API_INFORMATION
from api_twitter.api_information import auth_api
from api_twitter.get_information_twitter import get_all_tweets_by_user
from api_twitter.get_information_twitter import get_user_information


###Get tweets posted by the user in your profile
def main(screen_name, PATH_DATA):
    ###Authorize twitter, initialize tweepy
    api_twitter = auth_api(ACCESS_API_INFORMATION)

    # Get the User information for twitter
    screen_name = "realDonaldTrump"
    account_information = get_user_information(screen_name, api_twitter)
    account_information = pd.DataFrame.from_dict([account_information])
    account_information.to_csv(os.path.join(PATH_DATA, "account_information.csv"))

    ###Get tweets posted by the user in your profile
    max_tweets = 3200
    tweets_per_query = 200
    all_tweets_user = get_all_tweets_by_user(api_twitter, screen_name, max_tweets, tweets_per_query)

    df_tweets_user = pd.DataFrame()
    for tweet in all_tweets_user:
        aux_df = pd.DataFrame.from_dict(tweet)
        df_tweets_user = pd.concat([df_tweets_user, aux_df])
    df_tweets_user = df_tweets_user.reset_index(drop=True)
    df_tweets_user["created_at_int"] = df_tweets_user["created_at"].astype('int64')

    df = pd.DataFrame({'year': [2015, 2016],
                    'month': [2, 3],
                    'day': [4, 5]})
    df = df_tweets_user.\
        filter(["created_year", "created_month", "created_day"]).\
        rename(columns={"created_year": "year", "created_month": "month", "created_day": "day"})

    df_tweets_user["date"] = pd.to_datetime(df)
    df_tweets_user["date"] = df_tweets_user.date.astype(np.int64)/1000000

    df_tweets_user.to_csv(os.path.join(PATH_DATA, "df_tweets_user.csv"))

if __name__ == "__main__":
    # Get the User information for twitter
    screen_name = "realDonaldTrump"
    ROOT_PATH = os.path.dirname(os.path.dirname(os.getcwd()))
    PATH_DATA = os.path.join(ROOT_PATH, "data")

    main(screen_name, PATH_DATA)
