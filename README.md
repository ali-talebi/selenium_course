

Website for Testing : https://trytestingthis.netlify.app/ 

مثال: ارسال فرم با submit()

<form id="loginForm" action="/login" method="post">
    <input type="text" name="username" id="username">
    <input type="password" name="password" id="password">
    <button type="submit" id="submitButton">Login</button>
</form>


ارسال فرم با متد submit()
در اینجا از متد submit() برای ارسال فرم استفاده می‌کنیم:

from selenium import webdriver
from selenium.webdriver.common.by import By

# راه‌اندازی مرورگر
driver = webdriver.Chrome()

# باز کردن صفحه وب
driver.get("http://example.com")

# یافتن فیلدهای ورودی و پر کردن آن‌ها
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("test_user")
password.send_keys("secure_password")

# یافتن دکمه و ارسال فرم
submit_button = driver.find_element(By.ID, "submitButton")
submit_button.submit()  # ارسال فرم

# بستن مرورگر
driver.quit()



نکات مهم
تفاوت با click():

اگر بخواهید روی دکمه کلیک کنید، از click() استفاده می‌کنید.
اگر بخواهید فرم را مستقیماً ارسال کنید، از submit() استفاده می‌کنید.
نیازی به دکمه submit ندارید:

می‌توانید روی هر فیلد درون فرم (مثل فیلدهای ورودی) متد submit() را صدا بزنید، و کل فرم ارسال خواهد شد.

مثال ارسال فرم بدون کلیک روی دکمه:

username = driver.find_element(By.ID, "username")

username.send_keys("test_user")

# ارسال فرم از طریق فیلد ورودی
username.submit()



چه زمانی از submit() استفاده کنیم؟

اگر بخواهید فرم را به صورت مستقیم ارسال کنید بدون اینکه روی دکمه کلیک کنید.


زمانی که دکمه Submit وجود ندارد ولی فرم باید ارسال شود (مثل مواردی که ارسال فرم با فشردن Enter انجام می‌شود).

خطاهای احتمالی
خطای NoSuchElementException: اگر المنتی که submit() روی آن صدا زده می‌شود درون تگ <form> نباشد، خطا رخ می‌دهد.

خطای WebDriverException: اگر از مرورگرهایی استفاده کنید که با نسخه Selenium شما ناسازگار هستند، ممکن است متد submit() به درستی کار نکند.


جمع‌بندی

متد submit() برای ارسال فرم HTML استفاده می‌شود.

می‌تواند روی دکمه‌ها، فیلدهای ورودی یا هر المانی درون یک فرم صدا زده شود.

این متد زمانی مفید است که بخواهید فرم‌ها را بدون کلیک کردن ارسال کنید.





<h3> XPATH Locator in Selenium </h3>

<ul>
    <li> //tag[@attribute = ' ... ' ] </li>
    <li> //tag[@attribute = ' ... ' and /or  @attribute=' ... ' ]</li>
    <li> //tag[(@attribute = ' ... ' and / or  @attribute=' ... ' ) and / or  (@attribute = ' ... ' and @attribute=' ... ' ) ]</li>
    <li> //tag[@attribute='...']/..</li> Parent 
    <li> //tag[@attribute='...']/tag[condition]</li> get child tag . This is Absolute xpath 
    <li> //tag[condition]//tag[condition] </li> search through children  , this is relation xpath 
     //*[@class = 'login form']//*[@name='uname']/.. find parent 
      //*[@class = 'login form']//*[@name='uname'] search childern 
    <li>//tag[condition][index]</li>
    <li>(//tag[condition])[index]</li>
    <li>//tag[tag[condition]]</li> like : //tr[td[text() = 'Actor']] 
    <li>//tag[.//tag[condition]]</li> //tr[.//td[text() = 'Actor']]
    <li>//tag[contains(@attribute , value )]</li> like : //*[contains(@id , 'name')] 
    <li>//tag[]</li> like : //tr[td[last()]] 
    <li>//*[starts-with(@attribute , value )]</li> like : //*[starts-with(@id , 'lna')] 
    <li>//*[normalize-space(text()) = 'option 1']</li> remove space first and last 
    <li>//*[translate(@id , 'what data' , 'replaced data' )]</li> like : //*[transalte('abcd' , 'b' , 'x' )] -> axcd 
    //*[translate(text() , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , 'abcdefghijklmnopqrstuvwxyz' ) = 'option']
    //*[normalize-space(translate(text() , 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' , 'abcdefghijklmnopqrstuvwxyz' ) )  = 'option 1'] 
    //*[string-length(@id) = 4 ] 
    //*[round(text()) = '430' ]
    //*[floar(text()) = '448' ] 
    //*[substring-before(text() , ':') = 'Username']
    Axes 
    <li>  find specific parent :  </li> like : //*[@id='uname']/parent::div[@class='login form'] or //*[@id='uname']/.. or //*[@id='uname']/parent::* 
    <li> find total parent : </li> like : //tr[text() = 'Singer' ]/ancestor::* 
    //tr[td[text() = 'Singer']]/ancestor::table 
    //tr[td[text() = 'Singer']]/ancestor::table[@style='width:100%']
    //*[@id='uname']/ancestor-or-self::*[@id='uname'] # search in ancestor and self 
    //*[@id='uname']/ancestor::*[@id='uname'] # just search in ancestor 
    //tbody//*[text() = 'Singer' ] or //tbody/descendant::*[text() = 'Singer' ] 
    //*[@value='option 1']/following::*[@value='option 1']
    
    
    
    
</ul>
