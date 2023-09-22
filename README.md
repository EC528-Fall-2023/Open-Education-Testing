** **

## Project Description Template

The purpose of this Project Description is to present the ideas proposed and decisions made during the preliminary envisioning and inception phase of the project. The goal is to analyze an initial concept proposal at a strategic level of detail and attain/compose an agreement between the project team members and the project customer (mentors and instructors) on the desired solution and overall project direction.

This template proposal contains a number of sections, which you can edit/modify/add/delete/organize as you like.  Some key sections we’d like to have in the proposal are:

- Vision: An executive summary of the vision, goals, users, and general scope of the intended project.

- Solution Concept: the approach the project team will take to meet the business needs. This section also provides an overview of the architectural and technical designs made for implementing the project.

- Scope: the boundary of the solution defined by itemizing the intended features and functions in detail, determining what is out of scope, a release strategy and possibly the criteria by which the solution will be accepted by users and operations.

Project Proposal can be used during the follow-up analysis and design meetings to give context to efforts of more detailed technical specifications and plans. It provides a clear direction for the project team; outlines project goals, priorities, and constraints; and sets expectations.

** **

## 1.   Vision and Goals Of The Project:

Our project's vision is to create an innovative and immersive educational environment where the integration of Jupyter notebooks and Linux terminal interactions transcends traditional learning boundaries. We aim to cultivate a dynamic ecosystem where teachers and students can utilize technology to enhance the educational experience. Some of our visions and improvements consist of: 

Integration of Comprehensive Tests: We recognize the importance of the Master_Container_Test.yml, which consolidates various image, build, gdb, and UI tests into one. To improve this, we will continually update and expand the test suite to cover a broader range of scenarios and edge cases. This will ensure comprehensive validation of the OPE repository base container image.

Recognizing  limitations of outdated testing methods: We are committed to a modernization effort centered around automation. By embracing automated testing, continuous integration and deployment, and scalable frameworks, we aim to improve reliability, efficiency, and adaptability in our testing approach. This shift ensures that as the Open Education (OPE) project evolves, testing practices evolve with it, delivering a more robust and future-ready educational platform.

Continuous Monitoring: We will implement continuous monitoring of our container images to identify any discrepancies, vulnerabilities, or performance issues. This proactive approach will help us maintain the reliability and security of the OPE environment.

Custom Test Development: As part of our commitment to improving the OPE project, we will develop new custom tests tailored to the specific requirements and unique features of our containerized educational materials. These tests will be designed to address our project's needs. 

Training and Skill Development: We recognize the importance of equipping our team members with the skills and knowledge required to excel in testing and automation. We will invest in training, building, and skill development to enhance our team's capabilities.

## 2. Users/Personas Of The Project:

Open Education is designed to provide greater accessibility for computer science educators and students. Users will have an easy method of distributing their content from a virtual environment through open source material. This is included but may not be limited to online textbooks, lectures, machine learning tools, as well as interactive kernel environments. Hosts of large computer science events (ie. hackathons) will also be able to use this online platform to provide a consistent environment among each user, with the same packages for everyone. Users of this platform may include but are not limited to:
* Educators within any field of computer science or engineering
* Authors looking to publish free open-source textbooks online
* Students involved in large computer science activites or events

** **


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

![](images/diagram.png)


Throughout the duration of this project, we will be contributing directly to open education tests. These tests directly involve the functionality of jupyter notebooks and other supported platforms. They do not involve server-side support, such as containerized support and remote access.
 
 

## 5. Acceptance criteria

Minimum acceptance criteria: 
   - The tests ensure that the base container only passes the build process if all of the packages are compatible and fully functioning, the address randomization works (need to clarify more on      this), and all of the dynamic content functions as intended.
   - Successfully deploy base container to NERC or some test cluster.
   - Implement all of the ope commands listed in the OPE-Testing *tools* branch as described by Professor Appavoo to allow for a more user-friendly framework for content creation. Also, add          necessary documentation for these commands.

Stretch goals: 
   - Add tool for translating textbooks written in LaTeX into the Jupyter Notebook format so that they can be hosted online and provide additional functionality by incorporating the suite of         Jupyter tools.

## 6.  Release Planning:

Release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher level details for the first iteration is expected.

1. **Also build container on a cluster (either NERC or test cluster). Verify and expand upon all of OPE textbook (8 tests)**
   - Build and deploy the container on a cluster, verify that it can run.
   - Rewrite Makefile and Dockerfile to work independent of ISA of system (arm64, x86). Should raise errors for incompatible packages with ISA (e.g. GDB not supported for ARM, stop build             process).
   - Go through OPE-Testing/.github/workflows/Master_Container_Test.yaml, test existing tests for missed edge cases (with a focus on GDB, and package version tests)
2. **Expand upon testing for RISE, write testing for Address randomization.**
   - Write address randomization tests using gdb.
   - Add onto selenium tests with RISE, look for missed edge cases.
3. **Write multimedia and terminal verification tests**
   - Write tests (maybe in Selenium?) for multimedia players and dynamic content. Also, write some tests to ensure the terminal functions as             required.
4. **Add functionality for ope commands listed by appavoo in tools branch**
   - Meet with Professor Appavoo (or send an email, but ideally meet) to ask for clarification where needed on the commands and verify our understanding is correct for each.
5. **Write code to translate LaTeX projects into OPE Jupyter NB framework**
   - At least start the framework for this. A professor who already wrote their textbook in LaTeX wants an easy migration to this platform to reap all the benefits of the OPE features and            hosting it online, but the barrier to entry is all the work of rewriting.
   - Write this code with pandoc and bash, maybe python too to parse sections of LaTeX and use *ope tools* developed in sprint 4 to make this process easier.
** **

## General comments

Remember that you can always add features at the end of the semester, but you can't go back in time and gain back time you spent on features that you couldn't complete.

** **
