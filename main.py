import requests
import smtplib
import os

#current latitude and longitude
MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")

#email id and password for login
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = os.environ.get("API_KEY")

#OWM parameters 
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

#get weather data
response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

#send email
for hour in weather_data["hourly"][:12]:
    weather_code = hour["weather"][0]["id"]
    if weather_code < 700:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Rain Alert!\n\nIt's going to rain today. Remember to bring an ☔.".encode('utf-8')
            )
        break
