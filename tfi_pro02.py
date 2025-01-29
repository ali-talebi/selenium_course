from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import pytest 
import time 
from selenium.webdriver.chrome.options import Options 


@pytest.fixture 
def driver_interface() : 
    driver = webdriver.Chrome()
    yield driver
    
@pytest.mark.login
def tfu_login(driver_interface) : 
    driver_interface.get('https://quera.org/')
    driver_interface.find_element(By.XPATH , '//a[text() ="ورود"]' ).click()
    driver_interface.find_element(By.XPATH , '//button[@type="submit" and @title="Google"]').click()
    driver_interface.find_element(By.XPATH , '//input[@type="email"]').send_keys("alitalebishahroodi@gmail.com")
    driver_interface.find_element(By.XPATH , '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]').click()
    
    time.sleep(100)
    
    
@pytest.mark.check
def tfu_check(driver_interface):
    driver_interface.get('https://quera.org/')
    driver_interface.find_element(By.XPATH , '//a[text() ="ورود"]' ).click()
    driver_interface.find_element(By.XPATH , '//input[@type="email" and @name="login"]').send_keys("alitalebishahroodi@gmail.com")
    driver_interface.find_element(By.XPATH , '//input[@type="password" and @name="password"]').send_keys("13781378ALI#t")
    driver_interface.find_element(By.XPATH , '//button[text() ="ورود" ]').click()
    driver_interface.find_element(By.XPATH , '//*[@class="UoPmmD2tUnQ41xr2PHDk"]') #  
    time.sleep(10)
    assert True 
    
@pytest.mark.problem 
def tfu_problem(driver_interface) : 
    driver_interface.get('https://quera.org/')
    driver_interface.find_element(By.XPATH , '//a[text() ="ورود"]' ).click()
    driver_interface.find_element(By.XPATH , '//input[@type="email" and @name="login"]').send_keys("alitalebishahroodi@gmail.com")
    driver_interface.find_element(By.XPATH , '//input[@type="password" and @name="password"]').send_keys("13781378ALI#t")
    driver_interface.find_element(By.XPATH , '//button[text() ="ورود" ]').click()
    driver_interface.find_element(By.XPATH , '//a[@data-slug="developer-problemset"]').click()
    driver_interface.find_element(By.XPATH , '//span[@class="chakra-checkbox__label css-6x44c9"]//span[text()="ساده"]').click()
    El = driver_interface.find_element(By.XPATH , '//a[text() ="تراکنش‌های بهینه" ]').text
    assert El == "تراکنش‌های بهینه" 
    rows = driver_interface.find_element(By.XPATH , '//table/tbody/tr')
    print( "rows : " , rows )
    time.sleep(15)
    
