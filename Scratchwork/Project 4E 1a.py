from bs4 import BeautifulSoup
import requests
from time import strftime
import os
#url = ""
#writeFileName = ""
#contentKeyword = ""
#fileToParse = ""
#savedStoryContent = ""

url = "http://www.nytimes.com/2016/12/13/us/politics/rex-tillerson-secretary-state-trump.html"
# writeFileName = "Test_File.txt"
# CONTENT_KEYWORD = "story-body-text story-content"
# fileToParse = writeFileName
# savedStoryName = "Save_Test.txt"
# list = []
# string = ""

def urlOpenAndWrite(url):

    try:

        res = requests.get(url)

        fileToParse = strftime("%a, %d %b %Y %H:%M:%S") + ".txt"
        ##print(res.text)

        target = open(fileToParse, "w")

        target.write(res.text)

        target.close()

        return fileToParse
    except:
        print("Something happened with urlOpenAndWrite. Possible bad link? No article name?")

def sniffAndRetrieveContent(fileToParse):

    try:
        ##Create Beautiful Soup tree to step through
        html_doc = open(fileToParse)

        soup = BeautifulSoup(html_doc, 'html.parser')

        ##Create the doc title from the article
        savedStoryName = (soup.title.string) + ".txt"

        ##Parsing and scraping desired content

        #content = soup.select(CONTENT_KEYWORD)
        elements = soup.find_all("p", class_=CONTENT_KEYWORD)

        #target = open(savedStoryName, "w")

        ##Transfering this from BS object to list

        listOfWholeLines = []

        for i in elements:
            for word in i:
                word = word.string
                listOfWholeLines.append(word)

        return listOfWholeLines, savedStoryName

        ##Iterating list to create single file text
        ##(Single file might be easier to step through
        ##For indexing later, is the thinking here)
        ##THIS COULD POSS. BE ANOTHER FUNCTION

        #wholeStory = ""

        # for i in range(len(listOfWholeLines)):
        #     line = listOfWholeLines[i]
        #     wholeStory = wholeStory + line

        ##Write the content to a file
        ##THIS COULD MOST LIKELY BE ANOTHER FUNCTION

        #target = open(savedStoryName, "w")
        #target.write(wholeStory)
        #target.close()

    except:
        print("Something happened with sniffAndRetrieveContent. Possible issue with parsing? Or title name?")

def compileContent(listOfWholeLines, savedStoryName):
    try:
        wholeStory = ""

        for i in range(len(listOfWholeLines)):

            line = listOfWholeLines[i]
            wholeStory = wholeStory + line

        return wholeStory

    except:
        print("Something happened with compileContent")

def commitContent(wholeStory, savedStoryName):
    try:
        target = open(savedStoryName, "w")
        target.write(wholeStory)
        target.close()

    except:
        print("Something happened with commitContent")

def newsScrape(url):

    try:
        rawFile = urlOpenAndWrite(url)

        (list, name) = sniffAndRetrieveContent(rawFile)
        print(list, name)

        wholeStory = compileContent(list, name)

        print(wholeStory)

        commitContent(wholeStory, name)

        os.remove(rawFile)

    except:
        print("Something happened with newsScrape, passed in bad URL? Strange saved name?")

CONTENT_KEYWORD = "story-body-text story-content"

newsScrape(url)