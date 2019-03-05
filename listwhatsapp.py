from selenium import webdriver
import time
import random
driver = webdriver.Firefox()
driver.get('https://www.whatsapp.com/')
names = input('enter name of your list (name1,name2,..):')
a = names.split(',')
names = list(a)
msg = input('enter yout massage :')
count = int(input('how many you want:'))
for name in names:
    user = driver.find_element_by_xpath('//span[@title ="{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_2S1VP')
    for i in range(count):
        msg_box.send_keys(msg)
        second =random.randrange(1,17)
        time.sleep(second)
        bottom = driver.find_element_by_class_name('_35EW6')
        bottom.click()

