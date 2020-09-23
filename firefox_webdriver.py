class FirefoxAmazonProductFinder():
    def __init__ (self, product_search):
        self.product_search = product_search
        self.firefox_driver = webdriver.Firefox()
        self.firefox_driver.get('https://amazon.com')
        self.searchForProduct()
        self.adjustSearchFilter()

    def searchForProduct(self):
        """Search for the product that was specified in the user prompt"""
        self.firefox_driver.find_element(
            By.XPATH, "//*[@id='twotabsearchtextbox']").send_keys(
            self.product_search, Keys.ENTER)
        self.firefox_driver.implicitly_wait(5)

    def adjustSearchFilter(self):
        """Adjust search filter to filter by highest average review"""
        self.firefox_driver.find_element(
            By.XPATH, "//*[@id='a-autoid-0-announce']").click()
        self.firefox_driver.implicitly_wait(5)
        self.firefox_driver.find_element(
            By.XPATH, "//*[@id='s-result-sort-select_3']").click()

    def goToProductPage(self):
        pass
    
    def addProductToCart(self):
        pass

    def __str__(self):
        pass