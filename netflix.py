from selenium import webdriver
from time import sleep


class begin:

    def login():
        driver = webdriver.Chrome()
        driver.get('https://www.netflix.com/browse')
        sleep(2)
        r_username = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[1]/div[1]/div/label/input')
        r_username.send_keys('write_user_email_id_here')
        r_password = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/div/label/input')
        r_password.send_keys('write_password_here')
        enter = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        enter.click()
        sleep(2)
        rafe = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div['
                                                 '2]/div/div/ul/li[3]/div/a/div/div')
        rafe.click()
        search=driver.find_elements_by_class_name('')
        search.click()



begin.login()
'''
search.click()
'''
