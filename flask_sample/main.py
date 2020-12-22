from flask import Flask, render_template, request, redirect, send_file

from exporter import save_to_file
from fake_scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("potato.html")


@app.route("/<username>")
def contact(username):
    return f"Hello {username}! How are you doing?"


@app.route("/report")
def report():
    print(request.args)
    word = request.args.get('word')
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs

    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        existing_jobs = db.get(word)
        if not existing_jobs:
            raise Exception()
        print('save_to_file')
        save_to_file(existing_jobs)
        return send_file('jobs.csv')
    except Exception as e:
        print('exception!!!!', e)
        return redirect("/")


app.run(host="127.0.0.1")  # repl.it 에서는 "0.0.0.0"
