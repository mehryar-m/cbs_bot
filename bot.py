## twitter bot to generate corporate bullshit
## inspired by cbs

from secrets import *
from bs4 import BeautifulSoup
import urllib3
import tweepy

# grab the authorizations
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)  
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)  
api = tweepy.API(auth) 

# read in corporate bullshit generator
url = 'http://cbsg.sourceforge.net/cgi-bin/live'
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data, "html.parser")

for li in soup.findAll('li'):
  size = len(str(li.get_text()))
  if (size < 140):
    api.update_status(li.get_text())
    break
  print(len(str(li.get_text()).strip()))
  ## api.update_status(li.get_text())
