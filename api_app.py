#import os
from flask import Flask
from flask import redirect,url_for,render_template,jsonify
from flask import request
#import requests
#from datetime import datetime
#from ailink import *
#from getguess import *
import json
from app import *
#
apiAPP=Flask(___name__)
# #
#--------------------------------------------------------------------------#
#Function:  API_APP_Call()
#Calls:  
#function
#jsonString
#--------------------------------------------------------------------------#
@apiAPP.route("/app_call",methods=["GET"])
def API_APP_Call():
    dictGet=request.args
    dictAPP=json.loads(dictGet["jsonString"])
    #
    if(dictGet["function"]=="APP_home"):
        dictAPP=APP_home(dictAPP,dictGet["strInSession"])
    elif(dictGet["function"]=="APP_guess"):
        dictAPP=APP_guess(dictAPP,dictAPP["strInSession"],
                            dictAPP["strInWordGuess"],
                            dictAPP["strInUsername"])
    elif(dictGet["function"]=="APP_win"):
        dictAPP = APP_win(dictAPP,dictAPP["strInSession"],
                            dictAPP["strInWordGuess"],
                            dictAPP["strInUsername"])
    #
    jsonReturn=jsonify(dictAPP)
    return jsonReturn
#
if(__name__=="__main__"):
    apiAPP.run(Debug=True)
