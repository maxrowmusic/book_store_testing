'''Регистрация аккаунта'''
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
'''2. Нажмите на вкладку "My Account"'''
my_account = driver.find_element(By.ID,"menu-item-50").click()
'''3. В разделе "Register", введите email для регистрации'''

'''4. В разделе "Register", введите пароль для регистрации'''
'''5. Нажмите на кнопку "Register"'''
time.sleep(3)
driver.quit()


'''Логин в систему'''
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# '''1. Откройте сайт'''
# driver.get("https://practice.automationtesting.in/")
# '''2. Нажмите на вкладку "My Account"'''
# my_account = driver.find_element(By.ID,"menu-item-50").click()
# '''3. В разделе "Login", введите email для логина'''
# '''4. В разделе "Login", введите пароль для логина'''
# '''5. Нажмите на кнопку "Login"'''
# '''6. Добавьте проверку, что на странице есть элемент "Logout"'''
# time.sleep(3)
# driver.quit()