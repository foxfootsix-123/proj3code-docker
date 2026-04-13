import time
import os
from flask import Flask
from flask import redirect,url_for,render_template,jsonify
from flask import request
from openai import OpenAI
import requests
import json
from ailink import *
#
apiAILINK=Flask(__name__)
#
#--------------------------------------------------------------------------#
#Function:  API_AILINK_Call()
#--------------------------------------------------------------------------#
@apiAILINK.route("/ailink_call",methods=["GET"])
def API_AILINK_Call():
    dictGet=request.args
    dictAILINK=json.loads(dictGet["jsonString"])
    #
    if(dictGet["function"]=="AILINK_Open"):
        AILINK_Open(dictAILINK)
    elif(dictGet["function"]=="AILINK_GetWord"):    
        dictAILINK["strAIWord"]=AILINK_GetWord(dictAILINK)
        dictAILINK["strAICategory"]=dictAILINK["strGuessCategory"]
        dictAILINK["strAILength"]=str(dictAILINK["nGuessLength"])
    elif(dictGet["function"]=="AILINK_GetHint"):
        dictAILINK["strAIHint"]=AILINK_GetHint(dictAILINK,dictAILINK["strAIWord"])
        dictAILINK["strAICategory"]=dictAILINK["strGuessCategory"]
        dictAILINK["strAILength"]=str(dictAILINK["nGuessLength"])
    elif(dictGet["function"]=="AILINK_Close"):
        AILINK_Close(dictAILINK)
    #
    jsonReturn=jsonify(dictAILINK)
    return jsonReturn
#
#--------------------------------------------------------------------------#
#Function:  API_AILINK_main()
#--------------------------------------------------------------------------#
@apiAILINK.route("/ailink_main")
def API_AILINK_main():
    paramIn=dict()
    paramIn["key1"]="value1"
    paramIn["key2"]="value2"
#    responseOut=requests.get(url="http://127.0.0.1:5000/ailink_test",params=paramIn)
#    responseOut.json()
#    return responseOut
#    paramIn.json()
    return paramIn

#API_AILINK_main()
if(__name__=="__main__"):
    apiAILINK.run(debug=True)
