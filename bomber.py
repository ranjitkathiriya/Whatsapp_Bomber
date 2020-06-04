from selenium import webdriver

driver = webdriver.Chrome("/chromedriver")    # Windows User change path here.
driver.get('http://web.whatsapp.com')

name = " " # Enter Your Name or Group
msg = " "# Message in whatsapp to send
count = 100 # count Number


input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_35EW6').click()

