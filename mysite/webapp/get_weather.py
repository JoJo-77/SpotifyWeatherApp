from bs4 import BeautifulSoup
import urllib


#Populates a dictionary with data from the website, returns None if the connection fails
def get_data(input):
	data = {}
	if input == "swampletics":
		data["easter_egg"] = "Meet pyletics my python locked ultimate mood playlist website -man"
		input = 22030
	url = "https://www.weather.gov/" + input

	try:
		con = get_connection(url)
	except:
		return None

	soup = BeautifulSoup(con.read(), "html.parser")
	data["location"] = soup.find("h2", attrs={"class": "panel-title"}).text.strip()
	data["weather"] = soup.find("p", attrs = {"class": "myforecast-current"}).text.strip()
	data["temperature"] = soup.find("p", attrs = {"class": "myforecast-current-lrg"}).text.strip() + " / " + soup.find("p", attrs = {"class": "myforecast-current-sm"}).text.strip()
	data["wind_speed"] = soup.findAll("td", attrs = {"class": None})[1].text.strip()
	if(data["wind_speed"]) == "Calm":
		data["wind_speed"] = "0"
	else:
		data["wind_speed"] = str([int(s) for s in data["wind_speed"].split(" ") if s.isdigit()][0]) 
	data["mood"] = None
	return data

def get_connection(url):
	req = urllib.request.Request(url, headers = {"User-Agent":"Magic Browser"})
	return urllib.request.urlopen(req)

#Hardcoded if statements to find mood of playlist by looking for keywords in weather
#Returns updated dictionary of data
def get_mood(data):
	#do not allow fall through for hard weathers such as rain, wind, or snow
	try:
		if data["easter_egg"]:
			data["mood"] = "osrs"
			return data
	except:
		if "sunny" in str.lower(data["weather"]) or "fair" in str.lower(data["weather"]) or "a few clouds" in str.lower(data["weather"])  :
			data["mood"] = "sunny"

		if int(data["wind_speed"]) > 15 or "breezy" in str.lower(data["weather"]):
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




