import re

a = "North Carolina Judge Delays Law Overhauling Elections Panel - The New York Times.txt"

b = open(a)

x = re.compile(r"[A-Z][a-z]*")

print(x.findall(b))

## ^[A-Z].*

