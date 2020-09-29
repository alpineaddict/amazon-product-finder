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
# TODO: Decide whether or not to leave browser choice in user prompt

# Things to fix
# XXX: INCONSISTENCY: Firefox unable to decline warranty
# XXX: INCONSISTENCY: Firefox unable to click "sort by" button
# XXX: INCONSISTENCY: Firefox not able to go to cart
# XXX: Firefox script not closing after last method execution
# XXX: Searching for "french press" on chrome
# XXX: Safari not working at all

from browser_webdriver import AmazonProductFinder

def userPrompt():
    """Prompt user to search for a product. Return product"""
    print("=" * 28, "AMAZON PRODUCT FINDER" ,"=" * 28)
    print("Please input a product to search for, and amazon product finder "
        "will automagically\nfind the highest rated product of your search "
        "and add it to the shopping cart."
    )
    product_search = input("Product search: ")
    print("Browsers available: Chrome, Firefox, Safari.")
    browser = input("Browser: ")
    return product_search, browser

def main():
    """Run user prompt search and build Selenium object. Initiate search"""
    # product_search, browser = userPrompt()

    print("Script running. Please wait...")
    product_search = 'electric tea kettle'
    PRODUCT_WEBSITE = 'https://amazon.com'

    # browser = AmazonProductFinder('chrome', PRODUCT_WEBSITE, product_search)
    browser = AmazonProductFinder('firefox', PRODUCT_WEBSITE, product_search)
    # browser = AmazonProductFinder('safari', PRODUCT_WEBSITE, product_search)
    # find_product = AmazonProductFinder(browser, PRODUCT_WEBSITE, product_search)

    browser.searchForProduct()
    browser.adjustSearchFilter()
    browser.goToProductPage()
    browser.addProductToCart()
    browser.goToCart()

    print("Script complete! Exiting program.")

if __name__ == '__main__':
    main()