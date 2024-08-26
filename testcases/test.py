from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create an instance of the Chrome WebDriver
driver_path = ChromeDriverManager().install()
# Create an instance of the Chrome WebDriver with the executable path
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()