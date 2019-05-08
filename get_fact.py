# Get Facts
import requests
from flask import Flask
from bs4 import BeautifulSoup

# app = Flask(__name__)

response = requests.get("http://unkno.com/")

soup = BeautifulSoup(response.content, "html.parser")
facts = soup.find_all("div", id="content")

print(facts[0].getText())

# @app.route()


# def get_fact():

