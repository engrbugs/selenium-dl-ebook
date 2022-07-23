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

if __name__ == '__main__':
    options = Options()
    options.add_argument(
        "user-data-dir=C:/Users/engrb/AppData/Local/Google/Chrome/User Data/Sel")  # Path to your chrome profile
    options.add_argument('--profile-directory=Sel')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get('https://www.hoopladigital.com/play/14444092')
    tic = time.perf_counter()
    print('please ENTER to continue:', end=":  ")
    input()
    toc = time.perf_counter()
    print(f"load time {toc - tic:0.4f} seconds")
    with open("ebook.txt", "w") as file:
        #  I need 74 pages
        #  The page number computing in the website is wrong
        for i in range(100):
            print(i + 1)
            time.sleep(2)
            #driver.switch_to.default_content()
            frame_reference = driver.find_element(By.TAG_NAME, 'iframe')
            driver.switch_to.frame(frame_reference)
            body1 = driver.find_element(By.TAG_NAME, 'html')
            elements = body1.find_elements(By.XPATH, "./*")
            for e in elements:
                print(e.text)
                file.write(e.text + "\n") if e.text.strip() != "" else None
            time.sleep(1)
            driver.switch_to.default_content()
            next_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/button[2]')
            next_button.click()
            time.sleep(1)
