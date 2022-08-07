import time
from datetime import date
from re import search
import webbrowser
import os

def runtime(dom,sub):
    token = 'https://www.'+dom+'.'+sub
    return token
def report(unique):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    today = date.today()
    d2 = today.strftime("%d/%m/%y")
    #Recording url in web_log.txt
    fp = open('Web_log.txt', 'a+')
    fp.write('\n''>> '+unique+' || '+d2+' || '+current_time)
    print(test,'has been recorded.')
    fp.close()

name, browser = str(input('Enter name of website and browser code: ')).split()
if(browser ==  'b' or browser == 'e'):
    if(name == 'youtube' or name == 'yt'):
        tld = 'yt_direct'
        sea = str(input('Search on yt: '))
    elif(name == 'spotify' or name == 'sp'):
        tld = 'spotify_direct'
    elif(name =='duckduckgo' or name == 'ddc'):
        tld = 'ddc_direct'
        sea = str(input('Search on ddc: '))
    elif(name == 'cs50'):
        tld = 'cs50_direct'    
    elif(name == 'google' or name == 'gmail' or name == 'outlook' or name == 'flipkart' or name == 'amazon'):
        tld = 'com'

    else:
        tld = str(input('Enter type of site(.com/.org/.in/.net): '))

    if(tld == 'yt_direct'):
        test = 'https://www.youtube.com/results?search_query='+sea+' '
    elif(tld == 'spotify_direct'):
        test = 'https://open.spotify.com/'
    elif(tld == 'ddc_direct'):
        test = 'https://duckduckgo.com/'+sea+'?'
    elif(tld == 'cs50_direct'):
        test = 'https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home'
    else:
        test = runtime(name,tld)

    print('Entered URL: ',test)

    if(browser == 'e'): 
        url = test
        webbrowser.open(url)
    else:
        url = test
        brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        webbrowser.get('brave').open(url)

    report(test)
    print('...')

if(browser == 'o'):
    ext = str(input('Enter: '))
    total = name+ext
    os.system(total)

else:
    print('Invalid browser code, enter one of the following: \nb = brave\ne = edge\no = open file')