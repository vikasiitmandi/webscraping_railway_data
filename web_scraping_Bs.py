import requests
from bs4 import BeautifulSoup
import csv

class WebScraper:
    def __init__(self, url):
        # Initialize the WebScraper with the provided URL and a user-agent header
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def make_request(self):
        # Make an HTTP GET request to the specified URL with the defined headers
        response = requests.get(self.url, headers=self.headers)
        return response

    def parse_html(self, html_content):
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find the table in the HTML
        table = soup.find('table')
        
        # Extract data from the table
        data = []
        for row in table.find_all('tr'):
            cols = row.find_all(['td', 'th'])
            cols = [col.text.strip() for col in cols]
            data.append(cols)
        return data

    def save_to_csv(self, data, filename='output1.csv'):
        # Save the extracted data to a CSV file
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(data)

    def run(self):
        # Execute the entire scraping process
        response = self.make_request()

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the HTML content from the response
            html_content = response.content
            
            # Parse HTML and extract data
            parsed_data = self.parse_html(html_content)
            
            # Save the data to a CSV file
            self.save_to_csv(parsed_data)
            
            print("CSV file has been created successfully.")
        else:
            print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")

# Usage
url_to_scrape = 'https://www.cleartrip.com/trains/amp/list'
scraper = WebScraper(url_to_scrape)
scraper.run()

