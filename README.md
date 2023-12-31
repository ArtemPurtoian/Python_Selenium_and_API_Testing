# Selenium Web and public API testing
# Getting started
* Set English as the system default language
* Install packages
  > pip install -r requirements.txt
# Executing tests
* To run a specific test in a module:
  > pytest -k "test_name" tests/test_module.py
* Or
  > pytest tests/test_module.py::test_name
* To run a specific module:
  > pytest tests/test_module.py
* To run all tests
  > pytest
* To run tests with a specific marker:
  > pytest -m "regression"
# Reporting
* Add the following after pytest command to generate an allure report:
  > --alluredir=./allure_report
* Or use pytest HTML reporter:
  > --html-report=./html_report/report.html --title='Python Automation Project'
_________________________________________________________
# Allure
* To start a web server with the generated allure report:
  > allure serve .\allure_report\