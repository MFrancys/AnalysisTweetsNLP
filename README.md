AnalysisTweets
==============================

Version: 1.0a0

Platform: Windows

Summary: AnalysisTweets get the tweets posted by a user and apply NLP of them

Keywords: tweets nlp tokens topics wordclouds clusters reducition_dimentions

Installation:
```bash
pip install -r requirements.txt
```

Usage:
To download the user's tweets in a csv file you must change the directory to src\data
and run the script get_tweets.py. Also, you must place yout twitter credentials in the
script api_information.py, which is the following location src\data\api_information.

```bash
python get_tweets.py
```

To view the tweets and analyze them through NLP, you must run the notebok called analysis_twitter.ipynb

```bash
1) ipython kernel install --user --name=myvenv
2) jupyter notebook
```

Project Organization
------------
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── df_tweets_user.csv       <- Data with all user tweets  
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── api_twitter <- Scripts to access the twitter api and download a user's tweets
    │   │   │   └── api_information.py
    │   │   │   └── get_information_twitter.py
    │   │   │   └── preprocessing_text.py
    │   │   │   ├── __init__.py    <- Makes api_twitter a Python module
    │   │   └── preprocessing_text <- Apply NLP on tweets    
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── processing_text.py
    │   │    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── make_graph.py
    │
    └── analysis_twitter.ipynb   <- Notebook to visualize the results of the tweet analysis

Author:
Maria Francys Lanza Garcia

Author-email:
mariafrancysucv@gmail.com
