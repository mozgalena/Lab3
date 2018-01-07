import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(requests.get('https://toipkro.ru/').text, "html.parser")

put = open("soup.prettify.txt", "w", encoding='utf-8')
put.write(soup.prettify())
put.close()

rr = soup.find_all('div', ['side-news', 'main-news', 'bottom-news'])
posts = []
for i in rr:
    items = i.find_all(['div', 'a'], ['item-image', 'item'])
    page_text = ''

    for item in items:
        title = item.find('div', {'class':'title'}).text
        try:
            created = item.find('span', {'class':'created'}).text
        except AttributeError:
            created = 'created = N/A'
        try:
            content = item.find('div', {'class':'content'}).text
        except AttributeError:
            content = 'content = N/A'
        try:
            information = item.find('span', {'class':'information'}).text
        except AttributeError:
            information = 'information = N/A'
        try:
            announcement = item.find('span', {'class':'announcement'}).text
        except AttributeError:
            announcement = 'announcement = N/A'
        try:
            page = item.find_all('a', {'class':'page'})
            for i in page:
                page_text += ' ' + i.text
        except AttributeError:
            page = 'page = N/A'
        posts.append({
                        'title':title,
                        'created':created,
                        'content':content,
                        'page':page_text,
                        'information':information,
                        'announcement':announcement
                     })

for i in range(len(posts)):
    if posts[i]['information'] != 'information = N/A':
        print(posts[i]['information'])
    if posts[i]['announcement'] != 'announcement = N/A':
        print(posts[i]['announcement'])
    print(posts[i]['created'])
    print(posts[i]['page'])
    print(posts[i]['title'])
    print(posts[i]['content'])
    print('\n')

