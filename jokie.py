import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

jokie = requests.get('http://www.laughfactory.com/jokes/clean-jokes')
soup = BeautifulSoup(jokie.content,'html.parser')
jokeresult = soup.find('div',class_="joke-text")
print(jokeresult)
#jokeresult = str(jokeresult)
'''li = list(jokeresult.find('div',class_="joke-text"))
print(li)'''
    