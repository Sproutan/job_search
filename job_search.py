import csv
from datetime import datetime
from itertools import count
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    """Generate a url from position and location"""
    template = "https://www.indeed.com/jobs?q={}&l={}&from=searchOnHP"
    url = template.format(position, location)
    return url

def get_record(card):
    # Extract job data from a single record
    atag = card.h2.a.span
    atag2 = card.h2.a
    job_title = atag.get('title')
    job_url = 'https://www.indeed.com' + str(atag2.get('href'))
    company_name = card.find("span", "companyName").text.strip()
    job_location = card.find('div', "companyLocation").text.strip()
    job_summary = card.find('div', 'job-snippet')
    posted_date = card.find('span', "date")
    today = datetime.today().strftime('%Y-%m-%d')
    try:
        salary = card.find('div','attribute_snippet').text
    except AttributeError:
        salary = ' '

    record = (job_title, company_name, job_location, posted_date, today, job_summary, salary, job_url)

    return record

def main(position, location):
    # Run the main program routine
    records = []
    url = get_url(position, location)


    # extract the job data
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('table', 'jobCard_mainContent')
        
        for card in cards:
            record = get_record(card)
            records.append(record)

        try:
            next_url = 'https://www.indeed.com' + soup.find('a',{'aria-label':'Next'}).get('href')
        except AttributeError:
            break

        #save the job data
        with open('results.csv', 'w', newline ='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['JobTitle','Company','Location','PostDate','ExtractDate','Summary','Salary','JobUrl'])
            writer.writerows(records)
        
        
        main("associate marketing manager", "new york ny")