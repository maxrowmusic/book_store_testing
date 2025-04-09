'''Добавление комментария'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
'''1. Откройте сайт'''
driver.get("https://practice.automationtesting.in/")
'''2. Проскролльте станицу вниз на 600 пикселей'''
driver.execute_script("window.scrollBy(0,600);")
'''3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"'''
selenuim_ruby = driver.find_element(By.CSS_SELECTOR, ".post-160>a>h3").click()
'''4. Нажмите на вкладку "REVIEWS"'''

'''5. Поставьте 5 звезд'''
'''6. Заполните поле "Rewiew" сообщением: "Nice book!"'''
'''7. Заполните поле "Name"'''
'''8. Заполните "Email"'''
'''9. Нажмите на кнопку "SUBMIT"'''
time.sleep(3)
driver.quit()

