from flask import Flask, redirect, render_template, flash, url_for
from flask import request

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def MyhomeRoot():
    return render_template('login.html')


@app.route('/')
def home():
    return render_template('home.html')


def read_credentials(username, password):
    with open('username.txt', 'r') as file:
        for line in file:
            new_field = line.split("*")
            full_field = new_field[0].split("|")
            stored_username = full_field[0]
            stored_password = full_field[1]
            if username == stored_username and password == stored_password:
                return True

    return False


@app.route('/login', methods=["GET", "POST"])
def login():
    username = request.form['username']
    password = request.form["password"]
    if read_credentials(username, password):
        return render_template('home.html')
    else:
        return render_template('error.html')


@app.route('/Signup', methods=["GET", "POST"])
def signup():
    username = request.form['username']
    password = request.form["password"]
    email = request.form["email"]
    with open("username.txt", "a") as file:
        file.write(f"{username}|{password}|{email}*\n")
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
