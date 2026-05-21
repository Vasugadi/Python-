import re

str="hello world: https://www.example.com, http://www.test.com, and https://www.sample.com are some of the URLs in this string."
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\$\$,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
print(url)
