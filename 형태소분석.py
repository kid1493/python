from ntpath import join
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer

dataset = pd.read_csv('C:/Users/Admin/Desktop/2500.csv', error_bad_lines=False)

tagger=Okt()

cv = CountVectorizer()

corpus = []

for doc_num in range(2500):
    noun_list = tagger.nouns([doc_num])
    corpus.append('',join(noun_list))

DTM_Array = cv.fit_transform(corpus).toarray()

feature_names = cv.get_feature_names()

DTM_DataFrame = pd.DataFrame(DTM_Array, columns=feature_names)

DTM_DataFrame.to_csv('C:/Users/Admin/Desktop/dataresult.csv',encoding='utf-8-sig')

print(cv.vocabulary_)
