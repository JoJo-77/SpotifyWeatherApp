#!/usr/bin/env python3
from selenium import webdriver
import unittest

# These tests all require that you have Chrome installed.
# If you use a different browser, try replacing webdriver.Chrome() with
# webdriver.Firefox() or webdriver.InternetExplorer()
class GetWebpage(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/webapp/home")
	def test_getpage(self):
		assert self.driver.title == "Sunny With a Chance of Bops"
	def tearDown(self):
		self.driver.quit()

class CheckSwitchButton_Playlist(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/webapp/home")
	def image_search(self):
		element = self.driver.find_element_by_class_name("btn btn-secondary")
		element.submit()
		assert "Switch to: playlists" in self.driver.page_source
	def tearDown(self):
		self.driver.quit()

class CheckSwitchButton_Song(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/webapp/homeSong")
	def image_search(self):
		element = self.driver.find_element_by_class_name("btn btn-secondary")
		element.submit()
		assert "Songs" in self.driver.page_source
	def tearDown(self):
		self.driver.quit()

class InputZIP_Playlist(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/webapp/home")
	def test_zip(self):
		element = self.driver.find_element_by_name("zipcode")
		element.send_keys("22030")
		element.submit()
		assert "https://open.spotify.com/embed" in self.driver.page_source
	def tearDown(self):
		self.driver.quit()

class InputZIP_Song(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://127.0.0.1:8000/webapp/homeSong")
	def test_zip(self):
		element = self.driver.find_element_by_name("zipcode")
		element.send_keys("22030")
		element.submit()
		assert "https://open.spotify.com/embed" in self.driver.page_source
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
