from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from hcaptcha import solvehCaptcha
from datetime import datetime
import requests
import time
import random
import pickle
import json
import os


def discord_register(email, username):
    url = "https://discord.com/register"

    options = webdriver.ChromeOptions()

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        )

    options.add_argument("accept-language=en-US,en;q=0.5")

    driver = webdriver.Chrome(
        executable_path=r"chromdriver\chromedriver.exe", 
        options=options
    )

    try:
        driver.get(url=url)
        time.sleep(8)       

        email_input = driver.find_element(By.ID, "uid_5")
        email_input.clear()
        email_input.send_keys(email)

        username_input = driver.find_element(By.ID, "uid_7")
        username_input.clear()
        username_input.send_keys(username)  

        chars = "+-/*!&$?=@<>#abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        length = 8
        password =''
        for i in range(length):
            password += random.choice(chars)

        password_input = driver.find_element(By.ID, "uid_9")
        password_input.clear()
        password_input.send_keys(password)

        month_list = ['January', 'February', 'March', 'April', 'May', 
        'June', 'July', 'August', 'September', 
        'October', 'November', 'December'
        ]
        month_input = driver.find_element(By.ID, "react-select-2-input")
        month_input.clear()
        month = random.choice(month_list)
        month_input.send_keys(month)
        month_input.send_keys(Keys.ENTER)

        date_input = driver.find_element(By.ID, "react-select-3-input")
        date_input.clear()
        date = random.randint(1, 29)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        year_input = driver.find_element(By.ID, "react-select-4-input")
        year_input.clear()
        year = random.randint(1985, 2005)
        year_input.send_keys(year)
        year_input.send_keys(Keys.ENTER)
        time.sleep(2)

        date_of_birth = f"{year}-{month}-{date}"
        convert_date = str(datetime.strptime(date_of_birth, "%Y-%B-%d")).split(" ")[0]

        login_button = driver.find_element(By.XPATH,"//button[contains(@class, 'button-1cRKG6')]").click()
        time.sleep(5)
        
        try:
            error_message = driver.find_element(By.XPATH,"//span[@class='errorMessage-1kMqS5']")
            driver.close()
            driver.quit()
            print("Email - Email/Username is already registered :( ==> Enter new data")
            email = input("Enter your email: ")
            username = input("Enter your username: ")
            discord_register(email, username)
        
        except:
            captcha_sitekey = str(
                driver.find_element(By.XPATH,"//div[contains(@class, 'flexCenter-1Mwsxg')]/div/iframe").get_attribute("src")
                )
            sitekey_clean = captcha_sitekey.split("&")[9].split("sitekey=")[-1]
            print("website key received: " + sitekey_clean)

            print("start processing hCaptcha: ....... ==> please wait 30 seconds")
            result = solvehCaptcha(
                sitekey=f'{sitekey_clean}',
                url=f'{url}',
            )

            time.sleep(30)
            
            if result:
                print("hCaptcha solved successfully :) ==> ")
                code = result['code']

                headers = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.5',
                    'content-type': 'application/json',
                    'dnt': '1',
                    'origin': 'https://discord.com',
                    'referer': 'https://discord.com/register',
                    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-fingerprint': '1013322895528841226.gdq10v9rzo7cmATZS3kTHq_4Mag',
                    'x-super-properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0NDA1NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
                    }

                json_data={
                    "captcha_key": f"{code}",
                    "consent": 'true',
                    "date_of_birth": f"{convert_date}",
                    "email": f"{email}",
                    "fingerprint": "1013322895528841226.gdq10v9rzo7cmATZS3kTHq_4Mag",
                    "gift_code_sku_id": 'null',
                    "invite": 'null',
                    "password": f"{password}",
                    "promotional_email_opt_in": 'false',
                    "username": f"{username}",        
                }
                
                print("form a request to get a token")
                response = requests.post(
                    'https://discord.com/api/v9/auth/register', 
                    headers=headers, 
                    json=json_data
                    )
                token = response.text.split("\"")[3]
                print("token_register_user: " + token)

        time.sleep(5)

        if not os.path.isdir('cookies'):
            os.makedirs('cookies')
        
        print(f"save_cookies_user: {username} ")
        pickle.dump(driver.get_cookies(), open(f'cookies/{username}_cookies', 'wb'))
        print(f"saved_cookies_user: {username} ")
        
        time.sleep(10)

        if not os.path.isdir('data'):
            os.makedirs('data')

        all_data = {
            "email": email, 
            "username": username,
            "password": password,
            "sitekey": sitekey_clean,
            "code_hcaptcha": code,
            "token_register_user": token
        }

        print(f"save_other_data_user: {username} ")
        with open(f"data/{username}.json", "w", encoding="utf=8") as file:
            json.dump(all_data, file, indent=4, ensure_ascii=False)
        print(f"saved_other_data_user: {username} ")

        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    email = input("Enter your email: ")
    username = input("Enter your username: ")
    discord_register(email, username)