import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "E:\code\python\WeatherForecast_WebApp\data_small\TG_STAID"+ str(station).zfill(6)+".txt"
    df = pd.read_csv(filename, skiprows = 20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]['   TG'].squeeze()/10

    return {"date": date,
            "station": station,
            "temperature": temperature}


if __name__ == "__main__":
    app.run(debug=True)  # this will allow you to see the error in the web page
