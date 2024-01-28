import unittest
from selenium import webdriver
from time import sleep, time
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Firefox()

driver.get('https://tinder.com/app/login')
sleep(3)


time_to_swipe = int(input('Set (in seconds) for how long do you want to swipe right: '))

timeout = 30

def enter_OTP(OTP):
    #OTP prompt
    OTP_input = driver.find_element(By.XPATH, '//input[contains(@aria-label, "OTP code digit 1")]')
    OTP_input.send_keys(OTP)
    sleep(2)
    OTP_input.send_keys(Keys.ENTER)
    sleep(2)

try:
    # Click the "Log in with phone number" button
    login_button = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Log in with phone number"]'))
    )
    login_button.click()

    # Wait until the input with name "phone_number" is present
    phone_number_input = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.NAME, "phone_number"))
    )
    phone_number_input.send_keys(int(input('Insert your phone number: ')))
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[2]/main/div[1]/div[1]/div/div[3]/button').click()
    sleep(2)
    enter_OTP(input('Enter OTP sent by sms: '))
    
    #Send email OTP button
    driver.find_element(By.XPATH, '//*[@id="c537208204"]//button[last()]').click()
    sleep(3)

    enter_OTP(input('Enter OTP sent by email: '))    

except Exception as e:
    # Handle the exception (e.g., print an error message)
    print(f"An error occurred: {str(e)}")


# Location and Notifications pop up
try:
    activate_location_popup = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="onboarding CenterAlign"]/div[contains(@class, "location")]'))
    )

    allow_location = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Allow"]'))
    )
    allow_location.click()

    notifications_popup = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Notifications')]"))
    )

    no_notifications_button = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//div/div/div[@aria-labelledby="onboarding-title"]/div/button[last()]'))
    )
    
    no_notifications_button.click()

except Exception as e:
    # Handle the exception (e.g., print an error message)
    print(f"An error occurred: {str(e)}")
    


# Location and Notifications pop up
sleep(3)
try:
    activate_location_popup = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="onboarding CenterAlign"]/div[contains(@class, "location")]'))
    )

    allow_location = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Allow"]'))
    )
    allow_location.click()

    notifications_popup = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Notifications')]"))
    )

    no_notifications_button = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//div/div/div[@aria-labelledby="onboarding-title"]/div/button[last()]'))
    )
    
    no_notifications_button.click()

except Exception as e:
    # Handle the exception (e.g., print an error message)
    print(f"An error occurred: {str(e)}")



stop = time_to_swipe + time.time()
while time.time() <= stop:
    # super like, upgrade suscription, Home screen pop up
    #(Repeat after every like given)
    
    if(len(driver.find_elements(By.XPATH, '//*[@id="c537208204"]/main/div[1]')) > 0):
        #Close pop up
        try:
            driver.find_elements(By.XPATH, '//*[@id="c537208204"]//button[last()]')[0].click()
        except Exception:
            pass        
    if(len(driver.find_elements(By.XPATH, "//*[contains(text(),'likes you too!')]")) > 0):
        try:
            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, '//button[@title="Back to Tinder"]'))).click()
        except Exception:
            pass
                 
    else:
        # Swipe right
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.RIGHT)

print("Well done, now you are a complete lazy-ass hacker!")
driver. close()