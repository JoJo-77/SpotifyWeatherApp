#!/usr/bin/env python3
import unittest
from get_weather import get_data
from get_weather import get_mood

mood_types = ["sunny", "windy", "rainy", "snowy", "cloudy"]

class GetWeather(unittest.TestCase):
	def test_local(self):
		result = get_data("22031") # Fairfax
		assert (("Sunny" in result["weather"]) or ("Fair" in result["weather"]) or ("Windy" in result["weather"]) or ("Rainy" in result["weather"]) or ("Snowy" in result["weather"]) or ("Cloudy" in result["weather"]))
	def test_midwest(self):
		result = get_data("60007") # Chicago
		assert (("Sunny" in result["weather"]) or ("Fair" in result["weather"]) or ("Windy" in result["weather"]) or ("Rainy" in result["weather"]) or ("Snowy" in result["weather"]) or ("Cloudy" in result["weather"]))
	def test_westcoast(self):
		result = get_data("90001") # Los Angeles
		assert (("Sunny" in result["weather"]) or ("Fair" in result["weather"]) or ("Windy" in result["weather"]) or ("Rainy" in result["weather"]) or ("Snowy" in result["weather"]) or ("Cloudy" in result["weather"]))

class GetMood(unittest.TestCase):
	def test_local(self):
		result = get_mood(get_data("22031")) # Fairfax
		assert result["mood"] in mood_types
	def test_midwest(self):
		result = get_mood(get_data("60007")) # Chicago
		assert result["mood"] in mood_types
	def test_westcoast(self):
		result = get_mood(get_data("90001")) # Los Angeles
		assert result["mood"] in mood_types

if __name__ == "__main__":
	unittest.main()
