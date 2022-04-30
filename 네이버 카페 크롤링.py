from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import re
from selenium.webdriver.common.keys import Keys # 키보드 키를 제어



keys = Keys()


driver = webdriver.Chrome("C:/Users/multicampus/Desktop/python/chromedriver/chromedriver.exe") #주소 
driver.get("https://section.cafe.naver.com/")

time.sleep(1)
Q = driver.find_element_by_css_selector('#header > div.snb_area > div > div.SearchArea > form > fieldset > div > div > div.FormInputText > input')
Q.click()

#query = urllib.parse.quote(input("검색 질의 : "))
keyword = "스티치"
Q.send_keys(keyword)
Q.send_keys(keys.ENTER)

time.sleep(1)
driver.find_element_by_css_selector('#mainContainer > div > div.SectionSearchContent > div.section_search_content > div > div.list_area.article_list_area > div > a > span').click()
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

len(soup.find_all('div', class_ = 'detail_area'))

link_len = len(soup.find_all('div', class_ = 'detail_area'))+1

df = pd.DataFrame(columns = ( "Title" , "Content" ,"Time"))

#title_list = []
#con_list = []
search = []
count = 1
idx = 1

while(count < 100):
    
    

    for i in range(1,link_len): # link_len
        driver.find_element_by_css_selector('#mainContainer > div > div.SectionSearchContent > div.section_search_content > div > div.article_list_area > ul > li:nth-child('+str(i)+') > div > div > div > a').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1]) # 현재 탭으로 전환

        driver.switch_to.frame('cafe_main') #iframe 제거

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        try:
            tit = soup.find('h3', class_ = 'title_text').text
            
        except:
            pass
        
     #   title_list.append(tit)
        tit = re.sub('[^0-9a-zA-Zㄱ-ㅣ-가-힣 ]',"",tit)
        search.append(tit)
       
        #제목 크롤링

      

        try:
            con = soup.find('div', class_="se-main-container").text
        except:
            try:
                con2 = soup.find('div',class_='se-text').text
                con = con + con2
            except:
                pass

        con = re.sub('[^0-9a-zA-Zㄱ-ㅣ-가-힣 ]',"",con)
       # con_list.append(con)
        search.append(con)
        #내용 크롤링

        try:
            dat = soup.find('span', class_ = 'date').text
            
        except:
            pass

        dat = re.sub('[^0-9a-zA-Zㄱ-ㅣ-가-힣 ]',"",dat)
        dat = dat[0:8]
        search.append(dat)


        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        df.loc[idx] = [tit, con, dat]
        df.to_csv('cafe_스티치_1000.csv')
        print ("count : " ,count ,"idx : " , idx)
        idx += 1
        if(idx > 1000):
            break


    
    try:
        driver.find_element_by_css_selector('#mainContainer > div > div.SectionSearchContent > div.section_search_content > div > div.article_list_area > div > div > div > a:nth-child('+str(count+2)+')').click()
    except:
        driver.find_element_by_css_selector('#mainContainer > div > div.SectionSearchContent > div.section_search_content > div > div.article_list_area > div > div > div > a:nth-child(8)').click()
    
    count+=1
    time.sleep(1)
df
