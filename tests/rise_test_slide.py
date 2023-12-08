import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import sys
import os
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell
import subprocess


def setup_driver():
    chrome_options = Options()
    if platform.system() in ['Windows', 'Darwin']:
        chrome_options.add_experimental_option('detach', True)
    elif platform.system() == 'Linux':
        chrome_options.add_argument('--headless')
    else:
        raise Exception("Unknown OS")
    return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()), options=chrome_options)

def create_jupyter_notebook_from_github(github_url, local_file_name):
    try:
        response = requests.get(github_url)
        response.raise_for_status()  # Raise an error for bad status codes
        notebook_content = response.json()
        with open(local_file_name, 'w', encoding='utf-8') as notebook_file:
            json.dump(notebook_content, notebook_file)
        print(f"Notebook created: {local_file_name}")
    except requests.RequestException as e:
        print(f"Failed to download the notebook: {e}")

def download_image(image_url, local_img_path):
    response = requests.get(image_url, stream=True)

    if response.status_code == 200:
        os.makedirs(os.path.dirname(local_img_path), exist_ok=True)
        with open(local_img_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print(f"Image downloaded successfully: {local_img_path}")
    else:
        print(f"Failed to download the image: {image_url}")

def open_jupyter_notebook(url, notebook_name, driver):
    try:
        driver.get(url)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".jp-DirListing")))
        notebook = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, f"//span[text()='{notebook_name}']"))
        )
        notebook.click()  # JavaScript click for double-click action
        driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('dblclick', {bubbles: true, cancelable: true, view: window}));", notebook)
        print(f"File '{notebook_name}' opened successfully.")
    except Exception as e:
        print(f"Error: {e}")

def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(filename)
        print(f"Saved screenshot: {filename}")
    except Exception as e:
        print(f"Error taking screenshot: {e}")

def find_element_and_click(driver, xpath):
    try:
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        element.click()
        return element
    except Exception as e:
        print(f"Error finding/clicking element: {e}")
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

def test_rise(token, notebook_github_url, local_notebook_name):
    driver = setup_driver()
    create_jupyter_notebook_from_github(notebook_github_url, local_notebook_name)
    open_jupyter_notebook(f"http://127.0.0.1:8888/lab?token={token}", local_notebook_name, driver)

    try:
        WebDriverWait(driver, 45)
        take_screenshot(driver, 'main_screenshot.png')

        # Correct the XPath and check if the "Launcher" tab is present
        try:
            launcher_element = driver.find_element(By.XPATH, "//div[contains(@class, 'lm-TabBar-tabLabel') and contains(@class, 'p-TabBar-tabLabel') and text()='Launcher']")
            is_launcher_page = True
        except NoSuchElementException:
            is_launcher_page = False 
        
        if is_launcher_page:
            print("On the Launcher page")
            find_element_and_click(driver, '//div[@data-category="Notebook"]')
        else:
            print("Not on the Launcher page, trying to open the notebook directly")
            notebook = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(), '{local_notebook_name}')]"))
            )
            notebook.click()      
                 
        take_screenshot(driver, 'new_nb_screenshot.png')

        find_element_and_click(driver, '//button[@data-command="RISE:preview"]')        
        take_screenshot(driver, 'rise_screenshot.png')

        fullscreen_button = find_element_and_click(driver, ".//button[@title='Open the slideshow in full screen']")
        is_fullscreen = driver.execute_script("return document.fullscreenElement !== null")
        print("Fullscreen button is functioning")

    finally:
        # Clean up  
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        WebDriverWait(driver, 30)      
        driver.quit()

def test_rise_slide(token):
    driver = setup_driver()
    url = f"http://127.0.0.1:8888/lab?token={token}"
    try:
        driver.get(url)
        WebDriverWait(driver, 45)
        take_screenshot(driver, 'main_screenshot.png')
        # Check if on the Launcher page
        try:
            driver.find_element(By.XPATH, "//div[contains(@class, 'lm-TabBar-tabLabel') and contains(@class, 'p-TabBar-tabLabel') and text()='Launcher']")
            print("On the Launcher page")
            find_element_and_click(driver, '//div[@data-category="Notebook"]')
        except NoSuchElementException:
            print("Not on the Launcher page")
        # Create a new notebook object
        nb = new_notebook()
        # Add cells to the notebook
        nb['cells'] = cells
        # Write the notebook to a file
        with open('example_notebook.ipynb', 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("Notebook created successfully.")
        take_screenshot(driver, 'new_nb_screenshot.png')

        find_element_and_click(driver, '//button[@data-command="RISE:preview"]')
        take_screenshot(driver, 'rise_screenshot.png')

        toolbar = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@class='lm-Widget jp-Toolbar' and @role='navigation']")))
        if toolbar:
            fullscreen_button = toolbar.find_element(By.XPATH, ".//button[@title='Open the slideshow in full screen']")
            fullscreen_button.click()
            is_fullscreen = driver.execute_script("return document.fullscreenElement !== null")
            print("Fullscreen button is functioning: ", is_fullscreen)
        else:
            print("Toolbar not found")
        print("RISE Extension is working!")
    except Exception as e:
        print(f"An error occurred during test: {e}")
    finally:
        # Clean up
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        WebDriverWait(driver, 90)
        driver.quit()


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Usage: python script.py <token>")
    else:
        notebook_github_url = "https://raw.githubusercontent.com/OPEFFORT/ope-project/main/content/test_book/02_slides_template/layout_example.ipynb"
        image_url = 'https://raw.githubusercontent.com/YiqinZhang/ope-project/e9ea65fa2317b3c39d70984875ce2885dde8e599/content/images/sample-image.jpg'
        local_notebook_name = "downloaded_notebook.ipynb"
        local_img_path='../images/sample-image.jpg'
        # test_rise(sys.argv[1], notebook_github_url, local_notebook_name)
        # Define the cells with their content and metadata
        cells = [
            new_markdown_cell("# Example Slidedeck", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("<hr>", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("**0) Blank**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("**BODY**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("We will try to illustrate single-column slides like this one.", metadata={"slideshow": {"slide_type": "slide"}}),
            new_markdown_cell("<hr>", metadata={"slideshow": {"slide_type": "skip"}}),  
            new_markdown_cell(source="**1) Image Only**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell(source="**BODY**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell(source='<img src="../images/sample-image.jpg" width = "100%">', 
                            metadata={"slideshow": {"slide_type": "slide"}}),
            new_markdown_cell(source="**NOTE**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell(source="- Using % of slide to scale the image", 
                            metadata={"slideshow": {"slide_type": "notes"}}),
            new_markdown_cell(source="- - - ", metadata={"slideshow": {"slide_type": "skip"}}),  
            new_markdown_cell("**7)Title Slide**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("# Title", metadata={"slideshow": {"slide_type": "slide"}}),
            new_markdown_cell("**NOTE**", metadata={"slideshow": {"slide_type": "skip"}}),
            new_markdown_cell("- a Note that will display in the notes view", metadata={"slideshow": {"slide_type": "notes"}}),
            new_markdown_cell("This is the end of the document.", metadata={"slideshow": {"slide_type": "skip"}, "tags": ["remove-cell"]}),
        ]
        test_rise_slide(sys.argv[1])

        # subprocess.run(["python", "screenshots_diff.py"])