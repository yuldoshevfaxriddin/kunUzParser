import requests
import bs4
import json

url = 'https://kun.uz'
url_authored = 'https://kun.uz/authored'

def getHtml(base_url,header=None):
    # returned html to string
    respons_text = requests.get(base_url,headers=header)
    return  respons_text.text

def getBs4(base_html):
    # returned bs4 object
    return bs4.BeautifulSoup(base_html,'lxml')

def getCategory(base_bs4:bs4):
    # returned list categorys
    category_li = base_bs4.find('div', {"class": "page-header__wrapper"}).find_all('li')
    category_list = []
    for i in category_li:
        data = {
            'name':i.find('a').text,
            'link':url+i.find('a')['href']
        }
        category_list.append(data)
    return category_list
    
def getRegion(base_bs4:bs4):
    # returned list regions
    region_li = base_bs4.find('div', {"class": "countries-list"}).find_all('li')
    region_list = []
    for i in region_li:
        data = {
            'name':i.find('a').text,
            'link':url+i.find('a')['href']
        }
        region_list.append(data)
    return region_list
def loadsXhrRequest(xhr):
    xhr_header = {'X-Requested-With':'XMLHttpRequest'}
    xhr_json = {}
    for k in xhr.keys():
        xhr_json[k] = json.loads(getHtml(xhr[k],header=xhr_header))
    with open('json.json','w') as file:
        file.write(json.dumps(xhr_json))

def newsList(base_html):
    news_list_html = getBs4(base_html=base_html).find_all('div',{'class':'col-md-4 mb-25 l-item'})
    news_list = []
    for news in news_list_html:
        item = {
            'image':news.find('img')['src'],
            'meta-data':news.find('div').find('span').text,
            'original-url':url+news.find('a')['href'],
            'tittle':news.find('a',{'class':'news__title'}).text
        }
        item['content']=getBs4(getHtml(item['original-url'])).find('div',{'class':'single-content'}).text;
        news_list.append(item)
    return news_list

xhr = {
    'xhr_main' :'https://kun.uz/time/news/main',
    'xhr_actual' :'https://kun.uz/news/list?f=actual',
    'xhr_interview' : 'https://kun.uz/news/list?f=interview',
    'xhr_authored' : 'https://kun.uz/news/list?f=authored',
    'xhr_busines' : 'https://kun.uz/news/list?f=business',
    'xhr_video' : 'https://kun.uz/news/list?f=video&t=1',
    'xhr_photo' : 'https://kun.uz/news/list?f=photo&t=1'
}

if __name__=='__main__':
    
    news_list = newsList(getHtml(url_authored))
    with open('test.html','w',encoding='utf-8') as f:
        f.write(json.dumps(news_list))