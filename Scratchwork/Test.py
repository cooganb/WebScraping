from bs4 import BeautifulSoup
import re

##Create Beautiful Soup object
html_doc = open("Austria.txt")

soup = BeautifulSoup(html_doc, 'html.parser')

##Testing to parse out content
mainBody = "story-body-text story-content"

content = soup.select(mainBody)

print(soup.title.string)

#Looked on stackoverflow, found this code snippet, another attempt
#This seems to be successful, seems like my main issue was not
#understanding I needed an underscore after class so i wasn't
#using a prohibited term!

elements = soup.find_all("p", class_=mainBody)

#print(elements)

##Now trying to figure out how to put the information in a file


##Successful attempt of pulling in text!

# for i in elements:
#     print(i.string)

#After successfully pulling in text, am now trying
#put it in a file!

##Realizing that I was screwing up by trying to put the strings
##in whole, need to split them up before! Gonna try for a list

listOfWholeLines = []

for i in elements:
    for word in i:
        word = word.string
        listOfWholeLines.append(word)

print(listOfWholeLines)
print(elements)

target = open("news_text.txt", "w")

wholeStory = ""

for i in range(len(listOfWholeLines)):
    line = listOfWholeLines[i]
    wholeStory = wholeStory + line

print(type(listOfWholeLines[2]))

print(wholeStory)

target.write(wholeStory)

target.close()

##Code below works and produces a document, but it's a little jagged
##I'm going to try and make it a bit cleaner:
#
# for i in range(len(listOfWholeLines)):
#     target.write(listOfWholeLines[i])
#     target.write("\n")

##Below code showed me I was stepping through large
##blocks but what I needed to do was step through
##an index of listOfWholeLines

#Now that I have the whole lines in the list,
#I'd like to step through and chop them up into
#individual words
#
#print(listOfWholeLines[2])

##Below code did not work, only gave me the whole lines
##back again.

# listOfWords = []
#
# for word in listOfWholeLines:
#         listOfWords.append(word)
#
# print(listOfWords)

##Now going to try to write to a file

    ##The below code did not work because some of the lines
    ## return as None, which the write function did not like
    # target = open("news_text.txt", "w")
    #
    # for i in elements:
    #     if i == None:
    #         0==0
    #     else:
    #         target.write(i.string)
    #
    # target.close()


#Another attempt to pull out class = "story-body..."

#print(content)

#print(soup.find_all('p'))
#print(soup.find_all(p('class="story-body-text story-content"')))

#bad code trying to isolate text
#soup.find_all(p=re.compile('class="story-body-text story-content"'))

#bad code trying to print p and pull that into a file
# print(soup.p.prettify())

#htmlContent = soup.find_all(p='class="story-body-text story-content"')

# #print(htmlContent)
# Future code to write to new file

# with open('file_output.html', 'w') as f:
#   for tag in soup.select("#ModelTable"):
#     f.write(tag.prettify())