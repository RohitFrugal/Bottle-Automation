import os
import shutil
import pytest

test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TestsCases")


def run_tests():
    # Define the path to the allure report folder
    report_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Report")

    # Delete the old allure report folder if it exists
    if os.path.exists(report_dir):
        shutil.rmtree(report_dir)

    # Run the test cases and generate the allure report
    pytest.main([
        "--alluredir={}".format(report_dir),
        test_dir
    ])

if __name__ == '__main__':
    run_tests()