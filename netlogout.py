#!/usr/bin/python3

from selenium import webdriver                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                options = webdriver.ChromeOptions()
options.add_argument('headless')
options.binary_location = '/usr/bin/chromium-browser'# chrome path
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://10.0.0.55')
browser.find_element_by_id('username').send_keys('xxxx')# username
browser.find_element_by_id('password').send_keys('xxxx')# password
browser.find_element_by_id('pc_logout').click()
browser.quit()
