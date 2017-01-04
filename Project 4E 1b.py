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

def sniffAndRetrieveContent(fileToParse):

    try:
        ##Converts raw HTML into tree object to step through
        html_doc = open(fileToParse)

        soup = BeautifulSoup(html_doc, 'html.parser')

        ##Create the final file title from the article
        savedStoryName = (soup.title.string) + ".txt"

        ##Steps through tree scraping only article content

        elements = soup.find_all("p", class_=CONTENT_KEYWORD)

        ##Iterates through a 'clean' version of scraped
        ##HTML content

        listOfWholeLines = []

        for i in elements:
            for word in i:
                word = word.string
                listOfWholeLines.append(word)

        ##Returns the final file name and the story
        ##as a list of scraped and rendered HTML lines
        return listOfWholeLines, savedStoryName

    except:
        print("Something happened with sniffAndRetrieveContent. Possible issue with content keyword?")


def compileContent(listOfWholeLines, savedStoryName):
    try:
        ##Take a list of article's lines and creates a
        ##single string. The thinking behind one
        ##line is to have something easy to process
        ##if user decides to split then index the terms
        ##of the article later
        ##
        ##There is one minor issue in the transfer here,
        ##after a period in the article there's no space.
        ##It's a minor thing that can be corrected later

        wholeStory = ""

        for i in range(len(listOfWholeLines)):

            line = listOfWholeLines[i]
            wholeStory = wholeStory + line

        ##Returns the desired news
        ##story as a single string.

        return wholeStory

    except:
        print("Something happened with compileContent, perhaps something's wrong with the compiled list?")

def commitContent(wholeStory, savedStoryName):
    try:
        ##Given the story as a string, and the accompanying
        ##descriptive title, this will create a .txt file
        ##with the descriptive title as its name and
        ##contains the desired story as a single string

        target = open(savedStoryName, "w")
        target.write(wholeStory)
        target.close()

    except:
        print("Something happened with commitContent, perhaps something's off with wholeStory? or savedStoryName?")

def newsScrape(url):

    try:
        rawFile = urlOpenAndWrite(url)

        (list, name) = sniffAndRetrieveContent(rawFile)

        wholeStory = compileContent(list, name)

        commitContent(wholeStory, name)

        ##Once the story has been rendered,
        ##this removes the raw file, which is
        ##not needed anymore.

        os.remove(rawFile)

    except:
        print("Something happened with newsScrape, did you put in the URL for a single article?")


##Mike, these links from nytimes.com are for you
##to plug in and try! Feel free to navigate to
##the site, click on an article, then paste in the
##url into newsScrape.

test1 = "http://www.nytimes.com/2016/12/12/world/europe/rex-tillersons-company-exxon-has-billions-at-stake-over-russia-sanctions.html?partner=rss&emc=rss"
test2 = "http://www.nytimes.com/2016/12/13/us/politics/donald-trump-transition.html?partner=rss&emc=rss"
test3 = "http://www.nytimes.com/2016/12/13/us/politics/rex-tillerson-secretary-state-trump.html?partner=rss&emc=rss"
test4 = "http://www.nytimes.com/2016/12/13/us/politics/rick-perry-energy-secretary-trump.html?partner=rss&emc=rss"
test5 = "http://www.nytimes.com/2016/12/12/world/europe/rex-tillersons-company-exxon-has-billions-at-stake-over-russia-sanctions.html?partner=rss&emc=rss"

newsScrape(test1)

