from selenium import webdriver
import unittest

class GetWebpage(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://127.0.0.1:8000/webapp/home")
	def test_getpage(self):
		self.assertEqual(self.driver.title, "Sunny With a Chance of Bops")
	def tearDown(self):
		self.driver.quit()

class InputZIP(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://127.0.0.1:8000/webapp/home")
	def test_putzip(self):
		#element = driver.find_element_by_id("zipcode")
		element = self.driver.find_element_by_name("zipcode")
		element.send_keys("22030")
		#element = self.driver.find_element_by_class_name("btn btn-dark")
		#element.click()
		element.submit()
		assert "https://open.spotify.com/embed" in self.driver.page_source
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
