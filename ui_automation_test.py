from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class webForm:
  def test(self):
      base_url = "https://www.ultimateqa.com/filling-out-forms/"
      driver = webdriver.Chrome()
      driver.maximize_window()
      driver.get(base_url)
      driver.implicitly_wait(5)

      driver.find_element(By.ID, "et_pb_contact_name_1").send_keys("Second name field")
      driver.find_element(By.ID, "et_pb_contact_message_1").send_keys("Second message text-box field")

      # Reading captcha details below
      x = driver.find_element(By.XPATH, "//input[@name='et_pb_contact_captcha_1']").get_attribute("data-first_digit")
      y = driver.find_element(By.XPATH, "//input[@name='et_pb_contact_captcha_1']").get_attribute("data-second_digit")
      captureSum = str(int(x) + int(y))

      driver.find_element(By.XPATH, "//input[@name='et_pb_contact_captcha_1']").send_keys(captureSum)
      buttons = driver.find_elements_by_class_name("et_pb_contact_submit")[1].click()

      # checking for the success message and print to console
      uiResponse = driver.find_element_by_css_selector("[class='et-pb-contact-message'] > p ")
      message = uiResponse.text
      print(message)
      time.sleep(10)

if __name__ == '__main__':
      wf = webForm()
      wf.test()