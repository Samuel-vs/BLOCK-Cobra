import webbrowser
  
# then make a url variable
url = "https://www.geeksforgeeks.org"
  
# getting path
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
  
# First registers the new browser
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
  
# after registering we can open it by getting its code.
webbrowser.get('brave').open(url)