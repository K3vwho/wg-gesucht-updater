import yaml
from selenium import webdriver
import time

loops = 1000
hour = 60*60*3

# load config
with open("user_data.yaml", "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


for i in range(loops):
    # Create a web driver object
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://www.wg-gesucht.de/mein-wg-gesucht.html")

    # Find the login form and enter your login credentials
    username_field = driver.find_element("name", "login_email_username")
    password_field = driver.find_element("name", "login_password")
    username_field.send_keys(conf['username'])
    password_field.send_keys(conf['password'])

    # Submit the login form

    # <input id = "login_submit" class = "btn btn-block wgg_orange" type = "submit" value = "Login" tabindex = "29" onclick = "ga('send', 'event', 'Buttons', 'login', 'Login-Popup');" >
    login_button = driver.find_element("id", "login_submit")
    # login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()

    # Navigate to the page for managing your ads
    time.sleep(2)
    # Find the ad that you want to update and click the edit button
    driver.get(
        "https://www.wg-gesucht.de/angebot-bearbeiten.html?action=update_offer&offer_id=" + str(conf['ad_id']))

    # Accept cookies
    cookies_button = driver.find_element(
        "id", "cmpbntyestxt")
    cookies_button.click()
    time.sleep(10)

    # Make the desired changes to your ad and save them
    # (code for making changes goes here)
    save_button = driver.find_element(
        "id", "update_offer")
    save_button.click()

    # Close the web driver to end the session
    driver.quit()

    time.sleep(hour)
