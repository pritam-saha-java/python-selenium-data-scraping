from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open the target URL
driver.get("https://www.skokka.in/call-girls/kolkata/")
time.sleep(2)  # Let the page load completely

# Find all the item cards
item_cards = driver.find_elements(By.CLASS_NAME, 'item-card')

# Extract and print the links from each card
for card in item_cards:
    try:
        link_element = card.find_element(By.CSS_SELECTOR, 'a.line-clamp')
        link = link_element.get_attribute('href')
        print(link)
    except:
        continue  # If there's any issue finding the link, skip to the next card

# Close the WebDriver
driver.close()
