'''
Credits to owner, fixes and updates made by DumbDanny. (dumb danny#9375)
Credits for hCaptcha solver goes to https://chrome.google.com/webstore/detail/noptcha-recaptcha-hcaptch/dknlfmjaanfblgfdfebhijalfmhmjjjo
'''

import os, sys
import warnings
import time, requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string
from colorama import Back, Fore
from os import path

# added title and bit of a info section.
print(f'''
▀█▀ █▀█ █▄▀ █▀▀ █▄░█   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
░█░ █▄█ █░█ ██▄ █░▀█   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄   Made By Damianek02, modified and updated by DumbDanny.

''')
print("Please note that sometimes the hCaptcha solver may need to have the 'auto open' feature enabled.")
print("To fix this issue, click on the extension, and click 'auto open'.")
print(' ')


warnings.filterwarnings("ignore", category=DeprecationWarning) 

file = open("users.txt", "a")
file1 = open("tokens.txt", "a")




def start():
    def get_random_email(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys(result_str + '@wp2.pl') # Changed Method used to find the xpath to the newer, non deprecated method.
        file.write("\n email: " + result_str +"@wp2.pl\n")
        


    def get_random_username(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys(result_str) # Changed Method used to find the xpath to the newer, non deprecated method.
        file.write("username: " + result_str + "\n")


    def get_random_password(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("!" + result_str) # Changed Method used to find the xpath to the newer, non deprecated method.
        file.write("password: " + "!" + result_str)
        


    def get_date(): # removed junk comments,updated methods to find elements and fixed patched xpaths.
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[1]/div/div/div/div/div[1]/div[1]").click()
        driver.find_element(By.ID, "react-select-2-option-0").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[2]/div/div/div/div/div[1]/div[1]").click()
        driver.find_element(By.ID, "react-select-3-option-0").click()
        
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[4]/div[1]/div[3]/div/div/div/div/div[1]").click()
        driver.find_element(By.ID, "react-select-4-option-17").click()


    def get_checkbox():
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div/div/div/form/div/div/div[5]/label/input").click() # Changed Method used to find the xpath to the newer, non deprecated method and fixed patched checkbox method.


    def get_button():
        driver.find_element(By.XPATH, "//button[@type='submit']").click() # Changed Method used to find the xpath to the newer, non deprecated method.

    def quit():
        driver.quit()




    # removed junk comments, added hcaptcha solver and removed language option.
    option = webdriver.ChromeOptions()
    option.add_argument("--mute-audio")
    option.add_extension(os.getcwd() + '\solver.crx') # gets the directory of the hCap solver.
    option.add_experimental_option("excludeSwitches", ["enable-logging"])
    #option.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1")



    driver = webdriver.Chrome(ChromeDriverManager().install(), options = option) # added options = options or else all the code above doesn't really work...
    driver.get('https://discord.com/register')

    time.sleep(2) # added time.sleep(2) to make *sure* that the page is loaded.
    print(f'{Back.GREEN}  INFO  {Back.RESET} Generating Token.')
    get_random_email(8)
    get_random_username(8)
    get_random_password(8)
    get_date()
    get_checkbox()
    get_button()

    # Trys to save token until its succesful.
    token = None
    while token is None:
        token = driver.execute_script("""return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()""")
        if token is None:
            pass
        else:
            print(f'{Back.GREEN}  INFO  {Back.RESET} Token Generated! {token}')
            with open('tokens.txt', 'w') as tokens:
                tokens.write('\n')
                tokens.write(token)
                tokens.close()




amount = int(input('How Many Tokens Would you like to generate: '))

for run in range(amount):
    start()

