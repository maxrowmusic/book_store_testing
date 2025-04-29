'''Отображение страницы товара'''
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
# '''2. Залогиньтесь"'''
# my_account = driver.find_element(By.ID,"menu-item-50").click()
# username = driver.find_element(By.ID,"username")
# username.send_keys("alex@sab.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("3250161718")
# login_button = driver.find_element(By.CSS_SELECTOR,".login>p:nth-child(3)>input:nth-child(3)")
# login_button.click()
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Откройте книгу "HTML 5 Forms"'''
# book = driver.find_element(By.CSS_SELECTOR,".post-181>a>h3")
# book.click()
# '''5. Добавьте тест, что заголовок книги называется: "HTML5 Forms"'''
# name_book = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".summary>h1")))
# name_book_text = name_book.text
# if name_book_text == "HTML5 Forms":
#     print("Заголовок книги называется HTML5 Forms")
# else:
#     print("Заголовок не тот")
# time.sleep(3)
# driver.quit()

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
# my_account = driver.find_element(By.ID,"menu-item-50").click()
# username = driver.find_element(By.ID,"username")
# username.send_keys("alex@sab.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("3250161718")
# login_button = driver.find_element(By.CSS_SELECTOR,".login>p:nth-child(3)>input:nth-child(3)")
# login_button.click()
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Откройте категорию "HTML"'''
# cat_html = driver.find_element(By.CSS_SELECTOR,".product-categories>li:nth-child(2) a").click()
# '''5. Добавьте тест, что отображается три товара'''
# WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,".products>li")))
# product_count = driver.find_elements(By.CSS_SELECTOR,".products>li")
# if len(product_count) == 3:
#     print("Отображается 3 товара")
# else:
#     print("Ошибка. Отображается товаров: ", len(product_count))
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
# my_account = driver.find_element(By.ID,"menu-item-50").click()
# username = driver.find_element(By.ID,"username")
# username.send_keys("alex@sab.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("3250161718")
# login_button = driver.find_element(By.CSS_SELECTOR,".login>p:nth-child(3)>input:nth-child(3)")
# login_button.click()
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию'''
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".woocommerce-ordering select")))
# sorting = driver.find_element(By.CSS_SELECTOR,".woocommerce-ordering select")
# sorting_value = sorting.get_attribute("value")
# if sorting_value == "menu_order":
#     print("Сортировка по умолчанию")
# else:
#     print("Ошибка. Сортировка ",sorting_value)
# '''5. Отсортируйте товары по цене от большей к меньшей'''
# select = Select(sorting)
# select.select_by_value("price-desc")
# '''6. Снова объявите переменную с локатором основного селектора сортировки'''
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".woocommerce-ordering select")))
# sorting_new = driver.find_element(By.CSS_SELECTOR,".woocommerce-ordering select")
# '''7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей'''
# sorting_value_new = sorting_new.get_attribute("value")
# if sorting_value_new == "price-desc":
#     print("Сортировка по цене от большей к меньшей")
# else:
#     print("Ошибка. Сортировка ",sorting_value_new)
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
# my_account = driver.find_element(By.ID,"menu-item-50").click()
# username = driver.find_element(By.ID,"username")
# username.send_keys("alex@sab.com")
# password = driver.find_element(By.ID, "password")
# password.send_keys("3250161718")
# login_button = driver.find_element(By.CSS_SELECTOR,".login>p:nth-child(3)>input:nth-child(3)")
# login_button.click()
# '''3. Нажмите на вкладку "Shop"'''
# shop = driver.find_element(By.ID,"menu-item-40").click()
# '''4. Откройте книгу "Android Quick Guide"'''
# book = driver.find_element(By.CSS_SELECTOR,".post-169 h3").click()
# '''5. Добавьте тест, что содержимое старой цены = "600.00"'''
# old_price = driver.find_element(By.CSS_SELECTOR,".price>del")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# '''6. Добавьте тест, что содержимое новой цены = "400.00"'''
# new_price = driver.find_element(By.CSS_SELECTOR,".price>ins")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# '''7. Добавьте явное ожидание и нажмите на обложку книги'''
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".images a")))
# img = driver.find_element(By.CSS_SELECTOR,".images a").click()
# '''8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик'''
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"pp_full_res")))
# close_img = driver.find_element(By.CLASS_NAME,"pp_close").click()
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
# add_to_basket = driver.find_element(By.CSS_SELECTOR,"li:nth-child(4)>.add_to_cart_button").click()
# '''4. Добавьте тест, что возле корзины (вверху справа) количество товаров = "1 Item", а стоимость = "180.00"'''
# time.sleep(1)
# item = driver.find_element(By.CLASS_NAME,"cartcontents")
# item_text = item.text
# assert item_text == "1 Item"
# print("В корзине количество товаров:",item_text)
#
# amount = driver.find_element(By.CSS_SELECTOR,".wpmenucart-contents>.amount")
# amount_text = amount.text
# assert amount_text == "₹180.00"
# print("Сумма в корзине:",amount_text)
# '''5. Перейдите в корзину'''
# basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
# '''6. Используйте явное ожидание, проверьте что в Subtotal отобразится стоимость'''
# subtotal = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".cart-subtotal>td>span")))
# subtotal_text = subtotal.text
# print("Отобразилось цена товара:",subtotal_text)
# '''7. Используйте явное ожидание, проверьте что в Total отобразится стоимость'''
# total = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".order-total>td>strong>.woocommerce-Price-amount")))
# total_text = total.text
# print("Итоговая цена отобразилась:",total_text)
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
# driver.execute_script("window.scrollBy(0,300);")
# book_one = driver.find_element(By.CSS_SELECTOR,"li:nth-child(4)>.add_to_cart_button").click()
# time.sleep(1)
# book_two = driver.find_element(By.CSS_SELECTOR,"li:nth-child(5)>.add_to_cart_button").click()
# time.sleep(1)
# '''4. Перейдите в корзину'''
# basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
# '''5. Удалите первую книгу'''
# time.sleep(1)
# delete_book = driver.find_element(By.CSS_SELECTOR,".cart_item:nth-child(1)>.product-remove>a").click()
# '''6. Нажмите на Undo (отмена удаления)'''
# undo = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".woocommerce-message>a")))
# undo.click()
# '''7. В Quantity увеличьте количество товара до 3 шт для "JS Data Structures and Algorithm"'''
# input_text = driver.find_element(By.CSS_SELECTOR,".cart_item:nth-child(1)>.product-quantity>.quantity>input")
# input_text.clear()
# input_text.send_keys(3)
# '''8. Нажмите на кнопку "UPDATE BASKET"'''
# update_basket = driver.find_element(By.CSS_SELECTOR,".actions>.button").click()
# '''9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3'''
# WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".cart_item:nth-child(1)>.product-quantity>.quantity>input")))
# js_data = driver.find_element(By.CSS_SELECTOR,".cart_item:nth-child(1)>.product-quantity>.quantity>input")
# js_value = js_data.get_attribute("value")
# assert js_value == "3"
# '''10. Нажмите на кнопку "APPLY COUPON"'''
# time.sleep(1)
# apply_coupon = driver.find_element(By.CSS_SELECTOR,".actions>div>.button").click()
# '''11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."'''
# error = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".woocommerce-error>li"),"Please enter a coupon code."))
# print("Возникло сообщение: Please enter a coupon code.",error)
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
# driver.execute_script("window.scrollBy(0,300);")
# '''3. Добавьте в корзину книгу "HTML5 WebApp Development"'''
# book = driver.find_element(By.CSS_SELECTOR,"li:nth-child(4)>.add_to_cart_button").click()
# time.sleep(2)
# '''4. Перейдите в корзину'''
# basket = driver.find_element(By.CLASS_NAME,"wpmenucart-contents").click()
# '''5. Нажмите "PROCEED TO CHECKOUT"'''
# proceed_to_checkout = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".wc-proceed-to-checkout>a")))
# proceed_to_checkout.click()
# '''6. Заполните все обязательные поля'''
# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"billing_first_name")))
# first_name = driver.find_element(By.ID,"billing_first_name")
# first_name.send_keys("Alex")
# last_name = driver.find_element(By.ID,"billing_last_name")
# last_name.send_keys("Sab")
# mail = driver.find_element(By.ID,"billing_email")
# mail.send_keys("alex@sab.com")
# phone = driver.find_element(By.ID,"billing_phone")
# phone.send_keys("1234567890")
# country = driver.find_element(By.ID,"s2id_billing_country").click()
# country_search = driver.find_element(By.ID,"s2id_autogen1_search")
# country_search.send_keys("Russia")
# country_text = driver.find_element(By.CSS_SELECTOR,"#select2-results-1>li>div>span").click()
# address = driver.find_element(By.CSS_SELECTOR,"#billing_address_1_field>#billing_address_1")
# address.send_keys("Main")
# city = driver.find_element(By.CSS_SELECTOR,"#billing_city_field>#billing_city")
# city.send_keys("Lukhovitsy")
# state = driver.find_element(By.CSS_SELECTOR,"#billing_state_field>#billing_state")
# state.send_keys("Moscow obl.")
# postcode = driver.find_element(By.CSS_SELECTOR,"#billing_postcode_field>#billing_postcode")
# postcode.send_keys("140500")
# '''7. Выберите способ оплаты "Check Payments"'''
# driver.execute_script("window.scrollBy(0,600);")
# time.sleep(2)
# check_payments = driver.find_element(By.ID,"payment_method_cheque").click()
# '''8. Нажмите PLACE ORDER'''
# place_order = driver.find_element(By.ID,"place_order").click()
# '''9. Используйте явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."'''
# thank_you = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-content>.woocommerce>.woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
# print("Отображается надпись: 'Thank you. Your order has been received.'",thank_you)
# '''10. Используйте явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"'''
# payment_method = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".page-content>.woocommerce>ul>li:nth-child(4)>strong"),"Check Payments"))
# print("Отображается метод оплаты: 'Check Payments'",payment_method)
# time.sleep(3)
# driver.quit()