import pandas as pd

###Package to visualization
import plotly as py
from plotly import graph_objs as go
from plotly.offline import plot, iplot, init_notebook_mode
from plotly.subplots import make_subplots

def graph_analysis_twitter(df_tweets_user, screen_name):
    df_tweets_user_sum = df_tweets_user.\
        filter(["created_month", "id", "retweet_count", "positive_sentiment", "negative_sentiment"]).\
        groupby(["created_month"]).\
        sum().reset_index().\
        sort_values(by='created_month')

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Create and style traces
    time = "created_month"
    fig.add_trace(go.Scatter(x=df_tweets_user_sum[time], y=df_tweets_user_sum["retweet_count"], name="retweet_count", yaxis="y2"))
    fig.add_trace(go.Scatter(x=df_tweets_user_sum[time], y=df_tweets_user_sum["id"], name="number_tweets"))
    fig.add_trace(go.Bar(x=df_tweets_user_sum[time], y=df_tweets_user_sum["negative_sentiment"], name="count_negative_sentiment"))
    fig.add_trace(go.Bar(x=df_tweets_user_sum[time], y=df_tweets_user_sum["positive_sentiment"], name="count_positive_sentiment"))

    # Edit the layout
    fig.update_layout(title=f'ANALYSIS OF PROFILE TWITTER - @{screen_name}',
                       xaxis_title='Month',
                       yaxis_title='Number Tweets',
                       yaxis2_title = "Number of retweets",
                       legend=dict(y=0.5, traceorder='reversed', font_size=16))

    return fig

def graph_count_words(df_vectorizer_tweets):
    count_words = df_vectorizer_tweets.sum().sort_values(ascending=False).iloc[1:50]
    #df_count_words = count_words.to_frame
    df_count_words = pd.DataFrame(
        index=count_words.index,
        data=count_words.values,
        columns=['freq']
    )

    ###Graph of count words
    fig = go.Figure()

    # Create and style traces
    fig.add_trace(go.Bar(x=df_count_words.index, y=df_count_words.freq, name="count_words"))

    # Edit the layout
    fig.update_layout(title='Top of most used words in the twitters',
                       xaxis_title='Month',
                       yaxis_title='Number Tweets',
                       legend=dict(y=0.5, traceorder='reversed', font_size=16))

    return fig
