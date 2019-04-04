from bs4 import BeautifulSoup
import urllib



def get_data():
	url = "https://www.weather.gov/" + input("Please Enter Zipcode: ")

	req = urllib.request.Request(url, headers = {"User-Agent":"Magic Browser"})

	con = urllib.request.urlopen(req)

	soup = BeautifulSoup(con.read(), "html.parser")

	data = {}

	data["location"] = soup.find("h2", attrs={"class": "panel-title"}).text.strip()

	data["weather"] = soup.find("p", attrs = {"class": "myforecast-current"}).text.strip()

	data["temperature"] = soup.find("p", attrs = {"class": "myforecast-current-lrg"}).text.strip() + " / " + soup.find("p", attrs = {"class": "myforecast-current-sm"}).text.strip()

	data["wind_speed"] = soup.findAll("td", attrs = {"class": None})[1].text.strip()

	data["wind_speed"] = str([int(s) for s in data["wind_speed"].split(" ") if s.isdigit()][0]) 

	data["mood"] = None

def get_mood(data):
	#do not allow fall through for hard weathers such as rain, wind, or snow

	if "sunny" in str.lower(data["weather"]) or "fair" in str.lower(data["weather"]):
		data["mood"] = "sunny"

	if int(data["wind_speed"]) > 15:
		data["mood"] = "windy"

	if "rainy" in str.lower(data["weather"]) or "overcast" in str.lower(data["weather"]):
		data["mood"] = "rainy"
		return data

	if "snowy" in str.lower(data["weather"]):
		data["mood"] = "snowy"
		return data

	if "cloudy" in str.lower(data["weather"]) :
		data["mood"] = "cloudy"
		return data
	return data

data = get_mood(get_data())

print(data) 



