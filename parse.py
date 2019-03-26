from bs4 import BeautifulSoup
import urllib

url = "https://www.weather.gov/" + input("Please Enter Zipcode: ")

req = urllib.request.Request(url, headers = {"User-Agent":"Magic Browser"})

con = urllib.request.urlopen(req)

soup = BeautifulSoup(con.read(), "html.parser")

location = soup.find("h2", attrs={"class": "panel-title"}).text.strip()

weather = soup.find("p", attrs = {"class": "myforecast-current"}).text.strip()

temp = soup.find("p", attrs = {"class": "myforecast-current-lrg"}).text.strip() + " / "

temp += soup.find("p", attrs = {"class": "myforecast-current-sm"}).text.strip()


print(location + '\n'+weather+ '\n'+temp)

