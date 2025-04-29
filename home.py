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
time.sleep(2)
'''3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"'''
selenuim_ruby = driver.find_element(By.CSS_SELECTOR, ".post-160>a>h3").click()
'''4. Нажмите на вкладку "REVIEWS"'''
reviews = driver.find_element(By.CLASS_NAME,"reviews_tab").click()
'''5. Поставьте 5 звезд'''
star_5 = driver.find_element(By.CLASS_NAME,"star-5").click()
'''6. Заполните поле "Rewiew" сообщением: "Nice book!"'''
comment = driver.find_element(By.ID,"comment")
comment.send_keys("Nice book!")
'''7. Заполните поле "Name"'''
name = driver.find_element(By.ID, "author")
name.send_keys("Alex")
'''8. Заполните "Email"'''
email = driver.find_element(By.ID,"email")
email.send_keys("alex@sab.com")
'''9. Нажмите на кнопку "SUBMIT"'''
submit = driver.find_element(By.CSS_SELECTOR,".form-submit>#submit").click()
time.sleep(3)
driver.quit()

