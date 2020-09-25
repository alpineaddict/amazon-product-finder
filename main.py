#!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out Firefox class
# TODO: Build out Safari class
# TODO: Build out test framework with pytest
# TODO: Make sure rogue chrome processes are killed on host machine
# TODO: Possibly remove self prefix from web driver variable(s)
# TODO: Create loop to add additional product
# TODO: Implement abstract base classes
# TODO: Remove "product" redundancy
# TODO: Remove sleeps and implement EXPLICIT WAITS
        # https://selenium-python.readthedocs.io/waits.html 
# TODO: All browsers in one class?
# TODO: Remove all subsequent action methods from __init__, put into main()
# TODO: Try except blocks for each method to catch element not found errors?

from chrome_webdriver import ChromeAmazonProductFinder
from firefox_webdriver import FirefoxAmazonProductFinder
from safari_webdriver import SafariAmazonProductFinder
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
    product_search = 'electric water kettle'
    PRODUCT_WEBSITE = 'https://amazon.com'

    chrome_browser = ChromeAmazonProductFinder(PRODUCT_WEBSITE, product_search)
    # firefox_browser = FirefoxAmazonProductFinder(PRODUCT_WEBSITE, product_search)

if __name__ == '__main__':
    main()