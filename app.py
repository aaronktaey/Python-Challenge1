from flask import Flask, render_template, request, redirect, send_file
from exporter import save_to_file
from scrapper import get_jobs

app = Flask("SuperScrapper")

db={}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/<random_string>')
def kimchi(random_string):
    print(random_string)
    return redirect("/")

@app.route('/report')
def report():
    keyword = request.args.get('keyword')
    if keyword:
        keyword = keyword.lower()
        fromDB = db.get(keyword)
        if fromDB:
            jobs = fromDB
            result_number = len(jobs)
        else:
            jobs = get_jobs(keyword)
            db[keyword] = jobs
            result_number = len(jobs)
    else:
        return redirect("/")
    return render_template("report.html", keyword=keyword, result_number=result_number, jobs=jobs)

@app.route('/export')
def export():
    try:
        keyword = request.args.get('keyword')
        print(keyword)
        if not keyword:
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="0.0.0.0")