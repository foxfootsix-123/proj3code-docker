import os
from flask import Flask
from flask import redirect,url_for,render_template,jsonify
from flask import request
import requests
from datetime import datetime
#from ailink import *
#from getguess import *
#
#----------------------------------------------------------------------------#
#Function:  APP_before()
#----------------------------------------------------------------------------# 
def APP_before(dictIn):
    return dictIn
#
#----------------------------------------------------------------------------#
#Function:  APP_after()
#----------------------------------------------------------------------------# 
def APP_after(dictIn):
    return dictIn
#
#----------------------------------------------------------------------------#
#Function:  APP_home()
#----------------------------------------------------------------------------# 
def APP_home(dictHome,strInSession):
    dictHome["htmlHeader"]="*Guess My AI Word.*<BR>Can you guess my AI word?<BR>"
    dictHome["htmlFooter"]="Guess My AI Word.  Can you guess my AI word?<BR>"
    dictHome["htmlFooter"]=dictHome["htmlFooter"]+"<FONT SIZE=3>CS540 Project 3 microservices game created by Ke and Dandan.</FONT>"
    dictHome["htmlContent"]="Can you guess my AI word?"
    dictHome["htmlHint"]="AI Hint:  "+dictHome["strAIHint"]
    dictHome["htmlInfo"]=f"My word is a {dictHome["strAICategory"]} and has {dictHome["strAILength"]} letters."
#    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
    if(dictHome["IsLocal"]!="No"):
       strForm="<FORM action='http://localhost:5000/formpost' method='get'>"
    else:
       strForm="<FORM action='https://phanes.pythonanywhere.com/formpost' method='get'>"
    strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
    strForm=strForm+"<input type='submit' value='Send'/><BR>"
    strForm=strForm+"---<BR>"
    strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
    strForm=strForm+"Name (save a score):  <input type='text' name='username' value=''/><BR>"
    strForm=strForm+"</FORM>"
    dictHome["htmlForm"]=strForm
    return dictHome
#
#----------------------------------------------------------------------------#
#Function:  APP_guess()
#----------------------------------------------------------------------------# 
def APP_guess(dictDraw,strInSession,strInWordGuess,strInUsername):
    dictDraw["htmlHeader"]="*Guess My AI Word.*<BR>Can you guess my AI word?<BR>  You guessed "+dictDraw["strWordGuess"]+"."
    if(strInUsername==""):
        dictDraw["htmlFooter"]="Guess My AI Word.  Can you guess my AI word?<BR>"
        dictDraw["htmlFooter"]=dictDraw["htmlFooter"]+"<FONT SIZE=3>CS540 Project 3 microservices game created by Ke and Dandan.</FONT>"
    else:
        dictDraw["htmlFooter"]="*Guess My AI Word, "+strInUsername+"*<BR>"
        dictDraw["htmlFooter"]=dictDraw["htmlFooter"]+"<FONT SIZE=3>CS540 Project 3 microservices game created by Ke and Dandan.</FONT>"
#
    dictDraw["htmlContent"]=""
    listChecks=dictDraw["listChecks"]
    listWords=dictDraw["listWords"]
    nCount=len(listWords)
    nLoop=0
    while(nLoop<nCount):
        strWord=listWords[nLoop]
        strCheck=listChecks[nLoop]
#        strWord=GLOBALKEEP_TrimString(strWord)
        if(strWord!=""):
            dictDraw["htmlContent"]=dictDraw["htmlContent"]+strWord+"  ["+strCheck+"]<BR>"
        else:
            dictDraw["htmlContent"]=dictDraw["htmlContent"]+"[*empty*]"+"  ["+strCheck+"]<BR>"            
        nLoop=nLoop+1
#
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"The guess was "+dictDraw["strWordGuess"]+"."
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Guess Count: "+dictDraw["strGuessCount"]+"<BR>"
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Total score: "+dictDraw["strScorekeep"]+"<BR>"
#
    dictDraw["htmlHint"]="AI Hint:  "+dictDraw["strAIHint"]
    dictDraw["htmlInfo"]=f"My AI word is a {dictDraw["strAICategory"]} and has {dictDraw["strAILength"]} letters."
#    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
    if(dictDraw["IsLocal"]!="No"):
       strForm="<FORM action='http://localhost:5000/formpost' method='get'>"
    else:
       strForm="<FORM action='https://phanes.pythonanywhere.com/formpost' method='get'>"
    strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
    strForm=strForm+"<input type='submit' value='Send'/><BR>"
    strForm=strForm+"---<BR>"
    strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
    strForm=strForm+"Name (save a score):  <input type='text' name='username' value='"+strInUsername+"'/><BR>"
    strForm=strForm+"</FORM>"
    dictDraw["htmlForm"]=strForm
    return dictDraw
#
#----------------------------------------------------------------------------#
#Function:  APP_win()
#----------------------------------------------------------------------------# 
def APP_win(dictDraw,strInSession,strInWordGuess,strInUsername):
    dictDraw["htmlHeader"]="*Guess My AI Word.*<BR>You have guessed my AI word.<BR>  You guessed "+dictDraw["strWordGuess"]+"."
    if(strInUsername==""):
        dictDraw["htmlFooter"]="Guess My AI Word.  You have guessed my AI word.<BR>"
        dictDraw["htmlFooter"]=dictDraw["htmlFooter"]+"<FONT SIZE=3>CS540 Project 3 microservices game created by Ke and Dandan.</FONT>"
    else:
        dictDraw["htmlFooter"]="*Guess My AI Word, "+strInUsername+"* You have guessed my AI word.<BR>"
        dictDraw["htmlFooter"]=dictDraw["htmlFooter"]+"<FONT SIZE=3>CS540 Project 3 microservices game created by Ke and Dandan.</FONT>"
#
    dictDraw["htmlContent"]=""
    listChecks=dictDraw["listChecks"]
    listWords=dictDraw["listWords"]
    nCount=len(listWords)
    nLoop=0
    while(nLoop<nCount):
        strWord=listWords[nLoop]
        strCheck=listChecks[nLoop]
#        strWord=GLOBALKEEP_TrimString(strWord)
        if(strWord!=""):
            dictDraw["htmlContent"]=dictDraw["htmlContent"]+strWord+"  ["+strCheck+"]<BR>"
        else:
            dictDraw["htmlContent"]=dictDraw["htmlContent"]+"[*empty*]"+"  ["+strCheck+"]<BR>"            
        nLoop=nLoop+1
#
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"You guessed my AI word -"+dictDraw["strWordGuess"]+"-."
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Guess Count: "+dictDraw["strGuessCount"]+"<BR>"
    dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Total score: "+dictDraw["strScorekeep"]+"<BR>"
#
    dictDraw["htmlHint"]="New AI Hint:  "+dictDraw["strAIHint"]
    dictDraw["htmlInfo"]=f"I have a new AI word.  It is a {dictDraw["strAICategory"]} and has {dictDraw["strAILength"]} letters."
#    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
    if(dictDraw["IsLocal"]!="No"):
       strForm="<FORM action='http://localhost:5000/formpost' method='get'>"
    else:
       strForm="<FORM action='https://phanes.pythonanywhere.com/formpost' method='get'>"
    strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
    strForm=strForm+"<input type='submit' value='Send'/><BR>"
    strForm=strForm+"---<BR>"
    strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
    strForm=strForm+"Name (save a score):  <input type='text' name='username' value='"+strInUsername.upper()+"'/><BR>"
    strForm=strForm+"</FORM>"
    dictDraw["htmlForm"]=strForm
    return dictDraw
