from cgitb import text
import requests
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text
def parser_text(text):
    return text.split('">')[1].split('</')[0]

htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 
soup = BeautifulSoup(htmldata, 'html.parser') 

current_temp = soup.find_all("span", class_="CurrentConditions--tempValue--3a50n") 
chances_rain = soup.find_all("div", class_= "CurrentConditions--phraseValue--2Z18W") 
  
temp = (str(current_temp[0]))
temp_rain = str(chances_rain[0]) 
temp = parser_text(temp)
temp_rain = parser_text(temp_rain)

result = "current_temp " + temp + "  in patna bihar" + "\n" +temp_rain 
n.show_toast("Weather update", result, duration = 10)