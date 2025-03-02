import time
import requests
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import sys

def scrape_submission_id(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table')
        
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            if len(columns) > 5: 
                submission_id = columns[0].text.strip()  
                verdict = columns[5].text.strip()
                
                if verdict == "Accepted":
                    print(f"Submission ID: {submission_id}")
                    return submission_id  

    print("No accepted submissions found.")
    return None


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
            return True
        else:
            print("Login failed.")
            return False

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

    if login_to_codeforces(username, password):
        url = "https://mirror.codeforces.com/problemset/status/2073/problem/A"
        scrape_submission_id(url)