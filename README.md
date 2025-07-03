# Code Analysis System – wit push Integration

## 📌 Overview

This project is a **backend system** developed as part of a final project. It integrates with the `wit push` command to ensure high-quality Python code is maintained across all commits. The system performs code analysis using the Abstract Syntax Tree (AST) module, detects common issues, and generates visual graphs with insights using Matplotlib. It simulates a basic form of internal CI (Continuous Integration) focused on code quality.

### Key Features:
- **Code Quality Checks**:
  - Function Length: Warns if a function exceeds 20 lines.
  - File Length: Warns if a file exceeds 200 lines.
  - Unused Variables: Warns if a variable is assigned but never used.
  - Missing Docstrings: Warns if a function lacks a documentation string.
  - BONUS: Warns about variables written in non-English letters.

- **Visual Graphs**:
  - Histogram: Distribution of function lengths.
  - Pie Chart: Number of issues per issue type.
  - Bar Chart: Number of issues per file.
  - BONUS: Line graph tracking the number of issues over time.

- **API Endpoints**:
  - `/analyze`: Accepts Python files and returns visual graphs.
  - `/alerts`: Accepts Python files and returns issue warnings.

This system is implemented using FastAPI for the backend server and integrates with the `wit` version control system for code analysis during `push` operations.

## Installation Instructions

1. **Clone the Repository**:
   git clone https://github.com/MiriShulman/python-advanced-project.git
   cd <repository-directory>
2. Create a Virtual Environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies:
   pip install -r requirements.txt

## Execution Instructions
1. Change the path in the wit.bat file to the path of main.py in your project.
2. Add the path of your project to the system environment variable 'Path': 
   Search in your PC 'Advanced system settings' -> 'Environment Variables' -> In 'System variables' section, find 'Path', select it -> Edit -> New -> Paste here your project path -> OK -> OK -> OK.
3. ## Use the Command Line Interface (CLI)

You can interact with the Wit version control system using the CLI commands. Here are some examples:

- **Initialize the Wit Repository**:
  ```bash
  wit init
  ```
  
- **Add a File:**:
  ```bash
  wit add <file_name>
  ```
  
- **Log Commits:**:
  ```bash
  wit log
  ```
  
- **Check Status:**:
  ```bash
  wit status
  ```
  
- **Checkout a Commit:**:
  ```bash
  wit checkout <commit_id>
  ```
  
- **Runs code analysis and returns visual insights:**:
  ```bash
    wit push
  ```
## Folder Structure

project/
├── images/
├── api.py
├── cli.py
├── graphs.py
├── main.py
├── our_ast.py
├── README.md
├── requirements.txt
├── test.py
├── wit.py
├── wit.bat

## API Endpoints

The following endpoints are available in the system:

### **`POST /alerts`**
Analyzes the given project folder and returns detected problems or alerts.

**Request Example:**
```json
{
  "path": "path/to/your/project"
}
```
**Response Example:**
```json
{
  "problems": {
    "file1.py": 3,
    "file2.py": 1
  }
}
```

### **`POST /analyze`**
Performs code analysis and generates visual graphs based on code structure and detected issues.

**Request Example:**
```json
{
  "path": "path/to/your/project"
}
```
**Response Example:**
```json
{
  "images": [
    "./images/number_of_issues_per_file.png",
    "./images/pie_chart_number_of_issues.png",
    "./images/histogram_functions_lengths.png"
  ]
}
```