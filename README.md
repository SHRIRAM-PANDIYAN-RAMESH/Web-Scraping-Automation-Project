WEB SCRAPING AUTOMATION PROJECT

Project Title:
  Flipkart Product Search and Data Storage System

Project Description:
  This project is a web scraping automation system developed using Python, Selenium, BeautifulSoup, and MySQL. 
  The application automatically searches for products on Flipkart, extracts product information from the search results page, and stores the collected data in a MySQL database.
  The project demonstrates browser automation, HTML parsing, data extraction, and database integration.

Objectives:
  1) Automate product searches on Flipkart.
  2) Extract product information from search results.
  3) Store extracted information in a MySQL database.
  4) Practice web scraping and automation techniques.
  5) Build a foundation for future price tracking and product analytics systems.

Technologies Used:
  1) Python 3.10.0
  2) Selenium
  3) BeautifulSoup (bs4)
  4) MySQL
  5) Chrome Browser
  6) ChromeDriver
  7) VS Code

Project Folder Structure:
  -- Web_Scraping_Automation_Project
    -- database.py
    -- flipkart_scraper.py
    -- output.txt
    -- flipkart_page.html

Modules Used in the Python Code:
  -- selenium.webdriver
    -- Opens and controls the Chrome browser.
  -- selenium.webdriver.common.by
    -- Locates web elements using Name, XPath, ID, CSS Selector, etc.
  -- selenium.webdriver.common.keys
    -- Simulates keyboard actions such as pressing Enter.
  -- BeautifulSoup
    -- Parses HTML and extracts required information.
  -- get_connection()
    -- Custom function used to establish a MySQL database connection.

Database Deatils:
  -- Database Name: ecommerce_tracker
  -- Table Name: scraped_products
  -- Specific Columns:
    -- id
    -- product_name
    -- price
    -- website
    -- scraped_at

Project Workflow:
  1. User Input
  2. Open Flipkart Using Selenium
  3. Search Product
  4. Load Search Results
  5. Extract Product Information
  6. Store Data in MySQL Database
  7. Display Results

Methods to Run the Project:
  1) Run the MySQL Server
  2) Open the Terminal in Visual Studio Code
  3) Run the command 'python flipkart_scraper.py'
  4) Then the command when run, opens the Flipkart Website using Selenium
  5) The terminal asks for user input as 'Enter Product Name:'.
  6) After the product name gets entered, with BeautifulSoup, we parse the HTML elements of the website and access the product name and price.
  7) The details will det displayed as output in the Terminal and those details will be saved in MySQL table 'scraped_products', under the database 'ecommerce_tracker'.
  8) We can view the table in MySQL by typing the query 'SELECT * FROM scraoed_products;'.
