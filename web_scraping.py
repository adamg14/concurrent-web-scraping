import requests
from bs4 import BeautifulSoup;

def web_scraping(url):
    about_elon = False
    
    response = requests.get(url)
    # content of the webpage as a string 
    content_string = str(response.content)
    parse_html = BeautifulSoup(content_string, "html.parser")
    
    # news article title
    titles = parse_html.find_all('title')
    # if title and subtitle include anything about Elon Musk and his companies the article is about him
    print(titles)
    for i in range(len(titles)):
        if ("Elon" in str(titles[i])):
            about_elon = True
            
    
    if about_elon:
        print("Article about Elon")
    else:
        print("Article not about Elon")
        
web_scraping("https://www.bbc.co.uk/news/technology-66850821")
web_scraping("https://news.sky.com/story/youtube-suspends-adverts-on-russell-brands-videos-after-comedian-accused-of-rape-and-sexual-assault-12964714")

