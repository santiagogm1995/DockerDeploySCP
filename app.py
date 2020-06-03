import os
import configparser
from flask import Flask, request

cofig = configparser.ConfigParser()
cofig.read("prop.ini")
app = Flask(__name__)


@app.route("/")
def deploy():
    # os.system("git clone https://username:password@github.com/santiagogm1995/Trash.git")
    #env = request.args['env']
    #switcher = {
    #    "CF": deployCF(request),
    #    "Neo": deployNeo(request)
    #}

    #func = switcher.get(env, lambda: '{"code":"404","msg": "Environment not found"}');

    #content = func(request)
    content = deployCF(request)
    return content

def deployCF(request):

    
    user = cofig['DEFAULT']['USER']
    passwd = cofig['DEFAULT']['PASSWORD']

    os.system("git clone https://" + user + ":" + passwd + "@github.com/santiagogm1995/Trash.git")
    #os.chdir("dir")
    #os.system()
    #os.system("mbt ....")
    #os.system("cf ...")

    return "TEST OK"


def deployNeo(request):
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=8080)

