import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Function to fetch HTML content from a URL using Selenium
def get_html_content_selenium(url):
   ######### # for firefox#######################################################
    driver = webdriver.Firefox() 
    driver.get(url)
 ######################## for chrome #########################################
    # driver = webdriver.Chrome() 
    # driver.get(url)
    # time.sleep(10)
###########################################################################
    # Wait for the table to be present in the DOM
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'table'))
    )
    
    html_content = driver.page_source
    #driver.quit()  # Uncomment this line if you want to close the browser after getting the HTML content
    return html_content




# Function to parse HTML table and convert it to a DataFrame
def parse_html_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    if table:
        df = pd.read_html(str(table))[0]
        return df
    else:
        print("No tables found.")
        return None
    
# Function to save DataFrame to a CSV file
def save_to_csv(dataframe, csv_filename):
    dataframe.to_csv(csv_filename, index=False)

# Replace 'your_url' and 'output.csv' with the actual URL of the HTML page and desired CSV file name
url = 'https://www.cleartrip.com/trains/amp/list'
csv_filename = 'output2.csv'

# Fetch HTML content from the URL using Selenium
html_content = get_html_content_selenium(url)

# Parse HTML table into a DataFrame
table_data = parse_html_table(html_content)

if table_data is not None:
    # Save DataFrame to a CSV file
    save_to_csv(table_data, csv_filename)
