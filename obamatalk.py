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

@app.route('/')
def home():
    fact = get_fact().strip()
    url = 'http://talkobamato.me/synthesize.py'

    data = {'input_text': fact }
    response = requests.post(url, data=data, allow_redirects=False)
    obama_url = response.headers['Location']

    return "<a href='{}'>{}</a>".format(obama_url, obama_url)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port, debug=True)

