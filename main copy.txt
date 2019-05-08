"""
A Mashup web app code to scrape a random fact from http://unkno.com. 
and send it to a pig latin web application running on Heroku: https://hidden-journey-62459.herokuapp.com, 
and print out the address for that piglatinized fact on the home page. 
"""
import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

# api-endpoint for piglatinize
URL = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'

# api-endpoint for facts
FACT_URL = 'http://unkno.com'

app = Flask(__name__)

def get_fact():
    """ 
    Retrieves a "fact" from the page: http://unkno.com/
    :return: fact
    """
    response = requests.get(FACT_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def get_url(fact):
    """
    Get the URL and display it on home page.
    to get the URL need to send a request to the Pig-Latin app with the text form data as the payload.
    The response to this will have the URL that we want to display as an HTTP Header, we also need to disable the redirect request/response.
    :params: fact
    :return: url location is the Response headers
    """

    response =  requests.post(URL, data={'input_text':fact}, allow_redirects=False)

    return response.headers['Location']


@app.route('/')
def home():
    fact = get_fact().strip()
    piglatinize_url = get_url(fact)

    return Response(response=piglatinize_url, mimetype="text/html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)

