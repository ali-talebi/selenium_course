from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import pytest 
import time 


@pytest.fixture(scope = 'module' ) 
def interface_driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver  = webdriver.Chrome(service=service)
    
    yield driver  


@pytest.mark.login
def tfu_login(interface_driver , request ) : 
    email_of_user = request.config.getoption('--email')
    password_of_user = request.config.getoption('--password')

    interface_driver.get("https://quera.org/")
    interface_driver.find_element(By.XPATH , '//a[@href = "/accounts/login" ]').click()
    interface_driver.find_element(By.XPATH , '//input[@type="email" and @name="login" ]').send_keys(email_of_user)
    interface_driver.find_element(By.XPATH , '//input[@type="password" and @name="password"]').send_keys(password_of_user)
    interface_driver.find_element(By.XPATH , '//button[@type="submit" and text() ="ورود"]').click()
    interface_driver.maximize_window()
    interface_driver.find_element(By.XPATH , "//header/div[@id='qnav__container']/div[@id='qnav__rightmenu']/a[@href='/problemset']").click() 
    
    table = WebDriverWait(interface_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    
    interface_driver.find_element(By.XPATH , '//span[@class="chakra-checkbox__label css-6x44c9"]//span[text()="ساده"]').click()
    time.sleep(3)
    interface_driver.find_element(By.XPATH , '//span[@class="chakra-checkbox__label css-6x44c9"]//span[text() = "متوسط" ]').click()
    time.sleep(3)
    interface_driver.find_element(By.XPATH , '//button[text() = "حذف همه" ]' ).click()
    time.sleep(3)
    total_rows = interface_driver.find_elements(By.XPATH , "//table[@class='chakra-table css-sp7w10']/tbody/tr") 
    print("total rows : " , len( total_rows ) ) 


    for index , value in enumerate(total_rows) :
        total_cell = value.find_elements(By.XPATH , "//td[3]") 
        total_text = [i for i in total_cell]
        print("total text " , total_text)
        print(" ****************************************************************** " )


    total_third_td = interface_driver.find_elements(By.XPATH , "//table[@class='chakra-table css-sp7w10']//td[@class='css-y1f195']")
    print( "*** Third *** " , total_third_td )
    r = [i.text for i in total_third_td ]
    print("R Third ** " , r ) 
    interface_driver.find_element(By.XPATH , "//span[@class='chakra-text css-8bp4l9' and text()='بیشترین حل']").click() 
    search_input = interface_driver.find_element(By.XPATH , "//input[@class='chakra-input css-1m07af1']")
    search_input.send_keys("SELENIUM ali talebi" + Keys.ENTER )
    actions = ActionChains(interface_driver)
    #actions.key_down(Keys.CONTROL).send_keys('a').key_up()
    
    actions.key_down(Keys.SHIFT).send_keys_to_element(search_input , "selenium ali tlaebi shahroodi ").send_keys_to_element(search_input , Keys.SHIFT).send_keys("olt team").perform()
    search_input.clear()
    search_input.click()
    search_input.clear()
    time.sleep(1)


@pytest.mark.doubleclick
def tfu_doubleclick(interface_driver) :
    actions = ActionChains(interface_driver) 
    interface_driver.get('https://trytestingthis.netlify.app/')
    element = interface_driver.find_element(By.XPATH , '//*[text() = "Double-click me"]')
    time.sleep(4)
    actions.double_click(element).perform()
    time.sleep(5)
    interface_driver.find_element(By.XPATH , '//*[text()="Your Sample Double Click worked!"]')
    time.sleep(5)


@pytest.mark.rightclick
def tfu_rightclick(interface_driver):
    interface_driver.get('https://trytestingthis.netlify.app/')
    element = interface_driver.find_element(By.XPATH , "//input[@id='fname']")
    actions = ActionChains(interface_driver)
    time.sleep(3)
    actions.context_click(element).perform()
    time.sleep(3)



@pytest.mark.tooltips
def tfu_tool_tips(interface_driver) : 
    interface_driver.get('https://trytestingthis.netlify.app/')
    element = interface_driver.find_element(By.XPATH , '//div[@class="tooltip"]')
    actions = ActionChains(interface_driver)
    time.sleep(3)
    actions.move_to_element(element).perform()
    findtext = interface_driver.find_element(By.XPATH , "//span[@class='tooltiptext']").text 
    assert findtext == "This is your sample Tooltip text"
    time.sleep(3)

@pytest.mark.increase_decrease 
def tfu_increase_decrese(interface_driver) : 
    interface_driver.get('https://demos.telerik.com/kendo-ui/circular-gauge/index')
    time.sleep(3)
    interface_driver.find_element(By.XPATH , '//*[text() = "default" and @class="theme-name"]').click()
    select_color = interface_driver.find_element(By.XPATH , "//*[text() = 'Purple' and @class='theme-name']").click()
    increase = interface_driver.find_element(By.XPATH , '//button[@title="Increase"]')
    decrease = interface_driver.find_element(By.XPATH , '//button[@title="Decrease"]')
    actions = ActionChains(interface_driver)

    time.sleep(10)
    actions.click_and_hold(increase).pause(3).release().click_and_hold(decrease).pause(3).perform()
    time.sleep(10)


