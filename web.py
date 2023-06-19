from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gui
class web():
    def __init__(self) -> None:
        
        options=Options()
        options.add_experimental_option('detach', True)
        self.g = gui.gui()
        self.website = self.g.returnWebsite()
        self.credentials = self.g.submitCredentials()
        self.usernameGUI = self.credentials[0]
        self.passwordGUI= self.credentials[1]
        self.choiceGUI = self.credentials[2]
        print(self.website)
        print(self.credentials[0])
        
    def uwl(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.url=self.driver.get("https://adfs.uwl.ac.uk/adfs/ls/?SAMLRequest=nVLLbsIwEPwVa%2B%2BJnUQRjUWCaBEqEhVRE3roBbnGgFXHplmH9vOb8lDphUMvllaendmd2eHoqzHkoFrUzuYQhQyIstKttd3msKynwR2MiiGKxsR7Pu78zj6rj06hJ32jRX76yaFrLXcCNXIrGoXcS16Nn%2BY8Dhnft8476QyQMaJqfS%2F14Cx2jWor1R60VMvneQ477%2FfIKXXWaKvC7tOEQobdOxW9bPAjRI9PVS2oMFogXUVZtIqATPp5tBX%2BuMOFRqw3eE3Sl9QgBTJ1rVTHVXLYCIMKyGySg4iTwSZRyWCXCpEynabbNJMRk1mqE5b2ICwFoj6o3zbETs0semF9DjGLk4AlQcLqKOIs4WkcxoPsFUh5NuBe25Oxt9x6O4GQP9Z1GZSLqgbycgmoB8A5Dn5Ub69zuE0sLuZD8V%2Brh%2FRaujiXfw%2Bj%2BAY%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=cImCWxgpagtRRrlv0WninpSJDmnci11f06H6%2FoUVF%2BWtOEkE1MqUsZOOh1UWlxBzlU8WpEUDsTPYZADEjleFIrupTsy76Hm%2Fnc4OjTAIX20k0s65Dl%2BJ2exzbTXd0WBUDB7J%2BoooFD63QbnFJ0Q77eHKcRbQ5PNAheVjVdF%2BegmZJScKtMxQgl6kPrAXFhfuusSN3qDj86xxmQrZJ3uERz4L%2BxvlbwXqqWysBODz8eIBx01%2FaHdoVZ3UjeiFM%2FpDNkFY4kQPsctl%2BASbh4XQ3Y7MXc9Rw015UbAjtMo0iwxArX5yHg5rtYBLPcSb9L%2F0E88UBeK6DKFzte83ponyGA%3D%3D")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.username = self.driver.find_element(By.ID,"userNameInput")
        self.password = self.driver.find_element(By.ID, 'passwordInput')
        self.signin = self.driver.find_element(By.ID,'submitButton')
        self.username.send_keys(self.usernameGUI)
        self.password.send_keys(self.passwordGUI)
        self.signin.click()
        try:
            self.loginerror = self.driver.find_element(By.CLASS_NAME,'back_to_login')
            self.loginerror.click()
        except:
            print("moving on")
        try:
            self.sidebar= self.driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/bb-base-layout/div/main/div/div/header/section/button').click()
        except:
            pass
        # driver.switch_to.frame

        self.driver.switch_to.active_element

        if self.choiceGUI=='Home':
            WebDriverWait(self.driver,30).until(
                EC.element_to_be_clickable(
                (By.CSS_SELECTOR,'a[href="https://online.uwl.ac.uk/ultra/institution-page"]')
                )
            ).click()

        elif self.choiceGUI=='Profile':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/profile"]')
                )
            ).click()

        elif self.choiceGUI=='Modules':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/course"]')
                )
            ).click()

        elif self.choiceGUI == 'Communities':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/organization"]')
                )
            ).click()

        elif self.choiceGUI == 'Calendar':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/calendar"]')
                )
            ).click()

        elif self.choiceGUI == 'Messages':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/messages"]')
                )
            ).click()

        elif self.choiceGUI == 'Marks':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/grades"]')
                )
            ).click()

        elif self.choiceGUI == 'Tools':
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/tools"]')
                )
            ).click()

        else:
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'a[href="https://online.uwl.ac.uk/ultra/stream"]')
                )
            ).click()
        # activity = driver.find_element(By.CSS_SELECTOR,'a[href="https://online.uwl.ac.uk/ultra/stream"]').click()
        # upcoming = driver.find_element(By.CSS_SELECTOR,'li[analytics-id="base.stream.groupings.upcoming.streamEntry"]').get_attribute()
        # print(upcoming)
        # driver.quit()
        # time.sleep(10)
    def email(self):
        self.options=webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        
        self.driver = webdriver.Chrome(options=self.options)

        self.driver.get("https://portal.uwl.ac.uk")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        try:
            self.email=self.driver.find_element(By.CSS_SELECTOR,'input[type="email"]').send_keys(self.usernameGUI)
            self.next= self.driver.find_element(By.ID,'idSIButton9').click()
            self.passw=self.driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys(self.passwordGUI)
            self.driver.switch_to.active_element

            self.driver.find_element(By.CSS_SELECTOR,'input[value="Sign in"]').click()
            self.driver.find_element(By.CSS_SELECTOR,'input[value="Yes"]').click()
            self.driver.find_element(By.CSS_SELECTOR,'a[id="emailId"]').click()
        except:
            self.driver.find_element(By.CSS_SELECTOR,'a[id="emailId"]').click()
        # driver.quit()
        # time.sleep(15)

    def guiweb(self):


        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)

        self.driver = webdriver.Chrome(options=self.options)
        try:
            self.driver.get(url="https://"+self.website)
        except:
            self.driver.close()







# g=gui.gui()
# w=web()
# w.guiweb()
