from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36"
)

driver = webdriver.Chrome('chromedriver.exe', options=opts)

url = 'https://www.google.com/recaptcha/api2/demo'
driver.get(url)

driver.switch_to.frame(driver.find_element_by_xpath('//iframe'))
captcha = driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-border"]')
print(captcha)
captcha.click()

input()

driver.switch_to.default_content()

submit = driver.find_element_by_xpath('//input[@id="recaptcha-demo-submit"]')
submit.click()

# Ya se habría pasado el captcha
contenido = driver.find_element_by_xpath('//div[@class="recaptcha-success"]')

print(contenido.text)