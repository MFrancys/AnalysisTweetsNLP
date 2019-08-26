import nltk
from string import punctuation, digits
from unidecode import unidecode
import spacy

###Import package to NLP
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import GridSearchCV

#from es_lemmatizer import lemmatize
nlp_en = spacy.load("en_core_web_sm")
#nlp_es.add_pipe(lemmatize, after='tagger')

def tokenize(text):
    non_words = digits+"¿¡"
    text_ = "".join([c for c in text if c not in non_words])
    doc = nlp_en(text_)
    tokens = []
    for token in doc:
        if len(token.text) > 1 and not token.is_punct and not token.is_space and not token.is_stop and not '@' in token.text:
            tokens.append(unidecode(token.text.lower()))
    return tokens


def get_best_lda(df_vectorizer_tweets):
    ###Get the main topics in the user's tweets

    #Build LDA Model

    lda_model = LatentDirichletAllocation(n_components=20,               # Number of topics
                                          max_iter=10,               # Max learning iterations
                                          learning_method='online',
                                          random_state=123,          # Random state
                                          batch_size=128,            # n docs in each learning iter
                                          evaluate_every = -1,       # compute perplexity every n iters, default: Don't
                                          n_jobs = -1,               # Use all available CPUs
                                         )

    lda_output = lda_model.fit_transform(df_vectorizer_tweets)

    ###Apply GridSearch to get the best LDA model

    # Define Search Param
    search_params = {'n_components': [10, 15, 20, 25, 30], 'learning_decay': [.5, .7, .9]}

    # Init the Model
    lda = LatentDirichletAllocation()

    # Init Grid Search Class
    model = GridSearchCV(lda, param_grid=search_params, cv=10)

    # Do the Grid Search
    model.fit(df_vectorizer_tweets)

    # Best Model
    best_lda_model = model.best_estimator_

    # Model Parameters
    print("Best Model's Params: ", model.best_params_)

    return best_lda_model
