import webbrowser

engine = str(input('Enter search engine name: '))
request = str(input('Search: '))

if(engine == 'google'):
    url = 'https://google.com/?q='+request+'&t=h_'
else:
    print('error')
webbrowser.open(url)