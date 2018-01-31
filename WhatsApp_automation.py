from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

all_names = ['Hack', 'Me', 'Bot'] #contact names you want to send message
msg = 'Good Morning' #messages
count = 3 #number of users

input('Enter anything after scanning QR code') #once you scan then input anything 

for name in all_names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('input-container')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('compose-btn-send')
        button.click()
