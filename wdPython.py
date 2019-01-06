#class Person(object):
#    def __init__(self, name):
#        self.name = name
#
#    def reveal_id(self):
#        print("My name is {}".format(self.name))
#
#
#
#luke = Person('Luke')
#luke.reveal_id()

import requests
import urllib2
from fbchat import Client
from getpass import getpass
from fbchat.models import *
from getpass import getpass
from bs4 import BeautifulSoup

fantasy_page = 'https://football.fantasysports.yahoo.com/f1/buzzindex?sort=BI_S&src=combined&bimtab=ALL&pos=ALL&date=2018-12-20'

page = urllib2.urlopen(fantasy_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find_all('a', attrs={'class': 'Nowrap'})

trendLen = len(soup.find_all('a', attrs={'class': 'Nowrap'}))

print trendLen

i = 0



for i in range(trendLen):
    name_box[i] = name_box[i].text.strip()

i = 0

while i < trendLen:
    print name_box[i]
    i = i + 1

username = # Enter your email
password = # Enter your password
client = Client(username, password)

i = 0

while i < 10:
    sent = client.send(Message(text=name_box[i]), thread_id=client.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")
    i = i + 1

client.logout()







