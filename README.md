# Open Education Testing
## Project Description

This project focuses on enriching educational technology through the integration of Jupyter notebooks and Linux terminal activities. Intended for students, educators, and infrastructure developers.

**Team Members**: Yuxi Ge, Jonathan Mikalov, Riya Deokar, Ross Mikulskis, Yiqin Zhang

**Mentor**: Isaiah Stapleton

## 1.   Vision and Goals Of The Project:

Our project's vision is to create an innovative and immersive educational environment where the integration of Jupyter notebooks and Linux terminal interactions transcends traditional learning boundaries. We aim to cultivate a dynamic ecosystem where teachers and students can utilize technology to enhance the educational experience. Some of our visions and improvements consist of: 

Integration of Comprehensive Tests: We recognize the importance of the Master_Container_Test.yml, which consolidates various image, build, gdb, and UI tests into one. To improve this, we will continually update and expand the test suite to cover a broader range of scenarios and edge cases. This will ensure comprehensive validation of the OPE repository base container image.

Recognizing  limitations of outdated testing methods: We are committed to a modernization effort centered around automation. By embracing automated testing, continuous integration and deployment, and scalable frameworks, we aim to improve reliability, efficiency, and adaptability in our testing approach. This shift ensures that as the Open Education (OPE) project evolves, testing practices evolve with it, delivering a more robust and future-ready educational platform.

Continuous Monitoring: We will implement continuous monitoring of our container images to identify any discrepancies, vulnerabilities, or performance issues. This proactive approach will help us maintain the reliability and security of the OPE environment.

Custom Test Development: As part of our commitment to improving the OPE project, we will develop new custom tests tailored to the specific requirements and unique features of our containerized educational materials. These tests will be designed to address our project's needs. 

Training and Skill Development: We recognize the importance of equipping our team members with the skills and knowledge required to excel in testing and automation. We will invest in training, building, and skill development to enhance our team's capabilities.

## 2. Users/Personas Of The Project:

Open Education Testing offers a comprehensive Testing Integration suite designed to cover a broad range of scenarios and edge cases. This approach ensures the thorough validation of the base container image in the OPE repository. Embrace technological progress by utilizing automation, efficient continuous integration, deployment, and scalable frameworks. 

Users of this platform may include but are not limited to:

1. **Computer Science Educators: e.g. Professor Emily**
- *Background and Role*: Professor Emily is an experienced educator teaching computer systems courses. She relies on the Open Education platform to provide high-quality educational materials to her students.
- *Needs and Goals*: Emily needs a reliable and secure environment for her students to access Jupyter notebooks and interact with Linux terminals. She values easy customization options for tailoring materials to her course and offering a standardized container environment in which her students can code.

2. **Students: e.g. Alex**
- *Background and Role*: Alex is a computer science student using the Open Education platform to learn about computer systems.
- *Needs and Goals*: Alex expects a user-friendly interface, interactive Jupyter notebooks, and access to Linux terminals for practical learning.

2. **Teachers of Any Subject: e.g. Wayne**
- *Background and Role*: Wayne is a guitar music professor who has various musical excercises and resources for his class.
- *Needs and Goals*: Wayne wants to publish these materials online while being able to collaborate with his colleagues on content creation.

These user personas represent a diverse set of users who can benefit from the functionalities of the Open Education project. Each persona has unique needs, goals, and challenges that the project can address to enhance the educational experience. The OPE project allows them to all fulfill their needs and goals by providing a system through which to create content, collaborate, learn, and curate customized container learning environments.



## 3. Scope and Features of the Project: Testing OPE (Open Education Platform)

### Scope

1. **In-Scope:**
   - **Code Development for OPE Features**: Creating and improving features within the OPE platform.
   - **Setup-and-Build**: Building and pushing beta images to quay.io.
   - **Health-Check**: Verifying container uptime.
   - **Image-Version-Check**: Confirming correct image and tag.
   - **JupyterNB-Test**: Checking package imports in Jupyter Notebook.
   - **Package-Version-Test**: Version consistency of installed packages.
   - **Checksum**: Validation of container image checksum.
   - **Size-and-Time-Display**: Metrics for build time and image size.
   - **UI-Test**: Functionality and layout checks using Selenium.
   - **GDB-Test**: GDB functionality validation.
   - **Approval**: Authorization process.
   - **Publish**: Publishing the stable image to OPE's quay.io repo.

2. **Out-of-Scope:**
   - Infrastructure setup for Mass Open Cloud.
   - Content creation for educational material.
   - Manual quality assurance tests.

### Features

1. **Comprehensive Testing**: The Master_Container_Test.yml serves as the core feature that includes all relevant image, build, gdb, and UI tests.
   
2. **Automation and Build**: Automating image build, versioning, and pushing to the registry.

3. **Health Metrics**: Periodic health check-ups to ensure container functionality.

4. **Package and Version Consistency**: Automated checks for software versions against a predefined list (versions.txt).

5. **UI Validation**: Selenium-based tests for interface and visual elements in Jupyter Notebook.

6. **GDB Functionality**: Automated bash scripts for validating GDB functionality 100 times.

7. **Security Checks**: Ensuring checksum integrity of the container image.

8. **Metrics Display**: Real-time display of build time and size.

9. **Approval Mechanism**: A feature to send and receive authorization approvals.

10. **Publication**: Publishing the approved, stable image to OPE’s quay.io repository.

    

## 4. Solution Concept
**Architecture**
![OPE testing](https://github.com/EC528-Fall-2023/Open-Education-Testing/assets/91744036/cddb0b81-1cd1-4eed-b9cb-b086e53b49f9)

![](images/A2.png)



Throughout the duration of this project, we will be contributing directly to open education tests. These tests directly involve the functionality of jupyter notebooks and other supported platforms. They do not involve server-side support, such as containerized support and remote access.


1. **Test Notebook Template**
   - We are developing a standaridzed template for Jupyter notebooks involving a variety of tests 
   - Tests include UID/GID checks, write permissions, accessible storage, and networking.
   - This template will allow users to run quick diagnotistics to ensure system compatability 

2. **OPE Tool**

   - The OPE tool is central to the OPE project for providing an easy-to-work-with interface for writing and cloning Jupyter Notebook textbooks.
   - The test notebook template will be integrated within the OPE Tool, which can be used for generating reports documenting compatability failures
   - We will be adding a new command to OPE Tool to allow users to create test reports on demand


3. **Environment Specific Tests**
   - We're enhancing our testing approach by crafting environment-specific testing scripts
   - Tailoring the solution makes our tests more robust, addressing critical aspects like user ID generation and unique user limits within the NERF environment.
   - These scripts ensure comprehensive validation, adaptability to evolving conditions, and resilience in our educational platform, reinforcing our commitment to meeting project-specific requirements effectively.
 

## 5. Acceptance criteria

Minimum acceptance criteria: 
   - Develop a Test Notebook Template. The tests ensure that the base container only passes the build process if all of the packages are compatible and fully functioning, the address randomization works (need to clarify more on this), and all content functions as intended.
   - Successfully deploy base container to NERC or some test cluster.
   - Implement all of the ope commands listed in the OPE-Testing *tools* branch as described by Professor Appavoo to allow for a more user-friendly framework for content creation. Also, add necessary documentation for these commands.

Stretch goals: 
   - Add tool for translating textbooks written in LaTeX into the Jupyter Notebook format so that they can be hosted online and provide additional functionality by incorporating the suite of Jupyter tools.

     

## 6.  Release Planning:

Release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher level details for the first iteration is expected.

1. **Build OPE Base Image and Container Locally and Verify Testing Procedures (8 tests)**
   - Construct the OPE base image both locally. Ensure the image is functional and can run seamlessly.
   - Familiarize with the Makefile and Dockerfile and Gain a comprehensive understanding of their structures and functionalities to aid in future modifications.
   - Refactor the Makefile and Dockerfile to ensure system independence and compatibility across various Instruction Set Architectures, specifically arm64 and x86.
   - Navigate to the workflow file located at `OPE-Testing/.github/workflows/Master_Container_Test.yaml`. Run the predefined tests and assess their performance, ensuring all tests function as expected.
2. **Create test notebook template for building/running OPE**
   - Write address randomization tests using gdb.
   - Test home directory, read/write permissions
   - Check pip install and configuration files
   - Perform UID / GID checks to ensure permission compatability
3. **Revise OPE Tests with Exception Handling and Standardize Tests**
   - Enhance existing tests with robust exception handling to provide developers with clear indications of build issues or failures.
   - Merge tests into one single notebook, standardizing under a common framework to properly report errors
4. **Add functionality for ope commands and revise GitHub Actions**
   - Verify and test each GitHub action found in .github/workflows to ensure proper build compatability tests
   - Create functionality for missing OPE commands in tools branch, including but not limited to: `ope new part`, `ope new section`, `repo_add`
   - Create autograding framework to incorporate OPE into gradescope to allow for exporting testing onto OPE container to circumvent any potential kernel incompatibilities between the gradescope kernel and the OPE course assignments.
   - Fix github actions workflow for conainer build to work. Also, identify and fix any broken tests and make tests more robust.
5. **Write code to translate LaTeX projects into OPE Jupyter NB framework**
   - At least start the framework for this. A professor who already wrote their textbook in LaTeX wants an easy migration to this platform to reap all the benefits of the OPE features and            hosting it online, but the barrier to entry is all the work of rewriting.
   - Write this code with pandoc and bash, maybe python too to parse sections of LaTeX and use *ope tools* developed in sprint 4 to make this process easier.
** **

Here are a couple repos that are important to our project, forked from the OPE repos:
- [https://github.com/rkulskis/ope-quay](https://github.com/rkulskis/ope-quay) (fork of [https://github.com/OPEFFORT/OPE-Testing](https://github.com/OPEFFORT/OPE-Testing)) 
for working on ope CLI tool and image build process tests
- [https://github.com/rkulskis/content-examples](https://github.com/rkulskis/content-examples) (fork of [https://github.com/OPEFFORT/content-examples](https://github.com/OPEFFORT/content-examples))
repo to be pulled by default with the ope CLI tool for textbook creation,
we added our jupyter .ipynb test notebook. Users can run it simply with `ope test`
- [https://github.com/kevinge7/OPE-Testing/tree/tools](https://github.com/kevinge7/OPE-Testing/tree/tools) (fork of [https://github.com/OPEFFORT/OPE-Testing](https://github.com/OPEFFORT/OPE-Testing) for working on OPE command line Tools.
- [https://github.com/rkulskis/gradescope-autograder](https://github.com/rkulskis/gradescope-autograder) framework for incorporating OPE with gradescope using `ssh` and `scp`. This API allows you to outsource the autograding of student code to your OPE container on your own cluster. This allows you to run your autograder tests on a cluster on which you know the kernel is compatible with the packages used in your OPE course. It then uploads the results back to gradescope for publishing.



## Videos

- **[Sprint 1 Recording](https://drive.google.com/file/d/1SKNGodw3gZbhzO0-K-_QMrUeJU3uBJo4/view?usp=sharing)**
- **[Sprint 2 Recording](https://drive.google.com/file/d/1lJqYb4c8eatcnu1teSPzbsKXZmZMlphi/view?usp=sharing)**
- **[Sprint 3 Recording](https://drive.google.com/file/d/1Iy90VqmvtLN4ZKXjmvYmGfP7ebv0lfrO/view?usp=drivesdk)**

## Slides
- **[Sprint 2 Slides](https://docs.google.com/presentation/d/1fL5fSKnzFHu7jynSGlMBzb1nYSS9v-ooWViMfuFNXDw/edit?usp=sharing)**
- **[Sprint 3 Slides](https://docs.google.com/presentation/d/1KDC8MQQU-c8FvkvjlLuOMwSis7lFfOR7dl87srLiVJI/edit)**
