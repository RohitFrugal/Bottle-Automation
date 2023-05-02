import subprocess

allure_results_dir = '/report'
report_dir = '../Reports'

cmd = f"allure generate {allure_results_dir} --clean --output {report_dir}"
subprocess.call(cmd, shell=True)
