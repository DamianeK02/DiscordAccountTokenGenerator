import os, sys
import warnings
import time,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string


warnings.filterwarnings("ignore", category=DeprecationWarning) 


file = open("users.txt", "a")
file1 = open("tokens.txt", "a")


def get_random_email(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    driver.find_element_by_xpath("//input[@name='email']").send_keys(result_str +"@wp2.pl")
    file.write("\n email: " + result_str +"@wp2.pl\n")
    


def get_random_username(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    driver.find_element_by_xpath("//input[@name='username']").send_keys(result_str)
    file.write("username: " + result_str + "\n")


def get_random_password(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    driver.find_element_by_xpath("//input[@name='password']").send_keys("!" + result_str)
    file.write("password: " + "!" + result_str)
    


def get_date():
    # driver.find_element_by_xpath("//span[text()='Dzień']").click()
    driver.find_element_by_xpath(".//div[@class='select-2TCrqx inputDay-18OXiE']").click()
    driver.find_element_by_id("react-select-2-option-0").click()

    # driver.find_element_by_xpath(".//span[text()='Miesiąc']").click()
    driver.find_element_by_xpath(".//div[@class='select-2TCrqx inputMonth-IGgn-0']").click()
    driver.find_element_by_id("react-select-3-option-0").click()
    
    # driver.find_element_by_xpath(".//span[text()='Rok']").click()
    driver.find_element_by_xpath(".//div[@class='select-2TCrqx inputYear-2J502p']").click()
    driver.find_element_by_id("react-select-4-option-17").click()


def get_checkbox():
    driver.find_element_by_xpath("//input[@class='inputDefault-3JxKJ2 input-3ITkQf']").click()


def get_button():
    driver.find_element_by_xpath("//button[@type='submit']").click()


def save_token():
    token = input("Input token to save it to file: ")
    file1.write("\n"+token)

def quit():
    driver.quit()
    





option = webdriver.ChromeOptions()
option.add_argument('lang=pl')
option.add_argument("--mute-audio")
option.add_experimental_option("excludeSwitches", ["enable-logging"])
# option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://discord.com/register')

get_random_email(8)
get_random_username(8)
get_random_password(8)
get_date()
get_checkbox()
get_button()
save_token()


kill_process = input("Kill process? Y/N: ")

if kill_process == "Y":
    print("killed")
    quit()
else:
    print("not killed")

