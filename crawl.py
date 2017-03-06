#!usr/bin/python
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
session=requests.session()
adapter =HTTPAdapter(max_retries=8)
session.mount('https://', adapter =adapter)
#converts https to something readable
headers= {
'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
#use to recieve desktop information(used as identifier)
}
usr = "https://www.linkedin.com/in/antonio-guion-5578b1114/"
req =session.get(usr, headers=headers)

#html = BeautifulSoup(req.text)


