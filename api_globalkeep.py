from flask import Flask
from flask import redirect,url_for,render_template,jsonify
from flask import request
import requests
from datetime import datetime
import json
from globalkeep import *
#
apiGLOBALKEEP=Flask(__name__)
#
#--------------------------------------------------------------------------#
#Function:  API_GLOBALKEEP_Call()
#Calls:  
#function
#jsonString
#--------------------------------------------------------------------------#
@apiGLOBALKEEP.route("/globalkeep_call",methods=["GET"])
def API_GLOBALKEEP_Call():
    dictGet=request.args
    dictGLOBALKEEP=json.loads(dictGet["jsonString"])
    #
    if(dictGet["function"]=="GLOBALKEEP_Constants"):
        dictGLOBALKEEP=GLOBALKEEP_Constants(dictGLOBALKEEP)
    elif(dictGet["function"]=="GLOBALKEEP_Init"):
        dictGLOBALKEEP=GLOBALKEEP_Init(dictGLOBALKEEP)
    elif(dictGet["function"]=="GLOBALKEEP_GetNewSessionID"):
        nError = GLOBALKEEP_GetNewSessionID(dictGLOBALKEEP,
                                                dictGet["strInFilename"])
    elif(dictGet["function"]=="GLOBALKEEP_SessionRead"):
        nError = GLOBALKEEP_SessionRead(dictGLOBALKEEP,
                                            dictGet["strSession"])
    elif(dictGet["function"]=="GLOBALKEEP_SessionWrite"):
        nError = GLOBALKEEP_SessionWrite(dictGLOBALKEEP,
                                            dictGet["strSession"])
    elif(dictGet["function"]=="GLOBALKEEP_ResetFile"):
        strFileSave=GLOBALKEEP_ResetFile(dictGLOBALKEEP)
    elif(dictGet["function"]=="GLOBALKEEP_Close"):
        strFileSave=GLOBALKEEP_Close(dictGLOBALKEEP)
    #
    jsonReturn=jsonify(dictGLOBALKEEP)
    return jsonReturn
#
if(__name__=="__main__"):
    apiGLOBALKEEP.run(Debug=True,port=5050)
