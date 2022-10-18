import fake_headers
import bs4
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = "https://habr.com/ru/all/"
HEADERS = fake_headers.Headers(browser='chrome', os='win', headers=True).generate()
responce = requests.get(URL, headers=HEADERS)
text = responce.text
soup = bs4.BeautifulSoup(text, features="html.parser")
articles = soup.find_all("article")
for article in articles:
    search_article = article.find_all(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
    url = "https://habr.com" + article.find(class_="tm-article-snippet__title-link").get('href')
    get_webpage = requests.get(url, headers=HEADERS)
    text_webpage = get_webpage.text
    soup_webpage = bs4.BeautifulSoup(text_webpage, features="html.parser")
    article_webpage = soup_webpage.find(class_="tm-article-body").find_all("p")
    for key in KEYWORDS:
        if key in str(article_webpage):
            title = article.find(class_="tm-article-snippet__title-link").find('span').text
            search_time = article.find("time").get("datetime")
            print(f'{search_time} - {title} - https://habr.com{url} ')
