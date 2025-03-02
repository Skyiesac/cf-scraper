import time
import undetected_chromedriver as uc
import sys

def login_to_codeforces(username, password):
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    try:
        driver.get("https://mirror.codeforces.com/enter?back=%2F")
        time.sleep(5)

        username_input = driver.find_element("name", "handleOrEmail")
        password_input = driver.find_element("name", "password")
        login_button = driver.find_element("class name", "submit")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button.click()

        time.sleep(10)

        if "enter" not in driver.current_url:
            print("Login successful!")
        else:
            print("Login failed.")

    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Error quitting driver: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python file.py username <username> password <password>")
        sys.exit(1)

    username = sys.argv[2]  
    password = sys.argv[4] 

    login_to_codeforces(username, password)