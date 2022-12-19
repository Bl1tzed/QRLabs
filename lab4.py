import pymorphy2
from matplotlib import pyplot
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
punc_str = "!()-[]{};:@#$%^',.\|/*-<>_~'"
morph = pymorphy2.MorphAnalyzer()
raw_text = open(r'text.txt', encoding='utf-8-sig').read()
sentences = sent_tokenize(raw_text, language='russian')
stop_words = set(stopwords.words('russian'))

def lemmatize(text):
    words = word_tokenize(text, language='russian')
    filtered_words = list()
    for word in words:
        if (word not in stop_words) and (word not in punc_str):
            filtered_words.append(word)
    unique_lemms = list()
    for filt_word in filtered_words:
        p = morph.parse(filt_word)[0].normal_form
        if p not in unique_lemms:
            unique_lemms.append(p)
    return unique_lemms


count_vectorizer = CountVectorizer()
string = [''.join(line) for line in sentences]
bag_of_words = count_vectorizer.fit_transform(string)
feature_names = count_vectorizer.get_feature_names_out()
print('Токен Векторизация')
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names[:113]))

count_vectorizer_lemms = CountVectorizer(tokenizer=lemmatize)
bag_of_words = count_vectorizer_lemms.fit_transform(string)
feature_names = count_vectorizer_lemms.get_feature_names_out()
print('Лемма Векторизация')
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names[:113]))

tfidf_vectorizer = TfidfVectorizer()
bag_of_words = tfidf_vectorizer.fit_transform(string)
feature_names = tfidf_vectorizer.get_feature_names_out()
print('TF-IDF Векторизация')
print(pd.DataFrame(bag_of_words.toarray(), columns=feature_names[:113]))

lemmed = lemmatize(raw_text)
text = ''
for word in lemmed:
    text += ' ' + word

cloud = WordCloud(collocations=False).generate(text)
pyplot.imshow(cloud)
pyplot.axis('off')
cloud.to_file('cloud.png')
