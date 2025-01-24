from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import pytest 
import time 
from selenium.webdriver.chrome.options import Options 

@pytest.fixture(scope='function')
def driver_interface() : 
    base_option = Options()
    base_option.add_argument('--headless')
    driver = webdriver.Chrome( options=base_option) 
    print("titile : " , driver.title)
    return driver 


@pytest.mark.other 
def tfu_s2(driver_interface) : 
    driver_interface.get("https://mechapars.ir")
    time.sleep(5)
    driver_interface.get("https://avicennasch.com")
    # time.sleep(3)
    # driver_interface.back()
    # time.sleep(3)
    # driver_interface.forward()
    # time.sleep(1)
    # driver_interface.refresh()
    time.sleep(3)
    driver_interface.switch_to.new_window('tab')
    driver_interface.switch_to.new_window('window')
    name_window = driver_interface.current_window_handle 
    total_handles = driver_interface.window_handles 
    print(' , '.join(total_handles))
    driver_interface.switch_to.window(total_handles[0])
    time.sleep(3)
    # driver_interface.quit() ## Squit Session 
    # driver_interface.close() ## tab close 
    
    print(driver_interface.get_window_size())
    print(driver_interface.set_window_size(width = 600 , height = 200))
    size = driver_interface.get_window_size()
    assert size['width'] == 600 and size['height'] == 200 
    driver_interface.set_window_position(150 , 160 )
    print("position : " , driver_interface.get_window_position() ) 
    driver_interface.maximize_window()
    time.sleep(3)
    driver_interface.minimize_window()
    time.sleep(1)
    driver_interface.get("https://www.yahoo.com/")
    driver_interface.driver.execute_script("window.scrollTo(0 , document.body.scrollHeight")

def tfu_s1(driver_interface) : 
    url = "https://play1.automationcamp.ir/forms.html"
    driver_interface.get(url)
    select_box = driver_interface.find_element(By.XPATH , "//input[@id='check_python']").click()
    label_box  = driver_interface.find_element(By.XPATH , "//span[@id='check_validate' and @class='form-text text-success']").text 
    time.sleep(3)
    driver_interface.close() 
    assert 'PYTHON' == label_box 
    
    
    
    
    
