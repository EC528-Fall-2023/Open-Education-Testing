# OPE Tool

This tool is designed to facilitate the management of projects within the Open Education Project (OPE). It includes a variety of functions for handling repositories, books, containers, and course creation.

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Git installed, as it is required for several functions.
3. **Command**: In the directory, run `./install.sh`

## Usage

Each function in the script is intended for specific tasks. Below are the usages and descriptions for each function.

### General

- **Usage**: Run the tool with a specific command and relevant arguments.
- **Command**: `ope <function> [arguments]`

### `new_project` 

- **Description**: Creates a new OPE project from templates.
- **Usage**: `ope new_project <project_name> [repo_url]`
- **Arguments**:
  - `project_name`: Name of the new project.
  - `repo_url` (optional): URL of the Git repository to associate with the project.

### `new_book`

- **Description**: Creates a new book within the project.
- **Usage**: `ope new_book <book_name>`
- **Arguments**:
  - `book_name`: Name of the new book.

### `new_container`

- **Description**: Adds source for building a new container for the project.
- **Usage**: `ope new_container <container_name>`
- **Arguments**:
  - `container_name`: Name of the new container.

### `new_course`

- **Description**: Creates a new course with a standard set of books and a container.
- **Usage**: `ope new_course <course_name> [repo_url]`
- **Arguments**:
  - `course_name`: Name of the new course.
  - `repo_url` (optional): URL of the Git repository for the course.

### `update`

- **Description**: Updates and rebases changes from the OPE framework.
- **Usage**: `ope update`
- No arguments required.

### Helper Functions

- **`repo_add`**: Adds a repository to a project.
- **`findprojectdir`**: Finds the project directory.
- **`projectdir`**: Outputs the project directory.
- **`new_part`**: Creates a new part in a book or course.
- **`print_func_page`**: Prints the help page for functions.
- **`Usage`**: Prints general usage information.

### Logging and Configuration

- Color configuration is included for better readability of output.

---
For detailed instructions: please go to https://riya-deokar.github.io/Documentation/firstBook/dummy_part/chapter.html

