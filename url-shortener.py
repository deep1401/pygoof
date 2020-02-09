import urllib.request

def shorten(url):
    api="http://tinyurl.com/api-create.php?url="
    short=urllib.request.urlopen(api+url).read()
    return short.decode('utf-8')


url=input("Enter url: ")
print(shorten(url))
