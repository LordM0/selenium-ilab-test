import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# set webdriver
response = webdriver.Edge()
response.get('https://ilabquality.com')

# click Careers menu item
try:
    careerButton = response.find_element(By.ID, 'menu-item-1373')
    careerButton.click()
except:
    print("No menu item with that id")

# select South Africa
try:
    countryButton = response.find_element(By.CLASS_NAME,
                                          'vc_general.vc_btn3.vc_btn3-size-lg.vc_btn3-shape-square.vc_btn3-style-gradient-custom.vc_btn3-block.vc_btn-gradient-btn-62f46f9301f0e')
    countryButton.click()
except:
    print("No class with that name")

# click the first job listing
try:
    jobListingButton = response.find_element(By.CLASS_NAME, 'wpjb-job_title.wpjb-title')
    jobListingButton.click()
except:
    print("No class with that name")

# click Apply Online
try:
    applyButton = response.find_element(By.CLASS_NAME, 'wpjb-button.wpjb-form-toggle.wpjb-form-job-apply')
    applyButton.click()
except:
    print("No class with that name")

# enter the applicant name
try:
    nameInput = response.find_element(By.ID, 'applicant_name')
    nameInput.send_keys("Some Nsame")
except:
    print("No input with that id")

# enter the applicant email
try:
    emailInput = response.find_element(By.ID, 'email')
    emailInput.send_keys("automationAssessment@iLABQuality.com")
except:
    print("No input with that id")

# enter the applicant phone
try:
    phoneInput = response.find_element(By.ID, 'phone')
    phoneInput.send_keys(str(0) + str(random.randint(10, 89)) + " " + str(random.randint(100, 999))
                         + " " + str(random.randint(1000, 9999)))
except:
    print("No input with that id")

# send application
try:
    sendButton = response.find_element(By.ID, 'wpjb_submit')
    sendButton.click()
except:
    print("No button with that id")

# print error message
try:
    errorMessage = response.find_element(By.CLASS_NAME, 'wpjb-errors')
    print(errorMessage.text)
except:
    print("No error message")
