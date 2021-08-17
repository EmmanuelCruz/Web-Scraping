import random
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox("geckodriver.exe")

url = "https://www.olxautos.com.mx/autos_c84"

driver.get(url)