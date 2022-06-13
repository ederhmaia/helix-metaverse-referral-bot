# commom imports
from colorama import Fore, Back, Style
from colorama import init
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pyautogui
import time
import os
import random
import string

os.environ['WDM_LOG_LEVEL'] = '0'
os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)


def CACHE_DELETE():
    DRIVER.execute_script("window.open('');")  # open new tab
    DRIVER.switch_to.window(DRIVER.window_handles[-1])  # switch to new window
    DRIVER.get('chrome://settings/clearBrowserData')  # open settings
    ACTIONS = ActionChains(DRIVER)
    ACTIONS.send_keys(Keys.TAB * 7)  # tab 7 times
    ACTIONS.send_keys(Keys.RETURN)
    ACTIONS.perform()
    DRIVER.close()  # close the tab
    DRIVER.switch_to.window(DRIVER.window_handles[0])  # switch back
    print(Fore.YELLOW + "-> Cache deleted!")


def GENERATE_RANDOM_PASSWORD():
    password = ''.join(random.choice(
        string.ascii_letters + string.digits) for _ in range(10))
    return password


DRIVER_OPTIONS = Options()
DRIVER_OPTIONS.add_argument("--disable-infobars")

# DRIVER_OPTIONS.add_argument("--headless")
DRIVER_OPTIONS.add_argument("--start-maximized")
DRIVER_OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
DRIVER_OPTIONS.add_argument(
    "user-data-dir=C:\\Users\\ederm\\AppData\\Local\\Google\\Chrome\\User Data\\Default")


REF_CODE = "https://helixmetaverse.com?r=NVT5m2c3"

print('''
-=[ mountain scene at night ]=-  2/97
          _    .  ,   .           .
      *  / \_ *  / \_      _  *        *   /\'__        *
        /    \  /    \,   ((        .    _/  /  \  *'.
   .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
      /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
    /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \ 
   /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
  /jgs     `.  / /       `.~-^=-=~=^=.-'      '-._ `._
''')
print(Fore.MAGENTA + "[!] Helix Referral NFT bot")
print(Fore.MAGENTA + "[@] by @edermxf / @ederhmaia")
print(Fore.MAGENTA + "[@] twitter / instagram")
print(Fore.MAGENTA + "[@] follow me, please, i need your help")
print(Fore.MAGENTA + "[@] I owe millions on loan")
print(Fore.MAGENTA +
      "[@] Donates: (eth/bsc/pol) 0x19f4B913C2ebdEFE887F03Bc1fC8Fa776B0277C9")

EMAIL_FILENAME = input(
    Fore.YELLOW + "-> Enter your email file name: ") or "email.txt"
print(Fore.GREEN + "-> Starting")

WEBDRIVER_SERVICE = Service(ChromeDriverManager().install())


REFERRAL_COUNTER = 0
ERROR_COUNTER = 0

with open(EMAIL_FILENAME, 'r') as f:
    EMAILS = f.readlines()
    print(Fore.GREEN + "-> Loaded " + str(len(EMAILS)) + " emails")

    for LINE in EMAILS:

        DRIVER = webdriver.Chrome(
            service=WEBDRIVER_SERVICE, options=DRIVER_OPTIONS)

        CACHE_DELETE()

        DRIVER.get(REF_CODE)

        CLAIM_BUTTON = WebDriverWait(DRIVER, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Claim Free NFT']//*[name()='svg']")))
        CLAIM_BUTTON.click()

        SIGNUP_EMAIL_BUTTON = WebDriverWait(DRIVER, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Sign Up with Email']")))
        SIGNUP_EMAIL_BUTTON.click()

        EMAIL_INPUT = WebDriverWait(DRIVER, 60).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email address']")))
        EMAIL_INPUT.send_keys(LINE.strip())

        time.sleep(1)

        # submit email address
        ACTIONS = ActionChains(DRIVER)
        ACTIONS.send_keys(Keys.RETURN)
        ACTIONS.perform()

        try:
            SUCCESS = WebDriverWait(DRIVER, 60).until(
                EC.presence_of_element_located((By.XPATH, "//h4[@class='Typography-module--heading--mGHi7 Typography-module--h4--trMLB mt--none mb--none']")))
            REFERRAL_COUNTER += 1
            print(Fore.GREEN + f"[{REFERRAL_COUNTER}] " +
                  LINE.strip() + " -> Success! ")
            DRIVER.quit()
            continue

        except:
            ERROR_COUNTER += 1
            print(Fore.RED + f"[{ERROR_COUNTER}]-> " +
                  LINE.strip() + " -> Error!")
            DRIVER.quit()
            continue

print(Fore.CYAN + "-> Done!")
