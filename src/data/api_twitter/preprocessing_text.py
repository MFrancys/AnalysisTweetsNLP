#import es_core_news_sm
#from es_lemmatizer import lemmatize
import nltk

from string import punctuation, digits
from unidecode import unidecode
from nltk.corpus import stopwords
from spacy.lemmatizer import Lemmatizer

import spacy
#from es_lemmatizer import lemmatize
nlp_es = spacy.load("en_core_web_sm")
#nlp_es.add_pipe(lemmatize, after='tagger')

NON_WORDS = punctuation + digits + "¿¡"
LIST_STOPWORDS = stopwords.words("spanish") + stopwords.words("english")
lemmatizer = Lemmatizer()

"""Prepocessing the raw texts

    This involves the following steps:
    1) Removing punctuation marks and digits from of the text.
    2) Tokenization - Split the sentences of text into words.
    3) Removing spanish and english stopwords.
    4) Check the spelling of the tokens.
    5) Lemmatization.
    6) Removing words with less two characters.
    7)Removing the accents.
    8) Removing internal stopwords.
    9) Join the tokens into a string.
"""

def cleaned_text(text):
    text = ("").join([c for c in text if c not in NON_WORDS])
#    text_tokens = nltk.word_tokenize(text, language="spanish")
    text_tokens = nltk.word_tokenize(text)
    tokens_no_stopwords = list(filter(lambda word: word not in LIST_STOPWORDS, text_tokens))
#    tokens_check_spelling = list(map(lambda word: spell_es.correction(word), tokens_no_stopwords))
    tokens_lemma = list(map(lambda word: spacy_lemma(word), tokens_no_stopwords))
    tokens_cleans = list(filter(lambda word: len(word)>1, tokens_lemma))
    tokens_no_stopwords_internal = list(filter(lambda word: word not in LIST_STOPWORDS, tokens_cleans))
    tokens_cleans = list(map(lambda word: unidecode(word), tokens_cleans))
    tokens = " ".join(tokens_no_stopwords_internal)
    return tokens

def spacy_lemma(word):
    """ Returns the word to its root with lemmatize

    Parameters
    ----------
    word : str
        Word to lemmatize

    Returns
    -------
    word
        A string with the root of a word
    """

    doc = nlp_es(word)
    for token in doc:
        return token.lemma_
