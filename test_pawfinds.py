"""
PawFinds Selenium Test Cases
Automated browser testing for PawFinds pet adoption web application
Uses headless Chrome for CI/CD pipeline integration
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

class PawFindsTests(unittest.TestCase):
    """Test suite for PawFinds pet adoption website"""
    
    @classmethod
    def setUpClass(cls):
        """Set up headless Chrome browser for all tests"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--remote-debugging-port=9222")
        
        cls.base_url = os.environ.get('APP_URL', 'https://721888ac1dfe2d157ccf48d135dc1761.serveousercontent.com')
        
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=chrome_options)
        cls.driver.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests"""
        cls.driver.quit()
    
    def test_01_home_page_loads(self):
        """Test 1: Verify home page loads successfully"""
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn("PawFinds", self.driver.title)
        print("✓ Test 1 Passed: Home page loads successfully")
    
    def test_02_page_title_correct(self):
        """Test 2: Verify page title contains correct text"""
        self.driver.get(self.base_url)
        time.sleep(2)
        expected_title = "PawFinds"
        self.assertIn(expected_title, self.driver.title)
        print("✓ Test 2 Passed: Page title is correct")
    
    def test_03_navigation_menu_exists(self):
        """Test 3: Verify navigation menu items exist"""
        self.driver.get(self.base_url)
        time.sleep(2)
        nav_items = ["Home", "Services", "Pets", "Contact Us"]
        page_source = self.driver.page_source
        for item in nav_items:
            self.assertIn(item, page_source)
        print("✓ Test 3 Passed: Navigation menu items exist")
    
    def test_04_pets_page_loads(self):
        """Test 4: Verify Pets page loads and displays content"""
        self.driver.get(f"{self.base_url}/pets")
        time.sleep(3)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 4 Passed: Pets page loads successfully")
    
    def test_05_services_page_loads(self):
        """Test 5: Verify Services page loads"""
        self.driver.get(f"{self.base_url}/services")
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 5 Passed: Services page loads successfully")
    
    def test_06_contact_page_loads(self):
        """Test 6: Verify Contact Us page loads"""
        self.driver.get(f"{self.base_url}/contact")
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertTrue(len(page_source) > 1000)
        print("✓ Test 6 Passed: Contact Us page loads successfully")
    
    def test_07_give_pet_button_exists(self):
        """Test 7: Verify 'Give a Pet' button exists on home page"""
        self.driver.get(self.base_url)
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertIn("Give a Pet", page_source)
        print("✓ Test 7 Passed: 'Give a Pet' button exists")
    
    def test_08_login_button_exists(self):
        """Test 8: Verify Login/Signup button exists"""
        self.driver.get(self.base_url)
        time.sleep(2)
        page_source = self.driver.page_source
        has_login = "Login" in page_source or "Signup" in page_source or "Sign" in page_source
        self.assertTrue(has_login)
        print("✓ Test 8 Passed: Login/Signup button exists")
    
    def test_09_footer_contains_email(self):
        """Test 9: Verify footer contains contact email"""
        self.driver.get(self.base_url)
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertIn("laybaashahidd@gmail.com", page_source)
        print("✓ Test 9 Passed: Footer contains contact email")
    
    def test_10_logo_and_branding(self):
        """Test 10: Verify PawFinds branding/logo is present"""
        self.driver.get(self.base_url)
        time.sleep(2)
        page_source = self.driver.page_source
        self.assertIn("PawFinds", page_source)
        print("✓ Test 10 Passed: PawFinds branding is present")


if __name__ == '__main__':
    unittest.main(verbosity=2)
