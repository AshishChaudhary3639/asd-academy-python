from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Setup the Chrome browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and type query
search_box = driver.find_element("name", "q")
search_box.send_keys("JavaScript Tutorial")
search_box.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()


# titles = driver.find_elements(By.TAG_NAME, "h3")
# top_titles = [title.text for title in titles if title.text.strip() != ""][:5]

# # Step 6: Save titles to a text file
# with open("top_google_results.txt", "w") as f:
#     for i, title in enumerate(top_titles, 1):
#         f.write(f"{i}. {title}\n")

# print("Top 5 search result titles saved to top_google_results.txt")

# # Step 7: Close browser
# driver.quit()