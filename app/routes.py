from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.urls import url_parse
from app import app
from app import db
from app.models import Deceased
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/akahn')
def akahn():
    return render_template("akahn.html")

@app.route('/mkahn')
def mkahn():
    return render_template("mkahn.html")

@app.route('/friedman')
def friedman():
    return render_template("friedman.html")

@app.route('/yamnik')
def yamnik():
    return render_template("yamnik.html")

@app.route('/memorial', methods=["GET", "POST"])
def memorial():
    plaques = []
    records = db.session.query(Deceased).order_by(Deceased.full_name)
    for record in records:
        send_date = f'{record.secular_death_date:%A} {record.secular_death_date:%B} {record.secular_death_date.day}, {record.secular_death_date.year}'
        plaques.append({"first_name" : record.first_name, "last_name" : record.last_name, "secular_death_date" : send_date, "jewish_death_date": record.jewish_death_date})
    return render_template('memorial.html', plaques=plaques)
