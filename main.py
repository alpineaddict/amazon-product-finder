#!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out test framework with pytest
# TODO: Try except blocks for each method to catch element not found errors?

from browser_webdriver import AmazonProductFinder
import sys

def userPrompt():
    """Prompt user to search for a product. Return product"""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please choose a browser to use and input a product to search for, "
        "and amazon product finder will automagically\nfind the highest rated "
        "product of your search and add it to the shopping cart."
    )
    supported_browsers = ['chrome', 'firefox', 'safari']

    while True:
        print("Supported browsers: [Chrome, Firefox, Safari]")
        browser_type = input("Browser: ").lower()
        if browser_type not in supported_browsers:
            print("ERROR! Specified browser is not in supported browser list.")
            print("Please try again.")
            continue
        else:
            product_search = input("Product search: ")
            break
    return browser_type.lower(), product_search

def additionalProductSearchPrompt():
    """Prompt user whether or not to search for another product"""
    choices = ['yes', 'no']
    
    print("Would you like to search for another product?")
    while True:
        answer = input("Yes/No: ").lower()
        if answer in choices:
            return answer.lower()
        else: 
            print("ERROR! Please type yes or no.")
            continue

def main():
    """Run user prompt search and build Selenium object. Initiate search"""
    PRODUCT_WEBSITE = 'https://amazon.com'

    while True:
        browser_type, product_search = userPrompt()
        print("Script running. Please wait...")
        selenium_browser = AmazonProductFinder(browser_type, PRODUCT_WEBSITE, product_search)
        selenium_browser.searchForProduct()
        selenium_browser.adjustSortOrder()
        selenium_browser.goToProductPage()
        selenium_browser.addProductToCart()
        selenium_browser.goToCart()
        print("Script complete!")
    
        if additionalProductSearchPrompt() == 'yes':
            continue
        else:
            print("Closing browser window. Exiting program.")
            selenium_browser.closeBrowserWindow()
            sys.exit()

if __name__ == '__main__':
    main()
