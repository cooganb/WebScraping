from bs4 import BeautifulSoup
import requests
from time import strftime
import os

##The below is site-specific for Nytimes.com
##I would like to build a dictionary for different
##sites so the user can type in the news site
##and the program would alter itself for that
##
##For now, just Nytimes.com

CONTENT_KEYWORD = "story-body-text story-content"

def urlOpenAndWrite(url):

    try:
        ##Pulls in website content using 'requests' library
        res = requests.get(url)

        ##Creates a unique ID for the raw HTML content
        fileToParse = strftime("%a, %d %b %Y %H:%M:%S") + ".txt"

        ##Commits raw HTML content to a file
        target = open(fileToParse, "w")

        target.write(res.text)

        target.close()

        ##Gives raw HTML content back
        return fileToParse
    except:
        print("Something happened with urlOpenAndWrite. Possible bad link? Bad raw file name?")

def retrieveURLsfromRSS(fileToParse):

##This is just for NYTimes right now,
##Needs to be generalized further

    try:
        ##Converts raw HTML into tree object to step through
        html_doc = open(fileToParse)

        soup = BeautifulSoup(html_doc, 'html.parser')

        ##This is a test to scrape from the RSS page
        ##So some comments will be commented out
        ##Title hardcoded in but ideally will be generated
        ##From page itself
        ##savedStoryName = "NYTimes Homepage RSS from " + strftime("%a, %d %b %Y %H:%M:%S") + ".txt"

        ##Steps through tree scraping only article content

        elements = soup.find_all('guid')

        ##Iterates through a 'clean' version of scraped
        ##HTML content

        ##print(savedStoryName)
        ##print(elements)

        listOfURLs = []

        for i in elements:
             for word in i:
                 word = word.string
                 listOfURLs.append(word)

        ##Returns the final file name and the story
        ##as a list of scraped and rendered HTML lines



        return listOfURLs

    except:
        print("Something happened with retrieveURLsfromRSS. Possible issue with terms to parse RSS? Invalid RSS page?")

listofURLs = retrieveURLsfromRSS(urlOpenAndWrite("http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"))
