from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the URL for the website
url = 'https://www.igihe.com/'
driver.get(url)

# Set up WebDriverWait with a 30-second timeout
wait = WebDriverWait(driver, 3000)

try:
    # Example: Search for articles or content related to "Burundi"
    # Note: Adjust the selector based on the actual HTML structure of the site

    # Wait for the main content to load
    main_content = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'main'))
    )

    # Find all article titles and contents
    articles = driver.find_elements(By.CSS_SELECTOR, 'article')  # Adjust selector if necessary

    for article in articles:
        title = article.find_element(By.CSS_SELECTOR, 'h2').text  # Adjust selector if necessary
        content = article.find_element(By.CSS_SELECTOR, 'p').text  # Adjust selector if necessary
        
        if 'Burundi' in title or 'Burundi' in content:
            print(f"Title: {title}")
            print(f"Content: {content}")
            print('-' * 80)

except TimeoutException:
    print("Timed out waiting for the page to load.")

finally:
    # Close the WebDriver
    driver.quit()
