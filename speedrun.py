from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from bs4 import BeautifulSoup

def open_google_window():
    # URL for random game on speedrun.com
    url = "https://www.speedrun.com/randomgame"

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')

    # Open Chrome browser
    with webdriver.Chrome(options=chrome_options) as driver:
        # Navigate to the specified URL
        driver.get(url)

        try:
            # Wait for and click the cookie consent button
            cookie_consent_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'ACCETTO') or contains(., 'Accetto')]"))
            )
            cookie_consent_button.click()
            time.sleep(1)

            # Get the URL after accepting cookies
            current_url = driver.current_url

            # Extract only the part after "https://www.speedrun.com/"
            name = current_url.replace("https://www.speedrun.com/", "")

            # Open the new link
            new_link = f"https://www.speedrun.com/{name}/runs/new?h=Any%"
            driver.get(new_link)
            time.sleep(1)

            # Extract the value of the "emulator" attribute from the source code
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            script_content = soup.find('script', {'id': '__NEXT_DATA__'}).text

            # Find the part of the text that contains "emulator" and get the value
            emulator_value = script_content.split('"emulator":', 1)[1].split(',', 1)[0].strip()

            # Convert the value to a boolean
            Emulator = emulator_value == "1"

            # Find the value of "totalPlayers"
            total_players_value = int(script_content.split('"totalPlayers":', 1)[1].split(',', 1)[0])

            # Create the string with the desired format
            data_string = f"{total_players_value} {name} {current_url}\n"

            # Determine the file name based on Emulator
            file_name = "emu.txt" if Emulator else "no_emu.txt"

            # Check if the file exists, create it if not
            if not os.path.exists(file_name):
                open(file_name, 'w').close()

            # Read the content of the file
            with open(file_name, "a+") as file:
                file.seek(0)
                lines = file.readlines()

            # Add the new string to the list only if it's not already present
            if data_string not in lines:
                lines.append(data_string)

            # Remove duplicates while preserving the order
            unique_lines = list(dict.fromkeys(lines))

            # Write the content to the file
            with open(file_name, "w") as file:
                file.writelines(unique_lines)

        except Exception as e:
            print(f"An exception occurred: {e}")

if __name__ == "__main__":
    # Run the function once
    open_google_window()

if __name__ == "__main__":
#HERE YOU CAN CHANCE THE NUMBER OF TIME THE SCRIPT RUN
    cycles = 1

    for i in range(cycles-1):
        open_google_window()
        print(i)
