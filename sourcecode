import nltk
import operator
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
stop_words = set(stopwords.words("english"))

frequency = {} # 여러개의 속성을 같이 묶기위해 dictionary 사용
document_text = open('Consumer_Complaints.txt', 'rt' , encoding = 'UTF8') #  파일 io

text_string = document_text.read().lower()

#words = re.findall(r'\b[a-z]{3,15}\b', text_string)  // 단어 갯수로 분류 하려다가 nltk를 이용 token단위로 나눈후 불용언어를 처리 하였습니다. ex ) 관사 , 조사 등등...

tokens = nltk.word_tokenize(text_string)
clean_tokens=[tok for tok in tokens if len(tok.lower())>1 and (tok.lower() not in stop_words)] #전치사 등 예외 처리

for i in clean_tokens:
        count = frequency.get(i, 0)
        frequency[i] = count + 1


dic = sorted(frequency.items(), key=operator.itemgetter(1) , reverse=True)  #dictionary를 list로 변환 후 사용 빈도수로 정렬

result = [word for word in dic if word not in stop_words]

for i in result[0:20]: # 상위 20개 슬라이싱
   print(i)


# C++ 을 사용하지 않고 python을 사용하면 간결한 코드로 처리할 수 있음. 성능은 
