from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Узнаем значение x
    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")
    print(x_value)
    
    # Подставим x в формулу
    y = calc(x_value)
    print(y)
    
    # Заполняем форму
    browser.find_element_by_id("answer").send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_class_name("btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
