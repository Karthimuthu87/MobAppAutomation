import unittest
from appium import webdriver, options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Pixel 6 API 31',
    appPackage='com.example.aplikasi_absen',
    appActivity='com.example.aplikasi_absen.StartActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_registration(self) -> None:

        resister_button = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/avStart_card_signup")
        resister_button.click()
        self.driver.implicitly_wait(10)
        full_name = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_fullname")
        full_name.send_keys("Karthika")
        email = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_email")
        email.send_keys("karthi@gmail.com")
        phone_number = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_phonenumber")
        phone_number.send_keys("+46763261187")
        address_field = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_address")
        address_field.send_keys("Stockholm")
        password_field = self.driver.find_element(by=AppiumBy.ID, value="com.example.aplikasi_absen:id/ipt_password")
        password_field.send_keys("karthi123")
        confirm_password = self.driver.find_element(by=AppiumBy.ID,
                                                    value="com.example.aplikasi_absen:id/ipt_confirmpassword")
        confirm_password.send_keys("karthi123")
        signup_button = self.driver.find_element(by=AppiumBy.ID,
                                            value="com.example.aplikasi_absen:id/avRegister_card_btnRegister")
        signup_button.click()


if __name__ == '__main__':
    unittest.main()
