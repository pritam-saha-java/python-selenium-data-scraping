from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# URL template to iterate through pages
url_template = "https://www.skokka.in/call-girls/kolkata/?p={}"

# List to store all the links
all_links = []

# Iterate through the first 30 pages
for page in range(1, 5):
    # Open the URL for the current page
    driver.get(url_template.format(page))
    time.sleep(2)  # Wait for the page to load
    
    # Find all the element cards
    cards = driver.find_elements(By.CLASS_NAME, "item-card")
    
    # Extract and store the links from each card
    for card in cards:
        link = card.find_element(By.CSS_SELECTOR, ".listing-title.item-title a").get_attribute("href")
        all_links.append(link)
    
    print(f"Collected links from page {page}")


#Start visting each page
for link in all_links:
    print(link)
    driver.get(link)
    time.sleep(2)




# Close the WebDriver
driver.quit()

