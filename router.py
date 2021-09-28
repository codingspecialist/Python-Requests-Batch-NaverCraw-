from flask import Flask
from flask.templating import render_template
import news_api as na

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", newsList=na.getNewsApi())

if __name__ == "__main__":
    app.run(debug=True, port=5000)