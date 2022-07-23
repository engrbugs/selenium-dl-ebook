# This is a sample Python script.
import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def iinput():
    print('please ENTER to continue:')
    x=input()
    return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #os.environ['PATH'] += r"C:\SeleniumDriver"
    options = Options()
    options.add_argument(
        "user-data-dir=C:/Users/engrb/AppData/Local/Google/Chrome/User Data/Sel")  # Path to your chrome profile
    options.add_argument('--profile-directory=Sel')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get('https://www.hoopladigital.com/play/14444092')
    tic = time.perf_counter()
    print('please ENTER to continue:')
    input()

    toc = time.perf_counter()
    #time.sleep(20)
    print(f"load time {toc - tic:0.4f} seconds")
    # Get element with tag name 'div'
    driver.switch_to.default_content()
    frame_reference = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(frame_reference)
    body1 = driver.find_element(By.TAG_NAME, 'html')

    elements = body1.find_elements(By.XPATH, "./*")

    for e in elements:
        print(e.text)

    #body2 = body1.find_element(By.TAG_NAME, "body")

    #elements = body2.find_element(By.XPATH, ".//")

    #for e in elements:
    #    print(e.text)

    #driver1 = webdriver.Chrome()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
