from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import csv

driver = webdriver.Chrome()

url_template = "https://www.skokka.in/call-girls/kolkata/?p={}"

all_links = []
phone_numbers = []

for page in range(1, 31):

    driver.get(url_template.format(page))
    time.sleep(1)
    
    # Find all the element cards
    cards = driver.find_elements(By.CLASS_NAME, "item-card")
    
    # Extract and store the links from each card
    for card in cards:
        link = card.find_element(By.CSS_SELECTOR, ".listing-title.item-title a").get_attribute("href")
        all_links.append(link)
    
    print(f"Collected links from page {page}")

# Visit each link and extract the phone number from the title
for link in all_links:
    print(f"Visiting link: {link}")
    driver.get(link)
    time.sleep(1)
    
    # Get the title of the page
    title = driver.title
    print(f"Page title: {title}")
    
    # Extract phone number using regular expression
    match = re.search(r'\d{11}', title)
    if match:
        phone_numbers.append(("Kolkata", match.group()))
        print(f"Extracted phone number: {match.group()}")
    else:
        print("No phone number found in the title")

# Close the WebDriver
driver.quit()

# Save the data to a CSV file
csv_file = "kolkata_phone_numbers.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Location", "Number"])  # Write the header
    writer.writerows(phone_numbers)  # Write the data

print(f"Data has been written to {csv_file}")
