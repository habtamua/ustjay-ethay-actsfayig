#Simple Time Server MicroService.
import os
import time
import calendar
from flask import Flask

app = Flask(__name__)
epoch_time = calendar.timegm(time.gmtime())

@app.route('/')
def get_epochTime():
    """Simple time microservice in Flask.
    return: the current Unix time or epoch time
    """
    
    return str(epoch_time)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port, debug=True)