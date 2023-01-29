#!/usr/bin/env bash
source venv/bin/activate
echo "-> Installing dependencies"
pip3 install playwright
pip3 install pytest
pip3 install pytest-playwright
playwright install
pip3 install --upgrade -r requirements.txt --quiet --user

echo "-> Removing old Allure results"
rm -r allure-results/* || echo "No results"

echo "-> Start tests"
pytest -n auto  tests --alluredir allure-results
echo "-> Test finished"

echo "-> Generating report"
allure generate allure-results --clean -o allure-report
echo "-> Execute 'allure serve' in the command line"