from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

service = Service("D:\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")

def get_driver():
    
    options = webdriver.ChromeOptions()
    
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Start the Chrome browser with the defined service and options
    driver = webdriver.Chrome(service=service,options=options)
    
    driver.get("http://automated.pythonanywhere.com/login/")
    
    return driver



def clean_text(text):
    
    output = float(text.split(": ")[1])
    return output
    

def main():
    
    driver = get_driver()
    
    # WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.ID, "id_username"))
    # )
    
    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(2)
    
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated"+Keys.RETURN)
    time.sleep(2)
    
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    
    text = driver.find_element(by="xpath",value='//*[@id="displaytimer"]').text
    return clean_text(text)
    


print(main())
    
    
