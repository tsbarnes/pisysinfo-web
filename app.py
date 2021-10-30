from flask import Flask, render_template, flash, redirect, request
import psutil
from system import System

app = Flask(__name__)
app.config.from_pyfile("app.cfg")


@app.route('/')
def default():  # put application's code here
    return render_template('index.html', system=System())


if __name__ == '__main__':
    app.run()
