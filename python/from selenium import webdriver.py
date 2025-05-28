from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (ChromeDriver is in the same folder as the script)
driver = webdriver.Chrome()

# Open the website
driver.get("https://bni-india.in/en-IN/advancedchaptersearch")

# Wait for the page to load
time.sleep(3)

# Close the cookie consent if present and wait until it is fully dismissed
try:
    cookie_accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='cc-btn cc-accept-all cc-btn-no-href']"))
    )
    cookie_accept.click()
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element((By.ID, "cookieconsent:desc"))
    )
except Exception as e:
    print("Cookie consent not found or already closed.")

# Select regions one by one using the select element (id="regionId")
region_select = Select(WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "regionId"))
))
regions = [option.get_attribute("value") for option in region_select.options if option.get_attribute("value")]

# Iterate over each region
for region in regions:
    try:
        region_select = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "regionId"))
        ))
        region_select.select_by_value(region)  # Select a region

        # Wait for the submit button to be clickable
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        submit_button.click()

        # Wait for the page to load the results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#chapterListTable tbody"))
        )

        # Get the rows with class 'odd' and 'even'
        tbody = driver.find_element(By.CSS_SELECTOR, "#chapterListTable tbody")
        rows = tbody.find_elements(By.CSS_SELECTOR, "tr.odd, tr.even")

        for row in rows:
            try:
                # Find and click the td element in the row
                td_element = row.find_element(By.TAG_NAME, "td")
                td_element.click()

                # Wait for the new page to load and find 'myTab'
                my_tab = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "myTab"))
                )

                # Find the first clickable 'nav-item' that is not 'active'
                nav_items = my_tab.find_elements(By.CLASS_NAME, "nav-item")
                for nav_item in nav_items:
                    if "active" not in nav_item.get_attribute("class"):
                        nav_item.click()
                        time.sleep(2)

                        # Wait for the new page to load the table
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.ID, "chapterListTable"))
                        )

                        # Find and process rows on the new page
                        chapter_table = driver.find_element(By.ID, "chapterListTable")
                        tbody_inner = chapter_table.find_element(By.TAG_NAME, "tbody")
                        inner_rows = tbody_inner.find_elements(By.CSS_SELECTOR, "tr.odd, tr.even")

                        for inner_row in inner_rows:
                            try:
                                inner_td = inner_row.find_element(By.TAG_NAME, "td")
                                inner_td.click()
                                time.sleep(2)

                                print("Clicked on inner row")

                                # Go back after processing the row
                                driver.back()
                                WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.ID, "chapterListTable"))
                                )
                                time.sleep(2)

                            except Exception as e:
                                print(f"Error clicking on inner row: {e}")
                                driver.back()
                                time.sleep(2)

                        driver.back()
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#chapterListTable tbody"))
                        )
                        time.sleep(2)
                        break

            except Exception as e:
                print(f"Error processing row: {e}")
                driver.back()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#chapterListTable tbody"))
                )
                time.sleep(2)

        driver.back()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "regionId"))
        )
        time.sleep(2)

    except Exception as e:
        print(f"Error processing region {region}: {e}")

# Close the browser after processing
driver.quit()