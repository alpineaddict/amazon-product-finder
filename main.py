#!/usr/bin/env python

"""
Utilize Selenium web driver to find products and add them to amazon cart.
App will prompt user to search for a product, then it will log into amazon,
search for the product, filter by highest rated item and then add said item
to the cart. Designed for use with Google Chrome, Firefox and Safari.
"""

# Task list 
# TODO: Build out test framework with pytest
# TODO: Create loop to add additional product
# TODO: Try except blocks for each method to catch element not found errors?

# Things to fix
# Safari breaking on addProductToCart.. not clicking on 1st product in results
# Safari closing out of window when finished, even when quit is not executed
# Safari window opens too smol; increase size
# Safari not clicking first product result if best seller

from browser_webdriver import AmazonProductFinder
import sys   # XXX unnecessary?
from time import sleep

def userPrompt():
    """Prompt user to search for a product. Return product"""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please input a product to search for, and amazon product finder "
        "will automagically\nfind the highest rated product of your search "
        "and add it to the shopping cart."
    )
    product_search = input("Product search: ")
    supported_browsers = ['chrome', 'firefox', 'safari']

    while True:
        print("Supported browsers: [Chrome, Firefox, Safari]")
        browser = input("Browser: ").lower()
        if browser not in supported_browsers:
            print("ERROR! Specified browser is not in supported browser list.")
            print("Please try again.")
            continue
        else:
            break
    return product_search, browser

def main():
    """Run user prompt search and build Selenium object. Initiate search"""
    PRODUCT_WEBSITE = 'https://amazon.com'
    product_search, browser.lower() = userPrompt()
    print("Script running. Please wait...")

    # XXX: Remove these lines once testing is no longer needed
    # product_search = 'french press'
    # browser = AmazonProductFinder('chrome', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('firefox', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('safari', PRODUCT_WEBSITE, product_search)

    find_product = AmazonProductFinder(browser, PRODUCT_WEBSITE, product_search)
    browser.searchForProduct()
    browser.adjustSortOrder()
    browser.goToProductPage()
    browser.addProductToCart()
    browser.goToCart()
    browser.closeBrowserWindow()
    print("Script complete! Exiting program.")

if __name__ == '__main__':
    main()

    # XXX: Remove once testing is complete
    # counter = 1
    # for iter in range(25):
    #     print(f"Run # {counter}")
    #     main()
    #     print()
    #     counter += 1
