import subprocess
import multiprocessing

browsers = ["chrome", "firefox"]  # List of browsers you want to test


def run_tests(browser):
    subprocess.run(
        ["pytest", "-v", "-s", "--alluredir=../../report", "Test_01_Login.py"],
        env={"BROWSER": browser}
    )


if __name__ == "__main__":
    with multiprocessing.Pool(processes=len(browsers)) as pool:
        pool.map(run_tests, browsers)
