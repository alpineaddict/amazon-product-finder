#!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out test framework with pytest
# TODO: Make sure rogue chrome processes are killed on host machine
# TODO: Possibly remove self prefix from web driver variable(s)
# TODO: Create loop to add additional product
# TODO: Remove "product" redundancy
# TODO: Try except blocks for each method to catch element not found errors?

# Things that are not working
# XXX: Firefox: not declining protection plan
# XXX: Searching for "french press" on chrome
# XXX: Safari not working

from chrome_webdriver import ChromeAmazonProductFinder
from firefox_webdriver import FirefoxAmazonProductFinder
from safari_webdriver import SafariAmazonProductFinder
from browser_webdriver import AmazonProductFinder
import sys

def userPrompt():
    """Prompt user to search for a product. Return product"""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please input a product to search for, and amazon product finder "
        "will automagically\nfind the highest rated product of your search "
        "and add it to the shopping cart."
    )
    product_search = input("Product search: ")
    return product_search

def main():
    """Run user prompt search and build Selenium object. Initiate search"""
    # product_search = userPrompt()

    print("Script running. Please wait...")
    product_search = 'electric tea kettle'
    PRODUCT_WEBSITE = 'https://amazon.com'

    browser = AmazonProductFinder('chrome', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('firefox', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('safari', PRODUCT_WEBSITE, product_search)

    browser.searchForProduct()
    browser.adjustSearchFilter()
    browser.goToProductPage()
    browser.addProductToCart()
    browser.goToCart()

    # browser = ChromeAmazonProductFinder(PRODUCT_WEBSITE, product_search)
    # firefox_browser = FirefoxAmazonProductFinder(PRODUCT_WEBSITE, product_search)

    print("Script complete! Exiting program.")

if __name__ == '__main__':
    main()