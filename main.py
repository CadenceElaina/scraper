import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize the WebDriver
driver = webdriver.Chrome()  # or use webdriver.Firefox()


def close_popups():
    try:
        # Add code to identify and close popups
        # Example for common popup close buttons; adjust the selectors as needed
        close_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btnCloseDark-DS-EntryPoint1-1'))  # Adjust the class name
        )
        close_button.click()
    except (NoSuchElementException, TimeoutException):
        # If popup not found or timeout occurs, continue
        pass


try:
    # Navigate to MSN Money
    driver.get("https://www.msn.com/en-us/money")

    # Wait for the search box to be present and visible
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "autoSuggest_commonv2-DS-EntryPoint1-1"))
    )

    # Optionally, wait a little extra time to ensure everything is loaded
    time.sleep(1)

    # Re-fetch the search box element to avoid stale reference issues
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "autoSuggest_commonv2-DS-EntryPoint1-1"))
    )

    # Enter the mutual fund symbol you want to search for
    fund_symbol = "AMCAP"
    search_box.send_keys(fund_symbol)
    search_box.send_keys(Keys.RETURN)

    # Close any popups that may appear


    # Wait for the search results page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))  # Wait for the body of the search results page to load
    )
    # If necessary, wait a little extra time for the page to finish loading
    time.sleep(2)
    close_popups()
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "autoSuggest_commonv2-DS-EntryPoint1-1"))
    )
    search_box.send_keys(Keys.RETURN)
    # Locate the span with the given class names
    span_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//span[contains(@class, 'displayNameWithBtn-DS-EntryPoint1-1') or contains(@class, 'displayNameWithBtnV2-DS-EntryPoint1-1')]"))
    )

    # Get the text from the span element
    span_text = span_element.text

    # Print the text
    print("Span Text:", span_text)

    # Locate the div with the given class names and get its text
    profile_div = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'profile_root-DS-EntryPoint1-1'))
    )

    # Get the text from the div
    profile_text = profile_div.text

    # Print the text from the div
    print("Profile Text:", profile_text)

    # Locate and click the link with class 'titleRow-DS-EntryPoint1-1'
    try:
        link_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'titleRow-DS-EntryPoint1-1'))
        )
        link_element.click()
    except (NoSuchElementException, TimeoutException) as e:
        print("Error clicking the link:", e)

    # Wait for the new page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

    # If necessary, wait a little extra time for the page to finish loading
    time.sleep(2)

    # Locate the div with class 'holdingsDetailSectorsCard-DS-EntryPoint1-1' and get its text
    holdings_div = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'holdingsDetailSectorsCard-DS-EntryPoint1-1'))
    )
    holdings_text = holdings_div.text
    print("Holdings Text:", holdings_text)

finally:
    # Close the browser
    driver.quit()
