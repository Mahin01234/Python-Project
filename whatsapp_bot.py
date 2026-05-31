"""
WhatsApp Bot using Selenium (English)
WARNING: Educational purpose only. Automation violates WhatsApp's Terms of Service.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------- 1. Automatic ChromeDriver setup (Selenium 4.6+ handles it) ----------
driver = webdriver.Chrome()  # No need for manual driver or webdriver-manager

# ---------- 2. Open WhatsApp Web ----------
driver.get('https://web.whatsapp.com/')
print("WhatsApp Web opened. Please scan the QR code (30 seconds given)...")
time.sleep(30)  # Wait for QR scan

# ---------- 3. Find a contact/group and send a message ----------
try:
    # Locate the search box
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
    )
    # Replace with the exact contact/group name as saved in WhatsApp
    contact_name = "Your Contact Name"
    search_box.send_keys(contact_name)
    time.sleep(2)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Locate the message input box
    message_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
    )
    message_text = "Hello! This message was sent automatically by a Python bot."
    message_box.send_keys(message_text)
    message_box.send_keys(Keys.ENTER)
    print("Message sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Make sure the contact name is correct and WhatsApp Web is loaded.")

# ---------- 4. Keep browser open for a few seconds (optional) ----------
print("Browser will close in 10 seconds...")
time.sleep(10)
driver.quit()

