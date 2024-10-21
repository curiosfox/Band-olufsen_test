# Bang & Olufsen Technical Interview Project

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
    - [Local Setup](#local-setup)
    - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Testing](#testing)
    - [Running Tests](#running-tests)
    - [Code Coverage](#code-coverage)
    - [Type Checking with Mypy](#type-checking-with-mypy)
- [Continuous Integration](#continuous-integration)
- [Logging](#logging)
- [Project Structure](#project-structure)
- [License](#license)

---

## **Introduction**

This application is designed to fetch and display user and post data from the JSONPlaceholder APIs. It provides a simple
command-line interface that allows users to:

- Retrieve and display a list of users.
- Retrieve and display a list of posts.
- Exit the application gracefully.

---

## **Features**

- **Command-Line Interface**: Easy-to-use menu-driven interface.
- **Data Fetching**: Retrieves data from external APIs.
- **Data Display**: Formats and displays data in a tabular form using `tabulate`.
- **Logging**: Implements logging for debugging and error tracking.
- **Type Hinting**: Uses Python type hints and passes Mypy checks.
- **Unit Testing**: Comprehensive tests written using `pytest`.
- **Code Coverage**: Test coverage reports generated using `pytest-cov`.
- **Docker Support**: Containerization using Docker for easy deployment.

---

## **Requirements**

- **Python**: 3.10 or higher
- **Dependencies**:
    - `requests`
    - `tabulate`
    - `pytest`
    - `pytest-mock`
    - `requests-mock`
    - `pytest-cov`
    - `mypy`
    - `types-requests`
    - `types-tabulate`
- **Docker** (Optional): For running the application in a container

---

## **Installation**

### **Local Setup**

1. **Clone the Repository**

 ```bash
git clone https://github.com/curiosfox/Band-olufsen_test.git
cd Band-olufsen_test
 ```

2. **Create a Virtual Environment**

```bash
python -m venv venv
```

3. **Activate the Virtual Environment**

On Windows:

```bash
venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Docker Setup**

1. **Build the Docker Image**

   Ensure Docker is installed and running on your system.

```bash
docker build -t bang-olufsen-app .
```

2. **Run the Docker Container**

```bash
docker run -it bang-olufsen-app
```

## **Running the Application Locally**

After installing the dependencies and activating the virtual environment, you can run the application using:

```bash
python -m App.main
```

## **Usage**

Upon starting the application, you will see a menu like this:

```markdown
Please select the following options to get data from the APIs:
    1. Press 1 for getting all the user data
    2. Press 2 for getting all the posts from the APIs
    3. To exit the Application

```
* Option 1: Fetches and displays all user data.
* Option 2: Fetches and displays all post data.
* Option 3: Exits the application.
### Example Usage:
```markdown
Please select the following options to get data from the APIs:
    1. Press 1 for getting all the user data
    2. Press 2 for getting all the posts from the APIs
    3. To exit the Application
1

```

After selecting 1, the application will fetch and display user data in a tabular format.
## **Testing**

### **Running Tests**

To run the unit tests, ensure you're in the project root directory and the virtual environment is activated.

```bash
pytest tests/
```

### **Code Coverage**

To generate a code coverage report:

```bash
pytest --cov=App --cov-report=html tests/
```

1. This command runs the tests and generates an HTML coverage report in the htmlcov/ directory.
2. Open htmlcov/index.html in your web browser to view the coverage report.

### **Type Checking with Mypy**
The project uses Mypy for static type checking to ensure type correctness throughout the codebase.

### Running Mypy
To perform type checking with Mypy:
```bash
mypy App/ tests/
```
This command checks all Python files in the App/ and tests/ directories.

Address any reported type errors to maintain code quality.

## **Continuous Integration**

This project includes a GitHub Actions workflow to automate the execution of the pytest suite.

### **Manual Pytest Execution Workflow**

- **Location**: `.github/workflows/manual.yml`
- **Trigger**: Manually via the GitHub Actions user interface.
- **Purpose**: Allows you to run the test suite on-demand.

#### **How to Use:**

1. Navigate to the **"Actions"** tab in your GitHub repository.
2. Click on **"Manual Pytest Execution"**.
3. Click **"Run workflow"**.
4. Select the branch (if applicable).
5. Click **"Run workflow"** to start the tests.

## **Logging**
The application uses Python's built-in logging module for logging.

### Log Levels:
* INFO: General information about the application's operation.
* WARNING: Warnings about potential issues or incorrect user inputs.
* ERROR: Errors that occur during execution, such as failed API requests.

### Log Output: 
Logs are output to the console.
You can adjust the logging level or configure logging to output to a file by modifying the create_logger function in main.py.

## **Project Structure**
```markdown
BangOlufsenProject/
├── App/
│   ├── __init__.py
│   ├── api.py
│   ├── main.py
│   ├── models.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── API/
│   │   ├── test_api_helper.py
│   │   └── test_api.py
│   ├── App/
│   │   ├── test_main_app_helper.py
│   │   └── test_main_app.py
├── Dockerfile
├── requirements.txt
├── README.md
```

* App/: Contains the application code.

  `api.py:` Handles API requests to fetch data.

  `main.py:` Entry point of the application, contains the main application logic.

  `models.py:` Defines data models using data classes.

* tests/: Contains unit tests for the application.

  `conftest.py`: Configuration for pytest fixtures.
  
  `API/test_api.py:` Tests for api.py.
  
  `App/test_main_app.py:` Tests for main.py.

* Dockerfile: Configuration file for building the Docker image.
* requirements.txt: Lists the project dependencies.
* README.md: Project documentation.

## **License**

This project is not licensed currently.
