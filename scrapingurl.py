def main():
    import requests
    from bs4 import BeautifulSoup
    from googlesearch import search
    import re
#query = input("Enter what you want to search in google...")
    li = list(search("weather", tld="com", num=10, stop=3, pause=2))
#print(li)
    weatherpage = requests.get('http://www.weather.com/wx/today/?lat=26.87&lon=80.98&locale=en_IN&par=google')
    soup = BeautifulSoup(weatherpage.content,'html.parser')
    result = soup.find(class_ = "today_nowcard-temp")
    result = str(result)
    numbers = re.findall('\d+',result)
    temp = str(numbers[0])+"degree celcius"
    return temp