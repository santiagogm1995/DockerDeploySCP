import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    os.system("git clone https://username:password@github.com/santiagogm1995/Trash.git")

    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
