import sys, requests, bs4, webbrowser

res = requests.get('https://google.com/search?q=' + ''.join(sys.argv[1:]))

#webbrowser.open('https://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()
parseTags = bs4.BeautifulSoup(res.text, "html.parser")
elements = parseTags.select('div#main > div > div > div > a')
numLinks = min(10, len(elements))
fd = open('data.txt', 'r+')

for i in range(numLinks):
    fd.write(str(i + 1) + ': ')
    query = 'https://google.com' + elements[i].get('href') + '\n'
    fd.write(query)
    fd.write('\n')
    #webbrowser.open('https://google.com' + elements[i].get('href'))