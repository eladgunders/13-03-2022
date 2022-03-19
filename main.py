from flask import Flask, redirect, render_template, request, url_for


pw = '12345678'


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        if request.form['txt_password'] == pw:
            user = request.form['txt_name']
            return redirect(url_for("user", usr=user))
        else:
            return render_template('login_failed.html')

@app.route("/<usr>")
def user(usr):
    return f'<h1>Hello {usr}</h1>'

 
if __name__ == '__main__':
    app.run()