pytest -v -s --alluredir="report" TestsCases\TestLogin.py
allure generate report --clean
allure serve allure-report

