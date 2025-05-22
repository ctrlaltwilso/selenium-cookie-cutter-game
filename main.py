from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

website = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(website)

# ------------ Upgrades ------------------- #
store_path = '/html/body/div[4]/div[5]/div/div[1]/b/text()[2]'

# --------- Cookie Clicker & Stats ------------ #
click_cookie = driver.find_element(By.CSS_SELECTOR, value="#cookie")


def cookie_clicker():
    '''clicks cookie for 5 seconds'''
    timer = time.time() + 5
    while time.time() < timer:
        click_cookie.click()


def check_money():
    current_money = driver.find_element(By.CSS_SELECTOR, value="#money")
    money = int(current_money.text.replace(",", ""))
    return money


def check_upgrades():
    upgrades_cost = driver.find_elements(By.CSS_SELECTOR, value='#store b')
    store_list = [cost.text.split(" - ") for cost in upgrades_cost]
    available_upgrades = []
    money = check_money()
    for i in range(len(store_list) - 2, -1, -1):
        if int(store_list[i][-1].replace(",", "")) < money:
            available_upgrades.append(store_list[i])
            break
    return buy_upgrade(max(available_upgrades[0]))


def buy_upgrade(available_upgrade):
    driver.find_element(By.CSS_SELECTOR, value="#buy" + available_upgrade).click()


def cookies_per_second():
    cookie_per_second = driver.find_element(By.CSS_SELECTOR, value="#cps").text
    print(cookie_per_second)


game_is_on = time.time() + 300
while time.time() < game_is_on:
    cookie_clicker()
    check_upgrades()

# After 5 minutes, find cookies per second and record time
cookies_per_second()
driver.quit()
