from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import config

class ChromeAmazonProductFinder():
    def __init__ (self, product_search):
        """
        Create Selenium driver object and open up Amazon.com on Chrome
        Execute class methods to search for, find and add the product to cart
        """
        self.product_search = product_search
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.chrome_driver = webdriver.Chrome(chrome_options=options)
        self.chrome_driver.get('https://amazon.com')
        sleep(3)
        self.searchForProduct()
        self.adjustSearchFilter()
        self.goToProductPage()
        self.addProductToCart()
        self.goToCart()

    def userLogin(self):
        """
        Log into amazon. This method is temporarily deprecated as logging in
        via Selenium requires granting authentication permission via email
        """
        self.chrome_driver.find_element_by_css_selector(
            "#nav-link-accountList").click()
        email_address_field = self.chrome_driver.find_element_by_name("email")
        email_address_field.send_keys(config.USERNAME)
        self.chrome_driver.find_element_by_css_selector("#continue").click()
        password_field = self.chrome_driver.find_element_by_name("password")
        password_field.send_keys(config.PASSWORD)
        self.chrome_driver.find_element_by_css_selector("#signInSubmit").click()
        sleep(1)

    def searchForProduct(self):
        """Search for the product that was specified in the user prompt"""
        self.chrome_driver.find_element(
            By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys(
            self.product_search, Keys.ENTER)
        self.chrome_driver.implicitly_wait(5)

    def adjustSearchFilter(self):
        """Adjust search filter to filter by highest average review"""
        self.chrome_driver.find_element(
            By.XPATH, "//*[@id='a-autoid-0-announce']").click()
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.find_element(
            By.XPATH, "//*[@id='s-result-sort-select_3']").click()

    def goToProductPage(self):
        """Click on first result for product page"""
        self.chrome_driver.find_element(
            By.XPATH, "//div[@data-cel-widget='search_result_1']//img").click()
        self.chrome_driver.implicitly_wait(5)
        
    def addProductToCart(self):
        """Add product to cart and decline extended warranty if present"""
        self.chrome_driver.find_element(
            By.XPATH, "//*[@id='submit.add-to-cart']").click()
        try:
            decline_protection_plan = self.chrome_driver.find_element(
                By.XPATH, "//*[@id='siNoCoverage-announce']")
            self.chrome_driver.execute_script(
                "arguments[0].click();", decline_protection_plan)
        except NoSuchElementException:
            pass

    def goToCart(self):
        """Navigate to shopping cart"""
        self.chrome_driver.find_element(By.XPATH,
            "//*[@id='hlb-view-cart-announce']").click()