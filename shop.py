'''Отображение страницы товара'''
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
'''2. Залогиньтесь"'''

'''3. Нажмите на вкладку "Shop"'''
shop = driver.find_element(By.ID,"menu-item-40").click()
'''4. Откройте книгу "HTML 5 Forms"'''
'''5. Добавьте тест, что заголовок книги называется: "HTML5 Forms"'''

time.sleep(3)
driver.quit()

'''Количество товаров в категории'''
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
# '''2. Залогиньтесь'''
#
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Откройте категорию "HTML"'''
# '''5. Добавьте тест, что отображается три товара'''
#
# time.sleep(3)
# driver.quit()

'''Сортировка товаров'''
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
# '''2. Залогиньтесь'''
#
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию'''
# '''5. Отсортируйте товары по цене от большей к меньшей'''
# '''6. Снова объявите переменную с локатором основного селектора сортировки'''
# '''7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей'''
#
# time.sleep(3)
# driver.quit()


'''Отображение, скидка товара'''
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
# '''2. Залогиньтесь'''
#
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Откройте книгу "Android Quick Guide"'''
# '''5. Добавьте тест, что содержимое старой цены = "600.00"'''
# '''6. Добавьте тест, что содержимое новой цены = "400.00"'''
# '''7. Добавьте явное ожидание и нажмите на обложку книги'''
# '''8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик'''
#
# time.sleep(3)
# driver.quit()


'''Проверка цены в корзине'''
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
# '''2. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''3. Добавьте в корзину книгу "HTML5 WebApp Development"'''
# '''4. Добавьте тест, что возле корзины (вверху справа) количество товаров = "1 Item", а стоимость = "180.00"'''
# '''5. Перейдите в корзину'''
# '''6. Используйте явное ожидание, проверьте что в Subtotal отобразится стоимость'''
# '''7. Используйте явное ожидание, проверьте что в Total отобразится стоимость'''
#
# time.sleep(3)
# driver.quit()


'''Работа в корзине'''
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
# '''2. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"'''
# '''4. Перейдите в корзину'''
# '''5. Удалите первую книгу'''
# '''6. Нажмите на Undo (отмена удаления)'''
# '''7. В Quantity увеличьте количество товара до 3 шт для "JS Data Structures and Algorithm"'''
# '''8. Нажмите на кнопку "UPDATE BASKET"'''
# '''9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3'''
# '''10. Нажмите на кнопку "APPLY COUPON"'''
# '''11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."'''
#
#
# time.sleep(3)
# driver.quit()

'''Покупка товара'''
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
# '''2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''3. Добавьте в корзину книгу "HTML5 WebApp Development"'''
# '''4. Перейдите в корзину'''
# '''5. Нажмите "PROCEED TO CHECKOUT"'''
# '''6. Заполните все обязательные поля'''
# '''7. Выберите способ оплаты "Check Payments"'''
# '''8. Нажмите PLACE ORDER'''
# '''9. Используйте явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."'''
# '''10. Используйте явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"'''
#
# time.sleep(3)
# driver.quit()