from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello()-> str:
    context: dict[str, str] = {'name': 'Vetrarljos'}
    return render_template("Index.html", **context)

if __name__ == "__main__":
    app.run()