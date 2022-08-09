import csv
from datetime import datetime
from itertools import count
import requests
from bs4 import BeautifulSoup


template = "https://www.indeed.com/jobs?q={}&l={}&from=searchOnHP"

def get_url(position, location):
    """Generate a url from position and location"""
    template = "https://www.indeed.com/jobs?q={}&l={}&from=searchOnHP"
    url = template.format(position, location)
    return url

url = get_url('associate marketing manager', 'palo alto ca')

## extract raw html

response = requests.get(url)

print(response)
print(response.reason)

soup = BeautifulSoup(response.text, 'html.parser')

cards = soup.find_all('table', 'jobCard_mainContent')

u = len(cards)
print(u)

## Prototype the model with a single record ##

card =  cards[0]

atag = card.h2.a.span
atag2 = card.h2.a

job_title = atag.get('title')

print(job_title)

job_url = 'https://www.indeed.com' + str(atag2.get('href'))

print(job_url)

company_name = card.find("span", "companyName").text.strip()

print(company_name)

company_location = card.find('div', "companyLocation").text.strip()

print(company_location)

company_summary = card.find('div', 'job-snippet')

print(company_summary)

posted_date = card.find('span', "date")

print(posted_date)

today = datetime.today().strftime('%Y-%m-%d')

try:
    salary = card.find('div','attribute_snippet').text
except AttributeError:
    salary = ' '

print(salary)


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

records =[]

for card in cards:
    record = get_record(card)
    records.append(record)

#Getting the next page

while True:
    try:
        next_url = 'https://www.indeed.com' + soup.find('a',{'aria-label':'Next'}).get('href')
    except AttributeError:
        break

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('table', 'jobCard_mainContent')
    
    for card in cards:
        record = get_record(card)
        records.append(record)


job_count = len(records)

print(job_count)