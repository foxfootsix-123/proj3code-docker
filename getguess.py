#from scorekeep import *
#from ailink import *
import requests
import os
from flask import Flask
from flask import redirect,url_for,render_template,jsonify
from flask import request
#
#----------------------------------------------------------------------------#
#Function:  funcCheckGuess()
#----------------------------------------------------------------------------#
def funcCheckGuess(gdictGlobal,strInGuess,strInWord):
    strInGuess=strInGuess.upper()
    strInWord=strInWord.upper()
    nLenGuess=len(strInGuess)
    nLenWord=len(strInWord)
    nScore=0
    strScore=""
    for nLoop in range(0,nLenWord):
        if(nLoop<nLenGuess):
            if(strInWord[nLoop]==strInGuess[nLoop]):
                strScore=strScore+str("O")
                nScore=nScore+1
            else:
                strScore=strScore+str("X")
        else:
            strScore=strScore+str("?")
        if(gdictGlobal["bDebug"]!=False):
            print(f"funcCheckGuess()::{nLoop}:{strScore}:nS{nScore}:lenG{nLenGuess}:lenW{nLenGuess}")
#    nTemp=nScore+1
    if((nScore==nLenWord) and (nScore==nLenGuess)):
        if(gdictGlobal["bDebug"]!=False):
            print(f"win {nScore}:{nLenWord}:{nLenGuess}")
        strScore="*"
    else:
        if(gdictGlobal["bDebug"]!=False):
            print(f"lose {nScore}:{nLenWord}:{nLenGuess}")
    return strScore
#
#----------------------------------------------------------------------------#
#Function:  GETGUESS_getguess()
#----------------------------------------------------------------------------#
def GETGUESS_getguess(gdictGlobal,strGuess,strUsername):
    strGuess=strGuess.upper()
    strUsername=strUsername.upper()
 #
    #increment guess count
    nGuessCount=int(gdictGlobal["nGuessCount"])
    nGuessCount=nGuessCount+1  #increment guess count
    gdictGlobal["nGuessCount"]=int(nGuessCount)
#
    strCount=str(nGuessCount)  #Guess count string
    print(f"getguess():  guess count {strCount}")
    listGuess=gdictGlobal["listGuess"]
    listCheck=gdictGlobal["listCheck"]
#
#    dictAILINK=gdictGlobal["dictAILINK"]
    strHint= gdictGlobal["strGuessHint"]
    strCategory=gdictGlobal["strGuessCategory"]
    strLength=gdictGlobal["strLength"]
    strWinWord =gdictGlobal["strGuessWord"]
    print(f"getguess()::hint:{strHint} category:{strCategory} length:{strLength} winword:{strWinWord}")
#    listWords=gdictGlobal["listWords"]
#    nSelect=gdictGlobal["nWordSelect"]
#    listSep=listWords[nSelect].split(',')
#    print(f"Comma: {listSep[0]},{listSep[1]},{listSep[2]}")
#    strCategory=listSep[1]
#    strLength=len(listSep[2])
#    strWinWord=listSep[2]
    gdictGlobal["strWinWord"]=strWinWord
    nWinWordLen=len(strWinWord)
#
    strCheck=funcCheckGuess(gdictGlobal,strGuess,strWinWord)
    dictSCORE=SCOREKEEP_Open(gstrFILENAME_SCORE)
    if(strCheck != "*"):
#        print(f"Check:{strCheck}-G{strGuess}-W{strWinWord}")
#        print("Get guess.")
#
#    strTemp=strGuess+"["+strCheck+"]"
        strTemp=strGuess
        if(strGuess == ""):
            strTemp="[*empty*]"
        listGuess.append(strTemp)
        listCheck.append(strCheck)
#
        strContent="<TABLE>"
        nLines=len(listGuess)
        for nLoop in range(0,nLines):
            strGuess0=str(listGuess[nLoop])
            strCheck0=str(listCheck[nLoop])
            strContent=strContent+"<FONT SIZE=4><TR><TD>"+strGuess0+"</TD><TD>["+strCheck0+"]"+"</TD></TR></FONT>"
#            print(f"getguess()::strG{strGuess0}:strC{strCheck0}")
        strContent=strContent+"</TABLE>"
        #
        strTemp=f"getguess():WinWord={strWinWord} Guess={strGuess} Count={strCount}"
        print(f"getguess():{strTemp}")
        if(strGuess==""):
            strTemp="[*empty*]"
        else:
            strTemp=strGuess.upper()
        strCount0=strCount
        strHeader=f"<FONT SIZE=5>Guess my word.  <BR>Guess: {strTemp} --- Guess number: {strCount}</FONT><BR>"
        if(strUsername==""):
            strFooter=f"<FONT SIZE=5>Guess my word (AI version).</FONT><BR>"
        else:
            strFooter="<FONT SIZE=5>Guess my word (AI version), " + strUsername + ".</FONT><BR>"
#        strFooter="<FONT SIZE=5>Guess my word.</FONT><BR>"
        gdictGlobal["strHeader"]=strHeader
        gdictGlobal["strFooter"]=strFooter
        gdictGlobal["strContent"]=strContent
        strPOSTURL=gdictGlobal["strPOSTURL"]
#    if(strCheck!="*"):
        strHint = gdictGlobal["strGuessHint"]
        strCategory="Hint:  "+strHint+"<BR>"+f"<FONT SIZE=4>My word is a {strCategory} and has {strLength} letters.</FONT><BR>"
#        strCategory=strHint+f"<BR>My word is a {strCategory} and {strLength} letters long.<BR>"
        print(f"getdguess():{strCategory}")
#        strGuessCount=str(gdictGlobal["nGuessCount"])
#        print(f"getguess():  guess count {strCount}")
        nWordScore=""
        if(strUsername!=""):
#            dictSCORE=SCOREKEEP_Open(gstrFILENAME_SCORE)
            nWordScore=10*nWinWordLen-1*(nGuessCount)
            strWordScore=f"The word score is {nWordScore}."
            nLifeScore=gdictGlobal["nLifeScore"]
            nLifeScore=SCOREKEEP_GetScore(dictSCORE,strUsername)
            strLifeScore=f"<BR>{strUsername} has {nLifeScore} points."
            strGuessCount0=f"<FONT SIZE=4>There has been {strCount0} guess(es).  "+ strWordScore + strLifeScore + "</FONT><BR>"
#            SCOREKEEP_Close(dictSCORE)
        else:
            strGuessCount0=f"<FONT SIZE=4>There has been {strCount0} guess(es).</FONT><BR>"
#        print("getguess()::strCount:{strCount}")
        gdictGlobal["strCategory"]=strCategory
        gdictGlobal["strUsername"]=strUsername
        gdictGlobal["strCount"]=strGuessCount0
#        print(f"getguess():  guess count {strGuessCount0} {strCount}")
#        strReturn = render_template("wordfun.html",
#                                    htmlHeader0=strHeader,
#                                    htmlFooter0=strFooter,
#                                    htmlContentList0=strContent,
#                                    htmlPOSTURL=strPOSTURL,
#                                    htmlCount=strCount,
#                                    htmlCategory=strCategory)
#        strReturn = redirect(url_for("getguess",
#                                    htmlHeader0=strHeader,
#                                    htmlFooter0=strFooter,
#                                    htmlContentList0=strContent,
#                                    htmlPOSTURL=strPOSTURL))
#        strReturn=redirect("/",code=302)
#        print(f"{strReturn}")
    else:
        #Player guessed word.
        print(f"Check:{strCheck}")
        print("Player guessed word.")
        strWord0=strWinWord.upper()
        #increment word selection
        dictAILINK=dict()
        AILINK_Open(dictAILINK)
        strWord = AILINK_GetWord(dictAILINK)
        strHint = AILINK_GetHint(dictAILINK,strWord)
        gdictGlobal["dictAILINK"]=dictAILINK
        gdictGlobal["strGuessCategory"]=dictAILINK["strGuessCategory"]
        gdictGlobal["strGuessWord"]=dictAILINK["strGuessWord"]
        gdictGlobal["nGuessLength"]=dictAILINK["nGuessLength"]
        gdictGlobal["strGuessHint"]=dictAILINK["strGuessHint"]
        gdictGlobal["strLength"]=str(dictAILINK["nGuessLength"])
        gdictGlobal["strCategory"]=dictAILINK["strGuessCategory"]
        gdictGlobal["strWinWord"]=dictAILINK["strGuessWord"]
        strLength=gdictGlobal["strLength"]
        strCategory=gdictGlobal["strCategory"]
        strWinWord=gdictGlobal["strWinWord"]
        AILINK_Close(dictAILINK)
        dictAILINK.clear()
        dictAILINK=None
#        nSelect=gdictGlobal["nWordSelect"]
#        listWords=gdictGlobal["listWords"]
#        nWordLen=len(listWords)
#        nSelect=nSelect+1
#        if(nSelect>=nWordLen):
#            nSelect=0
#        gdictGlobal["nWordSelect"]=int(nSelect)
        #
#        strTemp=listWords[nSelect]
#        listSep=strTemp.split(",")
#        strWinWord=listSep[2]
#        strLength=str(len(listSep[2]))
#        strCategory=listSep[1]
#        print(f"getguess()::strNew{strWinWord} and select {nSelect}:{strLength}:{strCategory}")
#
        strWinWord=gdictGlobal["strWinWord"]
        gdictGlobal["strLength"]=strLength
        gdictGlobal["strCategory"]=strCategory
        strLifeScore=""
        if(strUsername!=""):
            nWordScore=10*nWinWordLen-1*(nGuessCount)
            strWordScore=f"The word score is {nWordScore}."
            dictSCORE["strUsername"]=""
            dictSCORE["strScore"]=""
            nLifeScore=SCOREKEEP_AddScore(dictSCORE,strUsername,nWordScore)
            strUsername=dictSCORE["strUsername"]
            nWordScore=int(dictSCORE["strScore"])
            gdictGlobal["nLifeScore"]=nLifeScore
            strLifeScore=f"<BR>{strUsername} has {nLifeScore} points."
#            strCount="<FONT SIZE=4>There has been "+strCount+f" guess(es).  "+ strWordScore + strLifeScore + "</FONT><BR>"
        strCount="<FONT SIZE=4>I have selected a new word.  Guess my word."+ strLifeScore +"</FONT><BR>"
        strLength=gdictGlobal["strLength"]
        strCategory="Hint (AI generated):  "+strHint+"<BR>"+f"<FONT SIZE=4>My word is a {strCategory} and has {strLength} letters.</FONT><BR>"
#        strCategory=strHint+f"My word is a {strCategory} with {strLength} letters.<BR>"
        gdictGlobal["strCount"]=strCount
        strGuessCount=str(gdictGlobal["nGuessCount"])
        strHeader=f"<FONT size=5>You guessed my word in {strGuessCount} tries/try.  My AI word is {strWord0}.</FONT><BR>"
        if(strUsername==""):
            strFooter=f"<FONT size=5>Guess My Word (AI version).</FONT><BR>"
        else:
            strFooter=f"<FONT size=5>Guess My Word (AI version), " + strUsername + ".</FONT><BR>"
        print(f"getguess()::strF{strFooter}")
        listGuess.append(strGuess)
        listCheck.append(strCheck)
        strContent="<TABLE>"
        nLines=len(listGuess)
        for nLoop in range(0,nLines):
            strGuess0=str(listGuess[nLoop])
            strCheck0=str(listCheck[nLoop])
            strContent=strContent+"<FONT SIZE=4><TR><TD>"+strGuess0+"</TD><TD>["+strCheck0+"]"+"</TD></TR></FONT>"
        strContent=strContent+"</TABLE>"
#        strContent="strContent<BR>"
        strTemp=strGuess.upper()
#        strHeader=f"<FONT SIZE=5>Guess my word.  <BR>Guess: {strTemp} --- Guess number: {strGuessCount}</FONT><BR>"
#        strFooter=f"<FONT SIZE=5>Guess my word {strWinWord}.</FONT><BR>"
        gdictGlobal["strCategory"]=strCategory
        gdictGlobal["strHeader"]=strHeader
        gdictGlobal["strFooter"]=strFooter
        gdictGlobal["strContent"]=strContent
        strPOSTURL=gdictGlobal["strPOSTURL"]
        gdictGlobal["strUsername"]=strUsername
        gdictGlobal["nGuessCount"]=0
        listGuess=gdictGlobal["listGuess"]
        listGuess.clear()
        listGuess=[]
        gdictGlobal["listGuess"]=listGuess
        listCheck=gdictGlobal["listCheck"]
        listCheck.clear()
        listCheck=[]
        gdictGlobal["listCheck"]=listCheck
#        strReturn=redirect("/",code=302)
    SCOREKEEP_Close(dictSCORE)
    strReturn = render_template("wordfun.html",
                                htmlHeader0=strHeader,
                                htmlFooter0=strFooter,
                                htmlContentList0=strContent,
                                htmlPOSTURL=strPOSTURL,
                                htmlCount=strCount,
                                htmlCategory=strCategory,
                                htmlUsername=strUsername)
#    strReturn=redirect("/",code=302)
    print("getguess():Exit")
    return strReturn
#
#----------------------------------------------------------------------------#
#Function:  GETGUESS_home()
#----------------------------------------------------------------------------#
def GETGUESS_home(gdictGlobal):
    strUsername=gdictGlobal["strUsername"]
    print(f"home():Enter user{strUsername}")
    strCategory=gdictGlobal["strCategory"]
    strHeader=gdictGlobal["strHeader"]
    strFooter=gdictGlobal["strFooter"]
    strContent=gdictGlobal["strContent"]
    strPOSTURL=gdictGlobal["strPOSTURL"]
    strCount=gdictGlobal["strCount"]
    strCategory=gdictGlobal["strCategory"]
    strReturn = render_template("wordfun.html",
                                htmlHeader0=strHeader,
                                htmlFooter0=strFooter,
                                htmlContentList0=strContent,
                                htmlPOSTURL=strPOSTURL,
                                htmlCount=strCount,
                                htmlCategory=strCategory,
                                htmlUsername=strUsername)
    print("home():Exit")
    return strReturn
#
#----------------------------------------------------------------------------#
#Function:  GETGUESS_formpost()
#----------------------------------------------------------------------------#
def GETGUESS_formpost(gdictGlobal,strGuess,strUsername):
    dictParams=dict()
    dictParams["wordguess"]=strGuess.strip()
    dictParams["username"]=strUsername.strip()
    requests.get(url="http://phanes.pythonanywhere.com/getguess",params=dictParams)
#    requests.get(url="http://127.0.0.1:5000/getguess",params=dictParams)
#    strReturn="FORMPOST<BR>"
#    strReturn=redirect(())
    print("formpost():Exit")
    return
