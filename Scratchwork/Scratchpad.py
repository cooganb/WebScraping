##Trying to create a unique ID name for the text tiles:

##Here's what I came up with:

for i in range(10):
    x = strftime("%a, %d %b %Y %H:%M:%S")
    print(x)
    print(type(x))
    time.sleep(2)

##Below didn't work because x was not in loop

# x = time.localtime()
#
# for i in range(10):
#     print(x)
#     time.sleep(2)
#