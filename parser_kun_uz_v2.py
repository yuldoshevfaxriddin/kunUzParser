import requests
import bs4

url = 'https://kun.uz'

def getHtml(base_url):
    # returned html to string
    respons_text = requests.get(base_url)
    return respons_text.text

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

if __name__=='__main__':
    # running code
    html_text = getHtml(url)
    main_bs4 = getBs4(html_text)
    category_list = getCategory(main_bs4)
    region_list = getRegion(main_bs4)
    print(region_list)