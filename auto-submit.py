from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os

user = ""
password = ""
id_problem = ""

open ("code.cpp", "a").close()
pth = os.getcwd()
file = pth + '/' + "code.cpp"

ser = Service("./chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

#Đăng nhập
driver.get("http://ntucoder.net/Account/LogIn") #http://vinhdinhcoder.net/Account/LogIn
driver.find_element(By.ID, "Email").send_keys(user)
driver.find_element(By.ID, "MatKhau").send_keys(password)
driver.find_element(By.XPATH, "//input[contains(@src,'login-button.png')]").click()

#Nộp bài
while True:
  for i in range(1, 11):
   sleep(1)
   driver.get("http://ntucoder.net/Submission/Submit/?problemid=" + id_problem) #http://vinhdinhcoder.net/Submission/Submit/?problemid=
   sleep(1)
   driver.find_element(By.XPATH, "//input[@id='file']").send_keys(file)
   sleep(1)
   driver.find_element(By.XPATH, "//button[@value='Submit']").click()
  sleep(120)
