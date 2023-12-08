from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import platform
import sys


def setup_driver():
    chrome_options = Options()
    if platform.system() in ['Windows', 'Darwin']:
        chrome_options.add_experimental_option('detach', True)
    elif platform.system() == 'Linux':
        chrome_options.add_argument('--headless')
    else:
        raise Exception("Unknown OS")
    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=chrome_options)

def find_element_and_click(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        return element
    except Exception as e:
        print(f"Error finding/clicking element: {e}")


def test_terminal(token):
    driver = setup_driver()
    url = f"http://127.0.0.1:8888/lab?token={token}"

    try:
        driver.get(url)
        print("Opened JupyterLab.")
        #used to return to base screen for next test
        main_window_handle = driver.current_window_handle 
        try:
            # Try to find the Launcher button
            launcher_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@data-command="launcher:create"]'))
            )
            launcher_button.click()
            print("Opened the Launcher.")
        except:
            print("Launcher button not found, skipping to Terminal.")

        # Click on the Terminal icon in the Launcher
        terminal_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@title="Start a new terminal session"]'))
        )
        terminal_icon.click()
        print("Opened Terminal.")
        terminal_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'jp-Terminal')]//textarea"))
        )
        print("Terminal is ready for input.")    
        # Find terminal input and execute a command
        terminal_input.send_keys('echo Hello World' + Keys.ENTER)
        print("Command sent to terminal.")   
        # Find terminal output and print it
        output_xpath = "//div[contains(@class, 'jp-Terminal-body')]"
        try:
            output = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, output_xpath))
            )
            print("Captured terminal output:" + output.text)
        except Exception as e:
            print(f"An error occurred during test: {e}")
        print("Terminal test successful.")
        # Close the terminal
        close_terminal_xpath = "//div[contains(@class, 'jp-icon-hover') and contains(@class, 'lm-TabBar-tabCloseIcon')]"
        try:
            close_terminal_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, close_terminal_xpath))
            )
            close_terminal_button.click()
            print("Closed Terminal.")
        except Exception as e:
            print("Error closing terminal: ", e)
    except Exception as e:
        print(f"An error occurred during test: {e}")
    finally:
        driver.switch_to.window(main_window_handle)
        driver.refresh()
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python script.py <token>")
    else:
        test_terminal(sys.argv[1])