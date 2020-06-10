import os
import configparser
import logging
from error import ManagerException
from flask import Flask, request

cofig = configparser.ConfigParser()
cofig.read("prop.ini")
logging.basicConfig(filename="logFile.log", level=logging.INFO)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def swagger():
    swagger = open("swagger.json", "r")

    return swagger.read()

@app.route("/logs", methods=["GET"])
def getLogs():
    logsFile = open("logFile.log", "r")

    return logsFile.read()

@app.route("/deploy",methods=['POST','GET'])
def deploy(): 
    env = request.args['env']

    switcher = { 
        "CF": deployCF,
        "Neo": deployNeo
    }

    func = switcher.get(env, lambda: '{"code":"404","msg": "Environment not found"}')

    print(func)

    content = func()


    return content

def deployCF():

    #Authentication
    userGit = cofig['DEFAULT']['USER']
    passwd = cofig['DEFAULT']['PASSWORD']

    msg = "Correct"
    exit = '{"code":"200","msg": ' + msg + }'

    try:
        
        if user is None:
            raise Error('User not found')

        if nameApp is None:
            raise Error('Name app not found')

    except Error:
        pass
    


    logging.info('Create folder --> ' + "apps/" + user + "/" + nameApp)
    os.system("mkdir -p apps/" + user + "/" + nameApp)

    logging.info('Cloning repository from --> ' +  "https://" + userGit + ":" + passwd + "@github.com/santiagogm1995/" + nameApp + ".git ")
    os.system("git clone https://" + userGit + ":" + passwd + "@github.com/santiagogm1995/" + nameApp + ".git apps/" + user + "/" + nameApp + "/.")

    logging.info()
    #os.chdir("dir")
    #os.system()
    #os.system("mbt ....")
    #os.system("cf ...")

    os.system("rm -rf apps/" + user + "/*")

    return exit

def deployNeo():
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=8080)

