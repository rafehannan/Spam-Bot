import PyPDF2 as p2
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class pdf:
    pdf_file = open("pdf_file_name.pdf","rb")
    def parser(pdf_file):
        pdf_read = p2.PdfFileReader(pdf_file)
        num_pages = pdf_read.getNumPages()
        count = 0
        text = ""
        while count < num_pages:
            pageObj = pdf_read.getPage(count)
            count += 1
            text += pageObj.extractText()
        return (text)

class bot:

    def spam():
        pdf_file = open("pdf_file_name.pdf", "rb")
        spam_msg = ""
        spam_msg += pdf.parser(pdf_file)
        driver = webdriver.Chrome()
        driver.get('https://www.messenger.com/login/')
        driver.implicitly_wait(4)
        press = ActionChains(driver)
        r_username = driver.find_element_by_xpath(
            '//*[@id="email"]')
        r_username.send_keys('insert_email_ID_here')
        r_password = driver.find_element_by_xpath(
            '//*[@id="pass"]')
        r_password.send_keys('insert_password_here')
        enter = driver.find_element_by_xpath('//*[@id="loginbutton"]')
        enter.click()
        driver.get('insert_URL_of_target_friend(eg_https://www.messenger.com/t/saif.haque.186)')
        press.send_keys(spam_msg).perform()
        press.send_keys(Keys.ENTER).perform()
        sleep(2)

bot.spam()