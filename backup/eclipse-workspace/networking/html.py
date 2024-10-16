import urllib.request

try:
    url= urllib.request.urlopen("https://python.org")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("Web page is not found")
    
f = open("python.html","wb")
f.write(content)
f.close()
    