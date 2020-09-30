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

# XXX: Notes for next steps...
# XXX: Remove waits.. then use PDB to get full stack trace of why elements could not be found?

# Things to fix
# XXX: INCONSISTENCY: Firefox unable to decline warranty
# XXX: INCONSISTENCY: Firefox unable to click "sort by" button
    # "Sort by: Featured" gets highlighted, but dropdown does not appear.
# XXX: INCONSISTENCY: Firefox not able to go to cart - related to decline warranty offer
# XXX: Firefox script not closing after last method execution
# XXX: Searching for "french press" on chrome
# XXX: Safari not working at all

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
    # product_search, browser.lower() = userPrompt()
    print("Script running. Please wait...")

    # XXX: Remove these lines once testing is no longer needed
    product_search = 'electric tea kettle'
    # browser = AmazonProductFinder('chrome', PRODUCT_WEBSITE, product_search)
    browser = AmazonProductFinder('firefox', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('safari', PRODUCT_WEBSITE, product_search)

    # XXX: uncomment this line for final script execution once bugs are worked out:
    # find_product = AmazonProductFinder(browser, PRODUCT_WEBSITE, product_search)
    browser.searchForProduct()
    browser.adjustSortOrder()
    browser.goToProductPage()
    # browser.addProductToCart()
    # browser.goToCart()
    # browser.closeBrowserWindow()
    print("Script complete! Exiting program.")

if __name__ == '__main__':
    counter = 1
    for iter in range(25):
        print(f"Run # {counter}")
        main()
        print()
        counter += 1


# TODO: build out if/else statement for "best seller" results as XML is different
# Class value cannot contain "a-section a-spacing-none"
