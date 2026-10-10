# 🧪 Saucedemo Test Automation Suite

An end-to-end test automation project for [SauceDemo](https://www.saucedemo.com/), built with **Python**, **Selenium**, and **Pytest**. The project follows the **Page Object Model (POM)** design pattern and includes CI/CD integration via GitHub Actions and test reporting via Allure.

---

## 📁 Project Structure

```
saucedemo_TestCases/
│
├── pages/                   # Page Object Model classes
│   ├── __init__.py
│   ├── error_page.py        # Error page interactions
│   ├── login.py             # Login logic
│   ├── login_page.py        # Login page locators & actions
│   ├── product_page.py      # Product listing page
│   └── purchase.py          # Checkout/purchase flow
│
└── tests/                   # Test cases
    ├── .github/workflows/   # GitHub Actions CI/CD pipeline
    ├── __init__.py
    ├── conftest.py           # Pytest fixtures & setup
    ├── test_invalid_product.py
    ├── test_login.py
    ├── test_logout.py
    ├── test_purchase.py
    ├── test_sorting.py
    └── test_view_product.py
```

---

## ✅ Test Coverage

| Test File | Feature Tested |
|---|---|
| `test_login.py` | Valid & invalid login scenarios |
| `test_logout.py` | User logout flow |
| `test_purchase.py` | End-to-end checkout process |
| `test_sorting.py` | Product sorting (A-Z, Z-A, price) |
| `test_view_product.py` | Product detail page |
| `test_invalid_product.py` | Edge cases for invalid product access |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Testing Framework:** Pytest
- **Browser Automation:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Allure
- **CI/CD:** GitHub Actions

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.x
- Google Chrome + ChromeDriver (matching versions)

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

```bash
# Run all tests
pytest tests/

# Run a specific test file
pytest tests/test_login.py

# Run with Allure reporting
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

---

## 🔄 CI/CD

This project uses **GitHub Actions** to automatically run the test suite on every push. The workflow is defined in `tests/.github/workflows/`.

---

## 👩‍💻 Author

**Sara Allan** — QA Engineer & Data Analyst  
[LinkedIn](https://linkedin.com/in/sara-allan-b541aa193) · [GitHub](https://github.com/saraallan8)
