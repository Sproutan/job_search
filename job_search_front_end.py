import job_search
import csv
from pandas import read_csv
from flask import Flask, render_template, request, redirect, url_for, Response, send_file


app = Flask(__name__)


@app.route("/")


def index():
    with open("results.csv") as file:
        return render_template("index.html", csv=file)

def hello():
    return '''
        <html><body>
        Hello. <a href="/results.csv">Click me.</a>
        </body></html>
        '''

@app.route("/results.csv")

def plot_csv():
    return send_file(
        'outputs/Adjacency.csv',
        mimetype='text/csv',
        download_name='Adjacency.csv',
        as_attachment=True
    )





# x = input()
# y = input()

# job_search.main(x,y)






if __name__ == "__main__":
    app.run(host='0.0.0.0')


# print("Welcome to my Indeed scraper")


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

