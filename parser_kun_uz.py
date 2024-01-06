

import requests as r
import bs4


API_TOKEN = '<bot token>'
URL_HOST = "https://kun.uz"
#URL = "https://kun.uz/news/list?f=selected"
URL = "https://kun.uz/news/category/uzbekiston"

send_request = r.get(URL)
html_text = send_request.text 
HTML = bs4.BeautifulSoup(html_text, 'html.parser')
news_list = HTML.find_all("div", {"id": "news-list"})
news = bs4.BeautifulSoup(str(news_list), 'html.parser').find_all("div", {"class": "news"})

sendPhoto = f"https://api.telegram.org/bot{API_TOKEN}/sendPhoto"
chat_id = '1742197944' # 

#print(len(news))
JSON = list()
for i in news:
    
    temp = dict()
    
    img = i.find("img").attrs["src"]
    location = URL_HOST + i.find("a").attrs["href"]
    date = i.find("span").text
    title = i.find("a",{"class": "news__title"}).text
    '''
    print(img)
    print(location)
    print(date)
    print(title)
    '''        

    key_words =  {'photo':img ,'caption': title + location + ' \nHabar vaqti :'+date ,'chat_id':chat_id}
    result= r.post(sendPhoto,params = key_words)
    print(result)
        
    temp["img"] = img
    temp["location"] = location
    temp["date"] = date
    temp["title"] = title
    JSON.append(temp)
    #break

text =  str(JSON)
#print(text)

import json

with open('kun_uz_json.txt', 'w') as file:
     file.write(json.dumps(JSON)) # use `json.loads`

  

