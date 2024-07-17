from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import re

# Initialize the WebDriver
driver = webdriver.Chrome()

# URL template for pagination
url_template = "https://www.skokka.in/call-girls/?p={}"

# List to store all links
all_links = []
phone_numbers = []

# Loop through pages
for page in range(1, 3):
    driver.get(url_template.format(page))
    time.sleep(1)
    
    cards = driver.find_elements(By.CLASS_NAME, "item-card")
    
    for card in cards:
        link = card.find_element(By.CSS_SELECTOR, ".listing-title.item-title a").get_attribute("href")
        all_links.append(link)

# List to store data
data = []

# Visit each link and extract data
for link in all_links:
    driver.get(link)
    time.sleep(1)

    # Get the title of the page
    title = driver.title

    location_element = driver.find_element(By.CSS_SELECTOR, ".detail.tagcard .badge-pill.notranslate")
    location = location_element.text.split(" / ")[0]

    # Extract phone number using regular expression
    match = re.search(r'\d{11}', title)

    if match:
        phone_numbers.append((location, match.group()))
        print(f"Extracted phone number: {match.group()}")
        print(f"Extracted location: {location}")
    else:
        print("No phone number found in the title")

# Save data to CSV
csv_file = "extracted_data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Number"])
    writer.writerows(phone_numbers)

# Close the WebDriver
driver.quit()

print(f"Data successfully saved to {csv_file}")
