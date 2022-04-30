# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pandas as pd
import json
import re
client_id = "U1P_lUkQic8KDK9norx6"
client_secret = "yQwkhVI8IK"

query = urllib.parse.quote(input("검색 질의 : "))
idx = 0 
display = 100
start = 1
end = 1000

df = pd.DataFrame(columns = ( "Title" , "Link" , "Description"))

for start_index in range (start, end , display):

    url = "https://openapi.naver.com/v1/search/cafearticle?query=" + query \
    + "&display=" + str(display) \
    + "&start=" + str(start_index)

    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items =response_dict['items']
        for item_index in range(0,len(items)):
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, '', items[item_index]['title'])
            link = items[item_index]['link']
            description =  re.sub(remove_tag, '', items[item_index]['description'])
            df.loc[idx] = [title, link, description]
            idx += 1
            df.to_csv('df.csv')
    else:
        print("Error Code:" + rescode)

df
