'''Регистрация аккаунта'''
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
# '''3. В разделе "Register", введите email для регистрации'''
# reg_email = driver.find_element(By.ID,"reg_email")
# reg_email.send_keys("alex@sab.com")
# '''4. В разделе "Register", введите пароль для регистрации'''
# reg_password = driver.find_element(By.ID,"reg_password")
# reg_password.send_keys("3250161718")
# '''5. Нажмите на кнопку "Register"'''
# reg_button = driver.find_element(By.CSS_SELECTOR,".woocomerce-FormRow>input:nth-child(3)")
# reg_button.click()
# time.sleep(2)
# driver.quit()


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
# username = driver.find_element(By.ID,"username")
# username.send_keys("alex@sab.com")
# '''4. В разделе "Login", введите пароль для логина'''
# password = driver.find_element(By.ID, "password")
# password.send_keys("3250161718")
# '''5. Нажмите на кнопку "Login"'''
# login_button = driver.find_element(By.CSS_SELECTOR,".login>p:nth-child(3)>input:nth-child(3)")
# login_button.click()
# '''6. Добавьте проверку, что на странице есть элемент "Logout"'''
# logout_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
# logout_element_text = logout_element.text
# if logout_element_text == "Logout":
#     print("На странице есть элемент Logout")
# else:
#     print("Элемент отсутствует")
# time.sleep(2)
# driver.quit()