from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define the URL of the 2048 game
url = "https://2048game.com/"

# Define the keys for moving in the game
keys = [Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT]

# Function to check if the game is over
def is_game_over(driver):
    try:
        # Find the game over message element
        game_over_message = driver.find_element("css selector", ".game-message.game-over")
        # Check if the game over message is displayed
        if game_over_message.is_displayed():
            return True
        else:
            return False
    except NoSuchElementException:
        return False

# Function to check if the game is won
def is_game_won(driver):
    try:
        game_won_message = driver.find_element("css selector", ".game-message.game-won")
        if game_won_message.is_displayed():
            return True
        else:
            return False
    except NoSuchElementException:
        return False

# Function to play the game
def play_game(driver):
    game_container = driver.find_element("class name", "container")
    actions = ActionChains(driver)
    actions.click(game_container)
    while not is_game_over(driver) and not is_game_won(driver):  # Check if game is over or won
        try:
            for key in keys:
                actions.send_keys(key)
                actions.perform()
                time.sleep(0.05)  
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Function to restart the game
def restart_game(driver):
    if is_game_won(driver):
        print("Game won!")
        return
    try:
        retry_button = driver.find_element("class name", "retry-button")
        if retry_button.is_displayed() and retry_button.is_enabled():
            retry_button.click()
            print("Clicked on retry button.")
        else:
            print("Retry button not clickable.")
    except NoSuchElementException:
        print("Retry button not found.")

# Main function
def main():
    # Start the browser
    driver = webdriver.Firefox()

    # Open the game
    driver.get(url)

    try:
        while True:
            # Play the game
            play_game(driver)

            # Game over, restart
            restart_game(driver)

    except KeyboardInterrupt:
        print("Script stopped by the user")
    finally:
        # Quit the browser session
        driver.quit()

if __name__ == "__main__":
    main()
