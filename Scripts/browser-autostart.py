# pip install selenium or else: Import "selenium" could not be resolved
from selenium import webdriver

# List of URLs you want to open
urls_to_open = [
    "https://calendar.google.com/calendar/u",
    "https://outlook.live.com/mail/0/",
    "https://github.com/JMCD0",
    "https://chat.openai.com/c",
    # Add more URLs here
]

# Configure Firefox options
firefox_options = webdriver.FirefoxOptions()
# Set preferences to potentially pin tabs (for Firefox)
firefox_options.set_preference("browser.link.open_newwindow.restriction", 0)
firefox_options.set_preference("browser.link.open_newwindow", 3)

# Create a Firefox webdriver by specifying the path to geckodriver
# Replace '/path/to/geckodriver' with the actual path to your geckodriver executable
driver = webdriver.Firefox(executable_path='/path/to/geckodriver', options=firefox_options)
# Open each URL in a new tab
for url in urls_to_open:
    driver.execute_script(f"window.open('{url}', '_blank');")
# Close the first empty tab (opened by default)
driver.switch_to.window(driver.window_handles[0])
driver.close()
# Keep the remaining tabs open
driver.switch_to.window(driver.window_handles[-1])
# Optionally, maximize the window
driver.maximize_window()

# Close the driver when done
# driver.quit()
