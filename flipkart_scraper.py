## ----------------------------- WEB SCRAPING AUTOMATION - FLIPKART -----------------------------
## This Python Code uses Selenium, BeautifulSoup, and MySQL to scrape product data from Flipkart 
## and store it in a database.
## ----------------------------------------------------------------------------------------------

# -----------------------------
# Import Libraries
# -----------------------------
from selenium import webdriver
"""This line imports the webdriver module from the Selenium library, which allows us to 
automate web browser interactions."""
from selenium.webdriver.common.by import By
"""This line imports the By class from the selenium.webdriver.common.by module, which provides a way to 
locate elements on a web page using various strategies (e.g., by ID, name, XPath, etc.)."""
from selenium.webdriver.common.keys import Keys
"""This line imports the Keys class from the selenium.webdriver.common.keys module, which provides 
constants for keyboard keys (e.g., ENTER, RETURN, etc.) that can be used to simulate key presses in the 
browser."""
from bs4 import BeautifulSoup
"""This line imports the BeautifulSoup class from the bs4 library, which is used for parsing HTML and 
XML documents. It allows us to navigate and search the HTML structure of a web page."""
from database import get_connection
"""This import line connects the database connection which we have defined in the database.py file. 
The get_connection function will be used to establish a connection to the MySQL database where we will 
store the scraped product data."""

# -----------------------------
# Launch Browser
# -----------------------------

driver = webdriver.Chrome() 
"""This line is used to launch an instance of Google Chrome in which Flipkart will be opened and 
the scraping process will take place."""
driver.get("https://www.flipkart.com")
"""This line instructs the Chrome browser to navigate to the Flipkart website, using the get method."""

# -----------------------------
# Close Login Popup
# -----------------------------

try:
    # The code attempts to find a button element on the Flipkart homepage that contains the text '✕' 
    # (which is typically used to close popups) and clicks it to close the login popup that appears when
    # you first visit the site.
    close_button = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]") 
    #The click() method is then called on the close_button element to simulate a click action,
    #which should close the popup.
    close_button.click()
except:
    pass #If the close button is not found, the code will pass without any exception.

# -----------------------------
# Search Product
# -----------------------------

search_term = input("Enter product name: ") #The user enters the product name
search_box = driver.find_element(By.NAME, "q") #This line finds the search box on the Flipkart website by its name attribute, which is "q".
search_box.send_keys(search_term) #This line simulates typing the user's input (the product name) into the search box on the Flipkart website using the send_keys method.
search_box.send_keys(Keys.RETURN) #This line simulates pressing the "Enter" key after typing the search term, which triggers the search action on the Flipkart website.

# -----------------------------
# Get Page Source
# -----------------------------

html = driver.page_source #This line retrieves the HTML source code of the current page (which is the search results page for the entered product) and stores it in the variable html.
with open("flipkart_page.html","w",encoding="utf-8") as f:
    f.write(html) 
#This block of code opens a new file named "flipkart_page.html" in write mode with UTF-8 encoding and writes the HTML source code (stored in the html variable) to that file. This allows us to save the page source for later use or analysis.

# -----------------------------
# Parse HTML
# -----------------------------

soup = BeautifulSoup(html, "html.parser") #We use BeautifulSoup to parse HTML content of the page. We use this to navigate and extract
# product name and price from the HTML Structure of the page.

# -----------------------------
# Extract Products
# -----------------------------

products = [] #An empty list initialized to store the product information extracted from the HTML.
links = soup.find_all("a") #We use find_all method to find all <a> tags in HTML, for accessing the product links and titles.

for link in links: #A for loop is used to iterate over each link stored in the links variable.
    title = link.get("title") #Using get method, we try to extract the title of the product.
    href = link.get("href") #Using get method, we try to extract the href attribute of the link, which contains the URL of the product page.

    if (title and href and "/p/" in href and len(title) > 20): 
    #This condition checks if the title and href are not None, if the href contains "/p/" (which is a common pattern in Flipkart product URLs),
    #and if the length of the title is greater than 20 characters (to filter out irrelevant links).
        full_link = ("https://www.flipkart.com"+ href) 
        products.append({"title": title, "link": full_link}) #

# -----------------------------
# Extract Prices
# -----------------------------

prices = [] #We create an empty list to extract the prices of the products which we have extracted before.
price_elements = soup.find_all(string=lambda text: text and "₹" in text)
# We use find_all method to find all the text elements in HTML containing the rupee symbol.
# A lambda function is used to filter that respective elements and store the values in the price_elements variable.
for price in price_elements: #A for loop is used to iterate over each price stored in the price_elements variable.
    price_text = str(price).strip() #We convert the price element to a string and remove any leading or trailing whitespace using the strip() method.
    if "₹" in price_text: #We check if the price text contains the rupee symbol to ensure we are extracting valid price information.
        price_text = price_text.replace("₹", "") #We remove the rupee symbol from the price text using the replace() method.
        price_text = price_text.replace(",", "") #We remove any commas from the price text to ensure it can be stored as a numeric value in the database.
        prices.append(price_text) #We append the cleaned price text to the prices list for later use when storing the data in the database.

# -----------------------------
# Connect MySQL
# -----------------------------

connection = get_connection() #This line gets the connection to MySQL database which is defined in database.py file.
cursor = connection.cursor() #cursor() - used to create a cursor object to execute SQL queries and interact with the database.

cursor.execute("TRUNCATE TABLE scraped_products") 
#Suppose we want to clear existing data in our table, we use TRUNCATE method to update our table for new data addition.

# -----------------------------
# Print + Store
# -----------------------------

print("\nProducts Found:\n") #This line is printed to show how many products are found.

for i, (product, price) in enumerate(zip(products, prices),start=1): 
# enumerate() is used to loop through both products and prices simultaneously, providing an index (i) starting from 1 for each product-price pair.
# zip() is used to combine the products and prices lists into pairs, allowing us to access both the product information and its corresponding price in each iteration of the loop.
    print(f"{i}. {product['title']}") #This line prints the index (i) and the title of the product for each product found in the search results.
    print("Price :", price) #This line prints the price of the product for each product found in the search results.
    print("-" * 100) #This is just a separator line to separate the details of each product

    query = """INSERT INTO scraped_products (product_name, price, website) VALUES (%s, %s, %s)"""
    #A SQL query to insert the seraped products into the scraped_products table in MySQL.
    values = (product["title"], price, "Flipkart")
    #Here we store the product title, price and the scraped website name in the values variable which will be used to execute the SQL query.

    cursor.execute(query, values) #execute() - The above query line will be executed using this command.

# -----------------------------
# Commit Changes
# -----------------------------

connection.commit() #commit() - This line commits the transaction, that is the qurey executed to the database and saves the changes.
print("\nData stored successfully in MySQL!") #This line prints if the data is stored successfully in MySQL database.
cursor.close() #close() - This line closes the cursor object, to free up database resources after executing the queries.
connection.close() #This line closes the connection to the MySQL database, ensuring that all resources are properly released.
driver.quit() #quit() - This line closes the browser window that was opened by Selenium, ending the web scraping session.
