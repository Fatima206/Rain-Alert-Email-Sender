import requests
import smtplib
import os

MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = os.environ.get("API_KEY")

