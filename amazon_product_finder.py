#!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

import sys
from browser_webdriver import AmazonProductFinder

def user_prompt():
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
    product_search = input("Product search: ")
    return browser_type.lower(), product_search

def additional_product_search_prompt():
    """Prompt user whether or not to search for another product"""
    choices = ['yes', 'no']
    print("Would you like to search for another product?")

    while True:
        answer = input("Yes/No: ").lower()
        if answer not in choices:
            print("ERROR! Please type yes or no.")
            continue
        return answer.lower()

def main():
    """Run user prompt search and build Selenium object. Initiate search"""
    PRODUCT_WEBSITE = 'https://amazon.com'

    while True:
        browser_type, product_search = user_prompt()
        print("Script running. Please wait...")
        selenium_browser = AmazonProductFinder(browser_type, PRODUCT_WEBSITE, product_search)
        selenium_browser.search_for_product()
        selenium_browser.adjust_sort_order()
        selenium_browser.go_to_product_page()
        selenium_browser.add_product_to_cart()
        selenium_browser.go_to_cart()
        print("Script complete!")

        if additional_product_search_prompt() == 'yes':
            continue
        print("Closing browser window. Exiting program.")
        selenium_browser.close_browser_window()
        sys.exit()

if __name__ == '__main__':
    main()
