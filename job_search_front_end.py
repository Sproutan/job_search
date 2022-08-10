import job_search
import csv
from pandas import read_csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    with open("results.csv") as file:
        return render_template("index.html", csv=file)


if __name__ == "__main__":
    app.run(host='0.0.0.0')


# print("Welcome to my Indeed scraper")

# job_search.main("associate marketing manager","new york ny")
# 'JobTitle','Company','Location','PostDate','ExtractDate','Summary','Salary','JobUrl'



# def file_reader():
#     with open("results.csv") as file:
#         reader = csv.reader(file)

#         count = 0

#         for row in reader:
#             print(row[0])

#             if count > 10:
#                 break

#             count += 1

