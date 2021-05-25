import pyshorteners
url=input("Enter URL:")
print("URL after shorting: ",pyshorteners.Shortener().tinyurl.short(url))
