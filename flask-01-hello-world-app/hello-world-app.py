from flask import Flask  # 1st part-ilgili kütüphaneyi indir, site ayağa kaldıracağız

app = Flask(__name__)  # 2nd part-objeyi oluştur

@app.route("/")  # decorator /=anasayfa (localhost:5000)
def head():
    return "<h1>Hello World from Flask!!!</h1>"

@app.route("/second")
def second():
    return "This is my second page"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'

if __name__ == "__main__":  # 3rd part-kontrol mekanizmasını yaz ve çalıştır
    app.run(debug=True)  # özellikle mac'lerde sorun oluyor, portu değiştirmek/2000 yapmak için app.run(debug=True, port=2000) çalıştır, hiçbirşey yazmazsak 5000'de çalışır.