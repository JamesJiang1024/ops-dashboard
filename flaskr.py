import sqlite3
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE='/tmp/flaskr.db'
DEBUG=True
USERNAME='admin'
PASSWORD='default'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def show_dashboard():
    return render_template("index.html", data="abc")

@app.route("/cluster")
def show_cluster():
    return render_template("cluster.html", data="abc")

@app.route("/pool")
def show_pool():
    return render_template("pool.html", data="abc")

@app.route("/position")
def show_position():
    return render_template("position.html", data="aaa")


@app.route("/node")
def show_node():
    return render_template("node.html", data="cc")

@app.route("/play")
def show_play():
    return render_template("play.html", data="cc")

@app.route("/playbook")
def show_playbook():
    return render_template("playbook.html", data="cc")

@app.route("/playgroup")
def show_playgroup():
    return render_template("playgroup.html", data="cc")
   
if __name__ == '__main__':
    app.run(host="0.0.0.0")
