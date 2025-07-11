from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime as dt
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
    
    
    driver = webdriver.Chrome(service=service,options=options)
    
    driver.get("http://automated.pythonanywhere.com")
    
    return driver


def clean_text(text):
    
    output = float(text.split(":")[1])
    return output

def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename,'w') as file :
        file.write(text)

def main():
    
    driver = get_driver()
    
    while True:
        time.sleep(5)    
        element = driver.find_element(by="xpath",value='//*[@id="displaytimer"]').text
        text = str(clean_text(element))
        write_file(text)
        

print(main())
        
        
    

    
