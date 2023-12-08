# UI (Testing RISE and Jupyter Lab)

In the Open Education (OPE) Platform, Jupyter Lab serves as the primary user interface. The integrity of our data processing, critical for both research and analytical workflows, depends on thorough testing. By testing Jupyter Lab, we ensure that all functionalities, including code cell execution, operate correctly and integrate seamlessly with various tools and libraries across different platforms.

Furthermore, OPE employs RISE to convert Jupyter notebooks into slideshows, enhancing interactive presentations. This feature is widely used in educational and professional settings for presenting complex data and analyses. Testing RISE is crucial to verify that it operates as intended and ensures that these presentations are reliable and effective in conveying information accurately.

Overall, comprehensive testing of Jupyter Lab and RISE is integral to maintaining the platform’s effectiveness and reliability.

## What Are We Testing?

1. **UI Testing:**

This workflow automates several processes: setting up an environment, running JupyterLab within a container, testing the RISE extension for JupyterLab, conducting UI tests, and performing visual comparisons of screenshots. The UI testing is critical, as it ensures that new updates do not break or undesirably alter existing functionalities.

2. **RISE Functionality Testing:**

- **Content Integrity and Visual Accuracy:** Verifying that the content's integrity is maintained during its conversion from a notebook to a slideshow and that visual outputs are accurately displayed. This is essential for ensuring that the presentations effectively and accurately convey information.
- **Interactive Feature Verification:** Since RISE supports interactive elements like real-time code execution, testing these features is crucial to ensure smooth functionality during presentations.
- **Compatibility and Stability:** RISE testing includes examining compatibility with different versions of Jupyter and assessing stability during operation. This step is vital to avoid potential issues arising from version mismatches or operational instabilities.
- **Error-Free Operation:** All elements within RISE must operate without errors to guarantee a practical and seamless learning experience.

## How Do We Test?

### GitHub Actions for UI tests

The GitHub Actions workflow, located in the [.github/workflows/Master_Container_Test.yml](https://github.com/YiqinZhang/OPE-Testing/blob/0cb63464bb8a8c3962c6d3f783e4d8d59f7fc0ef/.github/workflows/Master_Container_Test.yml#L249C2-L249C2), is designed to conduct UI tests in a JupyterLab environment. This workflow comprises the following steps:

1. **Setting up the Environment**: It runs on the latest Ubuntu version and begins by checking out the necessary code from a GitHub repository.

2. **Python and Browser Setup**: The workflow sets up Python 3.9 and installs Chromium, a web browser essential for running Selenium-based browser tests.

3. **Installing Python Dependencies**: It upgrades pip and installs required Python packages including Selenium and WebDriver Manager. The version of ChromeDriver, a key component for browser automation, is also verified.

4. **Run JupyterLab Inside Container**: The workflow pulls a beta version of the Docker image and runs the JupyterLab environment inside a container.

5. **Executing RISE Tests**: Executes RISE extension tests in JupyterLab. These tests involve both functional testing of the extension and capturing screenshots for UI verification.

   In the [Dockerfile](https://github.com/OPEFFORT/OPE-Testing/blob/5df4c895e9e30ee24b36a4b295a5a9613d7853d4/base/Dockerfile#L49C6-L49C6) ,`jupyterlab-rise` is installed directly using pip with the command `pip install jupyterlab_rise`.

6. **Visual Comparison Testing**: Finally, the workflow performs a screenshot comparison test to identify any discrepancies or changes in the UI, ensuring visual consistency and correct functionality.

![Screenshot 2023-12-04 at 01 10 53](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/2a61c1e4-2cb0-4bb0-8771-f771b5a97208)

#### Setup with GitHub Actions

To ensure all necessary libraries and dependencies are included, update `tests/requirement.txt` and `base/pip_pkgs`. For instance, add libraries like `selenium`, `webdriver_manager`, and `nbformat` to `base/pip_pkgs` and `tests/requirement.txt` . This ensures they are automatically installed in the Docker container during initialization.

<img width="655" alt="Screenshot 2023-11-29 at 19 28 54" src="https://github.com/YiqinZhang/OPE-Testing/assets/55336328/93b4c3a6-7a2f-4356-87b2-81009af3c4ff">

### Test RISE Functionality

We employ Selenium for the RISE test to simulate opening a Jupyter Notebook file. The test then captures screenshots to confirm the correct functioning of RISE and visually verify its performance within a Jupyter environment. The Python scripts are executable from the command line, requiring a JupyterLab token as an input parameter.

[rise_test.py](https://github.com/YiqinZhang/OPE-Testing/blob/container-base-ope/tests/rise_test.py): This Python script, sets up a Selenium WebDriver and then navigates to a JupyterLab instance, identified by a URL and token, and performs several actions: creating a new notebook, triggering the RISE extension to preview a slideshow, checking the functionality of the full-screen button in the RISE interface and taking screenshots.

[rise_test_slide.py](https://github.com/YiqinZhang/OPE-Testing/blob/container-base-ope/tests/rise_test_slide.py): This Python script programmatically creates a new Jupyter notebook (`example_notebook.ipynb`) with predefined slides. Each slide, crafted with markdown cells, includes specific content, images, and metadata. The code proceeds to open this notebook in JupyterLab, activate the RISE presentation mode, and take screenshots at various stages (main page, new notebook page, and RISE preview).

[test_terminal.py](https://github.com/YiqinZhang/OPE-Testing/blob/container-base-ope/tests/test_terminal.py): The script automates the testing of a terminal session within a JupyterLab environment using Selenium WebDriver.

Initially, it navigates to the Launcher and locates the Terminal icon. Upon clicking this icon, a new terminal session is opened. The script then proceeds to send a command, `echo Hello World`. Following this, it verifies the command's output by checking for the text 'Hello World' within the terminal’s output. The successful detection of this text serves as an assertion that the output is as expected, thereby confirming the terminal's functionality in JupyterLab environment.

[screenshots_diff.py](https://github.com/YiqinZhang/OPE-Testing/blob/container-base-ope/tests/screenshots_diff.py): The code employs the Python Imaging Library (PIL) for image processing and comparison. It defines two functions: `is_image_blank` to check if an image is blank and `rms_diff`, a function that calculates the root mean square error between two images. This error quantifies the extent of their differences and minimizes false positives during image comparisons.
If both images are not blank, it resizes the test image to match the base image (if their sizes differ) and then calculates the RMS error between them. Based on a predefined threshold (in this case, an RMS error greater than 10), the script determines if the images are identical, very similar, or different, and prints the appropriate message.

[run_rise_test.ipynb](https://github.com/YiqinZhang/OPE-Testing/blob/container-base-ope/tests/run_rise_test.ipynb): Provide an IPython Notebook (`.ipynb`) to facilitate interactive code execution and control.

#### Test with locally

To effectively test RISE functionality within Jupyter Lab, our process involves the following steps:

1. **Retrieve Jupyter Lab Token:** First, obtain a `token` from a Jupyter Lab instance.
   ![Screenshot 2023-11-27 at 14 56 42](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/9c699718-6393-4596-b13a-a8bef8cd086c)

2. **Execute RISE Test Script:** Run the command `python rise-test.py {token}`. This command initiates the opening of the Jupyter Lab instance and captures a screenshot of the launcher page.

   ![Screenshot 2023-11-27 at 15 11 20](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/3a9a9cb2-4f89-4b08-8fe5-94be837e03ad)

   If you are using the Jupyter notebook version, named `run_rise_test.ipynb`, simply replace `{token}` with your specific token and then proceed to execute the cells within the notebook.

   ![Screenshot 2023-11-27 at 15 23 04](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/577249e3-7c97-4344-8e86-0a7352e6d619)

3. **Create and Capture Notebook File:** Following the simulated click on the Notebook launch icon, a new Jupyter Notebook file is automatically created.. We then take a screenshot for comparison purposes.
   ![new_nb_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/78c9470a-eff9-4ec0-b3ab-94eaeaa7afbf)

4. **Activate and Document RISE Function:** The test proceeds to locate and double-click the RISE icon, triggering the RISE function. A screenshot is taken at this stage to document the functionality.
   ![rise_screenshot](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/26f8a25b-6574-4ba3-9ddf-e341539e0c0a)

5. **Test Fullscreen Feature:** The process includes searching for and activating the fullscreen button to display the slideshow in fullscreen mode.

6. **Screenshots Comparasion:**  
   Successfully completing these steps and comparing the three screenshots without any discrepancies confirms that RISE is functioning effectively within the Jupyter Lab environment.

   ![Screenshot 2023-11-27 at 16 43 12](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/d703435e-541e-469a-b75c-45de0109f806)

   If the screenshots are either blank or deviate from the predefined images, the system will display error messages as follows:

   ![Screenshot 2023-12-04 at 01 13 56](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/1cfcb695-1e43-4fd6-8418-5c14bc05a078)

7. **Enhanced RISE Testing with Sample Slides:**

   Generate sample slides containing text, images, and notes, separated by dividing lines through scripts. Utilize Selenium to automate the opening of these slides and their conversion into a slideshow format. Then, capture screenshots of the slideshow for comparison against predefined slide templates to assess the visual effects.

   ![new_nb_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/fbcb0e1f-7386-4a28-a845-3ed87bac0b31)
   _Sample notebook slides_

   ![rise_screenshot 8](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/112d0594-2c81-4b01-ac23-f2e48f6a5bf6)
   _Sample slideshow_

   ![Screenshot 2023-11-27 at 14 25 47](https://github.com/YiqinZhang/OPE-Testing/assets/55336328/224279d2-584f-425f-971b-cf619fdf6595)
