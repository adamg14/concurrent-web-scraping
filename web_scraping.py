import requests
from bs4 import BeautifulSoup;
import sys

def web_scraping(url):
    about_elon = False
    
    response = requests.get(url)
    # content of the webpage as a string 
    content_string = str(response.content)
    parse_html = BeautifulSoup(content_string, "html.parser")
    
    # news article title
    titles = parse_html.find_all('title')
    # if title and subtitle include anything about Elon Musk and his companies the article is about him
    for i in range(len(titles)):
        if ("Elon" in str(titles[i])):
            about_elon = True
        if ("Musk" in str(titles[i])):
            about_elon = True
        if ("X" in str(titles[i]) and "Social Media" in str(titles[i])):
            about_elon = True
        if ("SpaceX" in str(titles[i])):
            about_elon = True
        if ("Tesla" in str(titles[i])):
            about_elon = True
        if ("HyperLoop" in str(titles[i])):
            about_elon = True
        if ("Neuralink" in str(titles[i])):
            about_elon = True
    
    # any heading tags
    h1_tags = parse_html.find_all('h1')
    h2_tags = parse_html.find_all('h2')
    h3_tags = parse_html.find_all('h3')
    h4_tags = parse_html.find_all('h4')
    
    for i in range(len(h1_tags)):
        if ("Elon" in str(h1_tags[i])):
            about_elon = True
        if ("Musk" in str(h1_tags[i])):
            about_elon = True
        if ("X" in str(h1_tags[i]) and "Social Media" in str(h1_tags[i])):
            about_elon = True
        if ("SpaceX" in str(h1_tags[i])):
            about_elon = True
        if ("Tesla" in str(h1_tags[i])):
            about_elon = True
        if ("HyperLoop" in str(h1_tags[i])):
            about_elon = True
        if ("Neuralink" in str(h1_tags[i])):
            about_elon = True
    
    # if the headings and titles do not include any keywords associated with Elon Musk, the articles paragraph tags must explicity mention his name
    paragraph_tags = parse_html.find_all('p')
    for i in range(len(paragraph_tags)):
        if ("Elon Musk" in str(paragraph_tags[i])):
            about_elon = True
            
    if about_elon:
        print("Article associated with Elon Musk")
    else:
        print("Article not associated with Elon Musk")

# second command line argument will be the article to be passed into (the first command line arguments after the python command is the script to be run)
web_scraping(sys.argv[1])

