"""
PawFinds Selenium Test Cases
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

class PawFindsTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 PawFinds-Selenium-Tests")
        
        cls.base_url = os.environ.get('APP_URL', 'http://13.60.49.1:4000')
        
        service = Service('/usr/local/bin/chromedriver')
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_01_home_page_loads(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertIn("PawFinds", self.driver.title)
        print("✓ Test 1 Passed: Home page loads successfully")
    
    def test_02_page_title_correct(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertIn("PawFinds", self.driver.title)
        print("✓ Test 2 Passed: Page title is correct")
    
    def test_03_navigation_menu_exists(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        nav_items = ["Home", "Services", "Pets", "Contact Us"]
        page_source = self.driver.page_source
        for item in nav_items:
            self.assertIn(item, page_source)
        print("✓ Test 3 Passed: Navigation menu items exist")
    
    def test_04_pets_page_loads(self):
        self.driver.get(f"{self.base_url}/pets")
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 4 Passed: Pets page loads successfully")
    
    def test_05_services_page_loads(self):
        self.driver.get(f"{self.base_url}/services")
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 5 Passed: Services page loads successfully")
    
    def test_06_contact_page_loads(self):
        self.driver.get(f"{self.base_url}/contact")
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 6 Passed: Contact Us page loads successfully")
    
    def test_07_give_pet_button_exists(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertIn("Give a Pet", page_source)
        print("✓ Test 7 Passed: 'Give a Pet' button exists")
    
    def test_08_login_button_exists(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        page_source = self.driver.page_source
        has_login = "Login" in page_source or "Signup" in page_source or "Sign" in page_source
        self.assertTrue(has_login)
        print("✓ Test 8 Passed: Login/Signup button exists")
    
    def test_09_footer_contains_email(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertIn("laybaashahidd@gmail.com", page_source)
        print("✓ Test 9 Passed: Footer contains contact email")
    
    def test_10_logo_and_branding(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertIn("PawFinds", page_source)
        print("✓ Test 10 Passed: PawFinds branding is present")


if __name__ == '__main__':
    unittest.main(verbosity=2)
