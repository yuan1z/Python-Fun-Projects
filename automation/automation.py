from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
print('Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title)
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
in_message = chrome_browser.find_element_by_css_selector('input#sum1.form-control')

in_message.send_keys('caonima')
#chrome_browser.close()