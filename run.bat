@echo off
setlocal

set TEST_CASE_FOLDER=E:\POM_for_Bottle\WebApp\TestsCases
set ALLURE_REPORT_FOLDER=E:\POM_for_Bottle\WebApp\AllureReports

pytest -v -s --alluredir="%ALLURE_REPORT_FOLDER%" "%TEST_CASE_FOLDER%"

endlocal
