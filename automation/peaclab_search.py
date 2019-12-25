from selenium import webdriver
#chromeOptions = webdriver.ChromeOptions()
#prefs = {"plugins.always_open_pdf_externally": True} #chrome setting disable chrome pdf viewer
#chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "./chromedriver"
chrome_browser = webdriver.Chrome(executable_path=chromedriver)
#chrome_browser = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
chrome_browser.maximize_window()
chrome_browser.get('https://www.bu.edu/peaclab/')
publications = chrome_browser.find_element_by_xpath('//a[@href="'+'https://www.bu.edu/peaclab/publications/'+'"]').click()
zihao_date= chrome_browser.find_element_by_xpath('//a[@href="'+'/peaclab/files/2019/12/DATE2020_zihao.pdf'+'"]').click()
print('all done')
#chrome_browser.find_element_by_xpath('//*[@id="download"]').click()