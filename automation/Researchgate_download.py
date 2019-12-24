from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.researchgate.net')
login = chrome_browser.find_element_by_class_name('gtm-header-login')
login.click()
login_page = chrome_browser.find_element_by_xpath('//a[@href="'+'connector/facebook'+'"]')
login_page.click()
chrome_browser.get("https://www.facebook.com/login.php?skip_api_login=1&api_key=117605508256145&kid_directed_site=0&app_id=117605508256145&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D117605508256145%26redirect_uri%3Dhttps%253A%252F%252Fwww.researchgate.net%252Fconnector%252Ffacebook%252Fconnected%26state%3D860d1d060e2d0fce7c556c2aeccb1239%26scope%3Demail%252Cpublic_profile%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9efcf95c-43f0-4205-b454-a919de769b5d&cancel_url=https%3A%2F%2Fwww.researchgate.net%2Fconnector%2Ffacebook%2Fconnected%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D860d1d060e2d0fce7c556c2aeccb1239%23_%3D_&display=page&locale=en_US&pl_dbl=0")
#facebook user name
username = chrome_browser.find_element_by_css_selector('input#email.inputtext._55r1.inputtext._1kbt.inputtext._1kbt').send_keys('xiaoshiyilangtxy@hotmail.com')

#facebook password
password = chrome_browser.find_element_by_id('pass') #grep html element object by id
password.clear()
password.send_keys('19928.27')


login = chrome_browser.find_element_by_css_selector('button#loginbutton._42ft._4jy0._52e0._4jy6._4jy1.selected._51sy')
login.click()

login = chrome_browser.find_element_by_class_name('gtm-header-login')
login.click()
login_page = chrome_browser.find_element_by_xpath('//a[@href="'+'connector/facebook'+'"]')
login_page.click()
'''
search_button = chrome_browser.find_element_by_class_name('search-bar-button')
search_button.click()
search_link = chrome_browser.find_element_by_css_selector('form.header-search-action')
print(search_link)
search_link.send_keys('Lecun')
search_button = chrome_browser.find_element_by_css_selector('button.search-bar-button')
search_button.click()
'''
'''
button = chrome_browser.find_element_by_class_name('btn-default')
print(button.get_attribute('innerHTML')) #get button innerHTML
user_botton2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_botton2)
assert 'Show Message' in chrome_browser.page_source #check element in html page

user_message = chrome_browser.find_element_by_id('user-message') #grep html element object by id
user_message.clear() #clear text box content
user_message.send_keys('I AM EXTRA COOL') #text to the text box
button.click()
output_message = chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text
#chrome_browser.close()
'''