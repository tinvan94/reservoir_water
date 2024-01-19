# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_reservoir_water():

    browser = webdriver.Chrome()
    browser.get('https://thuydienvietnam.vn/index.html#')
    c_input = browser.find_element(By.ID, "main-top-search-input")
    c_input.clear()
    c_input.send_keys("Kon Tum")
    c_input.send_keys(Keys.ENTER)
    c_input.click()
    rain_element = browser.find_element(By.ID, "qt-mua")

    print(f'Mua: {rain_element.text}')
    water_element = browser.find_element(By.ID, "qt-mucnuoc")
    print(f'Muc nuoc: {water_element.text}')
    dt_element = browser.find_element(By.ID, "qt-dungtich")
    print(f'Dung tich: {dt_element.text}')
    qd_element = browser.find_element(By.ID, "qt-qden")
    print(f'Q den: {qd_element.text}')
    qx_element = browser.find_element(By.ID, "qt-qxa")
    print(f'Ho dang xa: {qx_element.text}')
    mns_element = browser.find_element(By.ID, "qt-mucnuocsong")
    print(f'Muc nuoc song: {mns_element.text}')

    browser.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_reservoir_water()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
