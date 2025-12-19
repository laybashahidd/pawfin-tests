# PawFinds Selenium Tests

Automated test cases for PawFinds pet adoption web application.

## 10 Test Cases

1. Home page loads successfully
2. Page title is correct
3. Navigation menu exists
4. Pets page loads
5. Services page loads
6. Contact page loads
7. Give a Pet button exists
8. Login/Signup button exists
9. Footer contains email
10. Logo and branding present

## Run Locally
```bash
pip install -r requirements.txt
python -m pytest test_pawfinds.py -v
```

## Run in Docker
```bash
docker build -t pawfin-selenium-tests .
docker run --rm pawfin-selenium-tests
```
