import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ecampus.scu.edu/")

userid = ''
pwd = ''

page_loading = True
while page_loading:
    try:
        driver.find_element_by_id("userid").send_keys(userid)
        driver.find_element_by_id("pwd").send_keys(pwd)
        driver.find_element_by_name("Submit").click()
        page_loading = False
    except:
        print("Page loading. Will try again")
        time.sleep(1)

page_loading = True
while page_loading:
    try:
        driver.get('https://ecampus.scu.edu/psc/csprd92/EMPLOYEE/SA/c/SA_LEARNER_SERVICES.SSS_MY_ACAD.GBL?Page=SSS_MY_ACAD&Action=U')
        page_loading = False
    except:
        print("Page loading. Will try again")
        time.sleep(3)

page_loading = True
while page_loading:
    try:
        driver.find_element_by_id('win0divDERIVED_SSSACA2_SS_UNOFF_TRSC_LINK').click()
        page_loading = False
    except:
        print("Page loading. Will try again")
        time.sleep(1)

page_loading = True
while page_loading:
    try:
        driver.find_element_by_id('DERIVED_AA2_TSCRPT_TYPE3').click()
        driver.find_element_by_xpath("//option[@value='UNOFF']").click()
        time.sleep(2)
        driver.find_element_by_id('GO').click()
        page_loading = False
    except:
        print("Page loading. Will try again")
        time.sleep(5)

# driver.close()
