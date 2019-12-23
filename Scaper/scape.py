import requests
from bs4 import BeautifulSoup
import pprint

def create_custom_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        if subtext[idx].select('.score'): #check if score exists
            points = subtext[idx].select('.score')[0].getText().split(' ')[0]
            if int(points) > 100: #check if score > 100
                hn.append({'title':title,'link':href,'points':points})
    return sorted(hn,key = lambda x:x['points'],reverse = True)

page = 10 #number of page need to scrape
res_num = []
for i in range(1,page+1):
    res_num.append(requests.get(f'https://news.ycombinator.com/news?'+'p={i}'))#grep html data
my_list = []
for res in res_num:
    soup = BeautifulSoup(res.text,'html.parser')
    links = soup.select('.storylink')#grep link using css selector, "." means class
    subtext = soup.select('.subtext')#grep score using css selector, "." means class
    # return news and articles which score > 100
    my_list.extend(create_custom_hn(links,subtext))
pprint.pprint(sorted(my_list,key = lambda x:x['points'],reverse = True))
#scapy is a framework used to do scraping