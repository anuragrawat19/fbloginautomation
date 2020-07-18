from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass 

usr = input("Enter the Email id ")
pwd = getpass('Enter Password:')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.facebook.com/")
print("Facebook Opened")
sleep(1)

username = driver.find_element_by_id("email")
username.send_keys(usr)
print("Email Address is Entered ")

sleep(1)

password = driver.find_element_by_id("pass")
password.send_keys(pwd)
print("Password entered")

login = driver.find_element_by_id("loginbutton")
login.click()
print("Done")