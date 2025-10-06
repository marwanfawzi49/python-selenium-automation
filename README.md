 # 🧪 Target.com Test Automation Framework

An end-to-end **UI test automation framework** built for [Target.com](https://www.target.com/) using  
**Python**, **Selenium WebDriver**, and **Behave (BDD)** — structured with the **Page Object Model (POM)** for clarity, scalability, and maintainability.

This framework automates Target.com user flows such as **product search**, **add-to-cart**, and **sign-in** functionality,  
and demonstrates a professional, job-ready QA automation setup.

---

## 🧰 Tech Stack
- **Language:** Python 3.13  
- **Framework:** Behave (BDD)  
- **Automation Tool:** Selenium WebDriver  
- **Pattern:** Page Object Model (POM)  
- **Reporting:** Allure Reports  
- **Dependency Manager:** pip (`requirements.txt`)

---

## 📁 Project Structure

python-selenium-automation/
│
├── app/
│ └── application.py # Initializes all page objects
│
├── pages/ # Page Object files
│ ├── base_page.py
│ ├── header.py
│ ├── main_page.py
│ ├── search_results_page.py
│ ├── sign_in_page.py
│ └── target_app_page.py
│
├── features/ # BDD tests
│ ├── environment.py # Browser setup & teardown
│ ├── steps/ # Step definitions
│ └── tests/ # Gherkin feature files
│
├── locators.py # (optional) Shared locators
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── .gitignore # Git exclusions


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/marwanfawzi49/python-selenium-automation.git

cd python-selenium-automation

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
pip install -r requirements.txt
behave

Feature: Target search functionality

  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify search results are shown for tea


from behave import given

@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()

👤 Author

Marwan Ismael
QA Automation Engineer | Electrical Engineering Background
📍 Houston, TX