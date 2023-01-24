from flask import Flask, render_template  # render kiralıyoruz

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=117000, number2=229000)  # index.html kiraladık

@app.route("/serdar")
def number():
    num1 = 23
    num2 = 54
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)  # body.html kiraladık

if __name__== "__main__":
    app.run(debug=True)