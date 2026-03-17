# 🧪 Selenium Pytest Login Automation Framework

This project is an automated testing framework built using:
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)

It is designed for UI testing of web applications.


## 🚀 Features

- Selenium WebDriver automation
- Pytest test framework
- Page Object Model structure
- Easy-to-maintain code
- Cross-browser support (Chrome)
- Clean folder structure
- Easy setup

## 🛠 Tech Stack

- Python 3.10+
- Selenium
- Pytest
- WebDriver Manager ( Chromedriver )

## 🔄 Workflow of the Framework

### 1️⃣ Test Execution Flow

pytest → conftest.py → Browser opens → Test runs → Browser closes

### 2️⃣ How It Works

1. `pages/`
   - Contains Page Object classes
   - Stores locators
   - Contains page actions (login, click, etc.)

2. `tests/`
   - Contains test files
   - Uses functions starting with `test_`
   - Calls page methods


## 📦 Installation Steps

### 1️⃣ Clone Repository

git clone https://github.com/CodeWithAnji/login_automation_test.git

pytest

### 2️⃣ Create Virtual Environment

python -m venv venv

### 3️⃣ Activate Environment

Windows:

venv\Scripts\activate

### 4️⃣ Install Dependencies

pip install -r requirements.txt

### 5️⃣ Run Tests

pytest

## 📋 requirements.txt Example

selenium

pytest

Chromedriver 

## 👨‍💻 Author

Ganta Anjaneyulu 
GitHub: https://github.com/yourusername


