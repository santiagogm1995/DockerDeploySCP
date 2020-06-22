import os
import configparser
import logging
from error import ManagerException
from flask import Flask, request

cofig = configparser.ConfigParser()
cofig.read("prop.ini")
logging.basicConfig(filename="logFile.log", level=logging.INFO, format='%(levelname)s :[%(asctime)s] --> %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

msg = {
    1 : '{"code":"200","msg": "OK"}',
    2 : '{"code":"404","msg": "Environment not found"}'
}


app = Flask(__name__)

@app.route("/", methods=['GET'])
def swagger():
    swagger = open("swagger.json", "r")

    return swagger.read()

@app.route("/logs", methods=["GET"])
def getLogs():
    logsFile = open("logFile.log", "r")

    return logsFile.read()

@app.route("/deploy",methods=['GET'])
def deploy(): 
    env = request.args['env']

    switcher = {
        "CF": deployCF,
        "Neo": deployNeo
    }

    func = switcher.get(env, lambda: msg.get(2))

    content = func()

    return content

def deployCF():

    exit = msg.get(1)

    #Authentication GitHub
    userGit = cofig['DEFAULT']['USER']
    passwd = cofig['DEFAULT']['PASSWORD']

    user = request.args.get('user', None)
    project = request.args.get('project',None)

    logging.info("Check all parameters required")
    try:
        if user is None:
            raise ManagerException('400', 'PARAMETER "user" is required')

        if project is None:
            raise ManagerException('400', 'PARAMETER "project" is required')
    
    except ManagerException as e:
        logging.error(e.msg)
        exit = ManagerException.getError(1,"400",e.msg)
        return exit
    
    logging.info('Create folder --> ' + "apps/" + user + "/" + project)
    os.system("mkdir -p apps/" + user + "/" + project)

    logging.info('Cloning repository from --> ' +  "https://" + userGit + ":" + passwd + "@github.com/santiagogm1995/" + project + ".git ")
    os.system("git clone https://" + userGit + ":" + passwd + "@github.com/santiagogm1995/" + project + ".git apps/" + user + "/" + project + "/.")
    logging.info('Finish cloning repository')

    logging.info('Build MTA from Source')
    os.chdir('apps/' + user + '/' + project)
    os.system('mbt build')
    logging.info('Finish build MTA')
    #os.system("cf ...")

    os.system("rm -rf apps/" + user + "/*")

    print(exit)
    return exit

def deployNeo():
    return ""


if __name__ == "__main__":
    app.run(host="0.0.0.0" ,port=8080)

