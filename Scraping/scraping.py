# scraping.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def get_taco_bell_items():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.tacobell.com/food/new")

    taco_bell_items = []

    # Locate image elements
    images = driver.find_elements(By.TAG_NAME, "img")

    # Extract URLs and titles of product images
    for img in images:
        if "product-image" in img.get_attribute("class"):
            url = img.get_attribute("src")
            title = img.get_attribute("alt")
        
            # Only add the item if it has both a URL and a title
            if url and title:
                taco_bell_items.append({"url": url, "title": title})

    driver.quit()
    return taco_bell_items
