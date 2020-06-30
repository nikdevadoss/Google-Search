import sys, requests, bs4, webbrowser

res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))
#webbrowser.open('https://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
print(res.text)
parseTags = bs4.BeautifulSoup(res.text, "html.parser")
elements = parseTags.select('div#main > div > div > div > a')
numLinks = min(5, len(elements))
for i in range(numLinks):
    webbrowser.open('https://google.com' + elements[i].get('href'))