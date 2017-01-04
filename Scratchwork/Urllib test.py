import requests

url="http://www.nytimes.com/2016/12/04/world/europe/norbert-hofer-austria-election.html"

res = requests.get(url)

print(res.text)

target = open("Austria.txt", "w")

target.write(res.text)

target.close()