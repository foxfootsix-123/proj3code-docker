#from getguess import *
#from scorekeep import *
import os
from flask import Flask
from flask import redirect,url_for,render_template,jsonify
#from werkzeug.datastructures import MultiDict
from flask import request
import requests
from datetime import datetime
from ailink import *
from getguess import *
from globalkeep import *
from app import *
#
app = Flask(__name__,
            template_folder="template",
            static_folder="assets")
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_Constants()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_Constants(dictIn):
#     dictIn["strDelim"]="="
#     dictIn["strDot"]="."
#     dictIn["strBackSlash"]=chr(92)  #\\
#     dictIn["strCR"]=chr(13)
#     dictIn["strLF"]=chr(10)
#     dictIn["strFilename"]=""
# #    dictIn["IsLocal"]="Yes"
#     dictIn["fileGLOBAL"]=None
# #    dictGLOBAL=dict()
#     return dictIn
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_Init()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_Init(dictIn):
# #    dictIn["strDelim"]="="
# #    dictIn["strDot"]="."
# #    dictIn["strBackSlash"]=chr(92)  #\\
# #   dictIn["strCR"]=chr(13)
# #   dictIn["strLF"]=chr(10)
# #   dictIn["strFilename"]=""
# #   dictIn["IsLocal"]="No"
# #   dictIn["fileGLOBAL"]=None
# #    dictGLOBAL=dict()
#     dictIn["bDebug"]=False
#     dictIn["IsLocal"]="Yes"
#     dictIn["strFileSave"]=None
#     dictIn["strWordGuess"]=""
#     dictIn["strGuessCount"]=str(0)
#     listWords=[]
#     dictIn["listWords"]=listWords
#     listChecks=[]
#     dictIn["listChecks"]=listChecks
#     return dictIn
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_TrimString()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_TrimString(strInString):
#     strOutString=""
#     nCount=len(strInString)
#     nLoop=0
#     while(nLoop<nCount):
#         strChar=strInString[nLoop:nLoop+1]
#         if((strChar>="A") and (strChar<="Z")):
#             strOutString=strOutString+strChar
#         if((strChar>="a") and (strChar<="z")):
#             strOutString=strOutString+strChar
#         if((strChar>="0") and (strChar<="9")):
#             strOutString=strOutString+strChar
#         if(strChar==" "):
#             strOutString=strOutString+strChar
#         nLoop=nLoop+1
#     return strOutString#
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_ParseLine()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_ParseLine(dictIn,strIn):
#     GLOBALKEEP_Constants(dictIn)
#     IsValue=False        
#     strOutKey=""
#     strOutValue=""
#     nCount=len(strIn)
#     nLoop=0
#     while(nLoop<nCount):
#         strChar=strIn[(nLoop):(nLoop+1)]
#         if(IsValue==False):
#             #key string
#             if(strChar!=(dictIn["strDelim"])):
#                 strOutKey=strOutKey+strChar
#             else:
#                 IsValue=True
#         else:
#             #value string
#             strOutValue=strOutValue+strChar
#         nLoop=nLoop+1
#     listOut=[]
#     listOut.append(strOutKey)
#     listOut.append(strOutValue)
#     return listOut
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_SessionRead()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_SessionRead(dictIn,strInSession):
#     GLOBALKEEP_Constants(dictIn)
#     nError=0
# #    dictIn.clear()
#     fileGLOBAL=open(strInSession,mode="rt",encoding="utf8")
#     dictIn["strSession"]=strInSession
#     print(f"GLOBALKEEP_SessionRead():filesave {dictIn["strFileSave"]}")
#     strLine=fileGLOBAL.readline()
#     while strLine:
#         listParse=GLOBALKEEP_ParseLine(dictIn,strLine)
#         strKey=listParse[0].strip()
#         strValue=listParse[1].strip()
#         if(strValue[0:1]=="["):
#             listTemp=[]
#             nLen=len(strValue)
#             strValue0=strValue[1:(nLen-1)]
# #
#             strSplit=""
#             nCount=len(strValue0)
#             nLoop=0
#             while(nLoop<nCount):
#                 strChar=strValue0[nLoop:(nLoop+1)]
#                 if(strChar==","):
#                     strSplit=GLOBALKEEP_TrimString(strSplit)
#                     listTemp.append(strSplit)
#                     strSplit=""
#                 else:
#                     strSplit=strSplit+strChar
#                 nLoop=nLoop+1
#             nCount=len(strSplit)
#             if(nCount != 0):
#                 listTemp.append(strSplit)
#             dictIn[strKey]=listTemp
#         else:
#             dictIn[strKey]=strValue
#         strLine=fileGLOBAL.readline()
#     fileGLOBAL.close()
#     fileGLOBAL=None
#     return nError
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_Read()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_Read(dictIn):
#     GLOBALKEEP_Constants(dictIn)
#     nError=0
#     dictIn.clear()
#     strLine=dictIn.fileGLOBAL.readline()
#     while strLine:
#         strKey=""
#         strValue=""
#         nError=GLOBALKEEP_ParseLine(strLine,strKey,strValue)
#         strKey=strKey.strip()
#         strValue=strValue.strip()
#         dictIn[strKey]=strValue
#         strLine=dictIn.fileGLOBAL.readline()
# #        dictIn=self.dictGLOBAL
#     return nError
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_SessionWrite()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_SessionWrite(dictIn,strInSession):
#     GLOBALKEEP_Constants(dictIn)
# #    dictIn["strFileSave"]=strInSession
# #    fileGLOBAL=open(dictIn["strFileSave"],mode="wt",encoding="utf8")
#     fileGLOBAL=open(strInSession,mode="wt",encoding="utf8")
#     nError=0
#     listLine=[]
#     for strKey in dictIn.keys():
#         strValue=str(dictIn[strKey])
#         if(strValue[0:1]=="["):
#             listTemp=dictIn[strKey]
#             strTemp=str(listTemp)
#             strLine=strKey+dictIn["strDelim"]+strTemp+dictIn["strLF"]
#             listLine.append(strLine)
#         else:
#             strLine=strKey+(dictIn["strDelim"])+strValue+dictIn["strLF"]
#             listLine.append(strLine)
#     fileGLOBAL.writelines(listLine)        
# #    dictIn["strFileSave"] = strInSession
#     print(f"GLOBALKEEP_SessionWrite():filesave {dictIn["strFileSave"]}")
#     fileGLOBAL.close()
#     fileGLOBAL=None
#     return nError
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_Write()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_Write(dictIn):
#     GLOBALKEEP_Constants(dictIn)
#     nError=0
#     listLine=[]
#     for strKey in dictIn.keys():
#         strValue=str(dictIn[strKey])
#         strLine=strKey+(dictIn.strDelim)+strValue  #+self.strCR+self.strLF
#         listLine.append(strLine)
#     dictIn["strFileSave"].fileGLOBAL.writelines(listLine)        
#     return nError
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_GetTimestamp()
# #Note:  YYYYMMDD-HHMMSS-sss
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_GetTimestamp(dictIn):
#     GLOBALKEEP_Constants(dictIn)
#     dtNow=datetime.now()
#     strDate=f"{dtNow.year:04}"
#     strDate=strDate+f"{dtNow.month:02}"
#     strDate=strDate+f"{dtNow.day:02}"
#     strTime=f"{dtNow.hour:02}"
#     strTime=strTime+f"{dtNow.minute:02}"
#     strTime=strTime+f"{dtNow.second:02}"
#     strMicro=f"{dtNow.microsecond:03}"
#     strTimestamp=strDate+"-"+strTime+"-"+strMicro
#     return strTimestamp
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_BuildDirFile()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_BuildDirFile(dictIn,nCount,listDir,listFile):
#     GLOBALKEEP_Constants(dictIn)
#     strOut=""
#     nItems=len(listDir)
#     if(nItems>1):
#         for strTemp in listDir:
#             strOut=strOut+strTemp+dictIn.strBackSlash
#     nItems=len(listFile)
#     nItems=nItems-1
#     strTimestamp = GLOBALKEEP_GetTimestamp(dictIn)
#     strCount="."+strTimestamp+f"-{nCount:05}"+"."+listFile[nItems]
#     nLoop=0
#     while(nLoop<nItems):
#         strOut=strOut+listFile[nLoop]
#         nLoop=nLoop+1
#     strDirFile=strOut+strCount
#     return strDirFile
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_GetNewSessionID()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_GetNewSessionID(dictIn,strInFilename):
#     listDir=strInFilename.split("\\")
#     nDirItems=len(listDir)
#     nDirItems=nDirItems-1
# #    if(nDirItems<2):

# #
#     strFile=listDir[nDirItems]
#     listSplit=strFile.split(".")
#     nItems=len(listSplit)
#     if(nItems<2):
#         #no file extension
#         listSplit.append("txt")
#         nItems=len(listSplit)
#         nItems=nItems-1    
#     nLoop=0
#     dictGLOBAL=dict()
#     strDirFile=GLOBALKEEP_BuildDirFile(dictGLOBAL,nLoop,listDir,listSplit)
#     bExists=os.path.exists(strDirFile)
#     while(bExists!=False):
#         nLoop=nLoop+1
#         strDirFile=GLOBALKEEP_BuildDirFile(dictGLOBAL,nLoop,listDir,listSplit)
#         bExists=os.path.exists(strDirFile)
#     strSessionID=strDirFile
#     print(f"GLOBALKEEP_GetNewSessionID():fsave{strDirFile}")
#     dictGLOBAL.clear()
#     dictGLOBAL=None
#     dictIn["strSessionID"]=strSessionID
#     return strSessionID
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_ReadOpen()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_ReadOpen(dictIn,strInFilename):
#     GLOBALKEEP_Constants(dictIn)
#     if((dictIn.strFileSave==None)):
#         #no file id
#         listDir=strInFilename.split("\\")
#         nDirItems=len(listDir)
#         nDirItems=nDirItems-1
# #
#         strFile=listDir[nDirItems]
#         listSplit=strFile.split(".")
#         nItems=len(listSplit)
#         nItems=nItems-1    
#         if(nItems<=0):
#             #no file extension
#             listSplit.append("txt")
#             nItems=len(listSplit)
#         nLoop=0
#         strDirFile=dictIn.GLOBALKEEP_BuildDirFile(nLoop,listDir,listSplit)
#         bExists=os.path.exists(strDirFile)
#         while(bExists!=False):
#             nLoop=nLoop+1
#             strDirFile=GLOBALKEEP_BuildDirFile(nLoop,listDir,listSplit)
#             bExists=os.path.exists(strDirFile)
#         dictIn.strFileSave=strDirFile
#         print(f"GLOBALKEEP_ReadOpen():fsave{strDirFile}")
#     else:
#         #file id
#         print(f"GLOBALKEEP_ReadOpen():filesave{dictIn.strFileSave}")
#     dictIn.fileGLOBAL=open((dictIn.strFileSave),mode="rt",encoding="utf8")
#     return dictIn.strFileSave
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_WriteOpen()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_WriteOpen(dictIn,strInFilename):
#     GLOBALKEEP_Constants(dictIn)
#     if((dictIn.strFileSave==None)):
#         #no file id
#         listDir=strInFilename.split("\\")
#         nDirItems=len(listDir)
#         nDirItems=nDirItems-1
# #
#         strFile=listDir[nDirItems]
#         listSplit=strFile.split(".")
#         nItems=len(listSplit)
#         if(nItems<=0):
#             #no file extension
#             listSplit.append("txt")
#             nItems=len(listSplit)
#         nItems=nItems-1    
#         nLoop=0
#         strDirFile=dictIn.GLOBALKEEP_BuildDirFile(nLoop,listDir,listSplit)
#         bExists=os.path.exists(strDirFile)
#         while(bExists!=False):
#             nLoop=nLoop+1
#             strDirFile=dictIn.GLOBALKEEP_BuildDirFile(nLoop,listDir,listSplit)
#             bExists=os.path.exists(strDirFile)
#         dictIn.strFileSave=strDirFile
#         print(f"GLOBALKEEP_WriteOpen():fsave{strDirFile}")
#     else:
#         #file id
#         print(f"GLOBALKEEP_WriteOpen():filesave{dictIn.strFileSave}")
#     dictIn.fileGLOBAL=open((dictIn.strFileSave),mode="wt",encoding="utf8")
#     return dictIn.strFileSave
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_ResetFile()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_ResetFile(dictIn):
#     GLOBALKEEP_Constants(dictIn)
#     dictIn.strFileSave==None
#     return dictIn.strFileSave
# #
# #----------------------------------------------------------------------------#
# #Function:  GLOBALKEEP_Close()
# #----------------------------------------------------------------------------#
# def GLOBALKEEP_Close(dictIn):
#     GLOBALKEEP_Constants(dictIn)
#     dictIn.dictGLOBAL.clear()
#     dictIn.fileGLOBAL.close()
#     dictIn.fileGLOBAL=None
# #    self.strFileSave=None
#     return dictIn
# #
# #----------------------------------------------------------------------------#
# #Function:  APP_before()
# #----------------------------------------------------------------------------# 
# def APP_before(dictIn):
#     return dictIn
# #
# #----------------------------------------------------------------------------#
# #Function:  APP_after()
# #----------------------------------------------------------------------------# 
# def APP_after(dictIn):
#     return dictIn
# #
# #----------------------------------------------------------------------------#
# #Function:  APP_home()
# #----------------------------------------------------------------------------# 
# def APP_home(dictHome,strInSession):
#     dictHome["htmlHeader"]="*Guess My Word.*<BR>Can you guess my word?<BR>"
#     dictHome["htmlFooter"]="Guess My Word.  Can you guess my word?<BR>"
#     dictHome["htmlContent"]="Can you guess my word?"
#     dictHome["htmlHint"]="Hint:  "+dictHome["strAIHint"]
#     dictHome["htmlInfo"]=f"My word is a {dictHome["strAICategory"]} and has {dictHome["strAILength"]} letters."
# #    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     if(dictHome["IsLocal"]!="No"):
#        strForm="<FORM action='http://127.0.0.1:5000/formpost' method='get'>"
#     else:
#        strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
#     strForm=strForm+"<input type='submit' value='Send'/><BR>"
#     strForm=strForm+"---<BR>"
#     strForm=strForm+"Name (save a score):  <input type='text' name='username' value=''/><BR>"
#     strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
#     strForm=strForm+"</FORM>"
#     dictHome["htmlForm"]=strForm
#     return dictHome
# #
# #----------------------------------------------------------------------------#
# #Function:  APP_guess()
# #----------------------------------------------------------------------------# 
# def APP_guess(dictDraw,strInSession,strInWordGuess,strInUsername):
#     dictDraw["htmlHeader"]="*Guess My Word.*<BR>Can you guess my word?<BR>  You guessed "+dictDraw["strWordGuess"]+"."
#     if(strInUsername==""):
#         dictDraw["htmlFooter"]="Guess My Word.  Can you guess my word?<BR>"
#     else:
#         dictDraw["htmlFooter"]="*Guess My Word, "+strInUsername+"*<BR>"
# #
#     dictDraw["htmlContent"]=""
#     listChecks=dictDraw["listChecks"]
#     listWords=dictDraw["listWords"]
#     nCount=len(listWords)
#     nLoop=0
#     while(nLoop<nCount):
#         strWord=listWords[nLoop]
#         strCheck=listChecks[nLoop]
# #        strWord=GLOBALKEEP_TrimString(strWord)
#         if(strWord!=""):
#             dictDraw["htmlContent"]=dictDraw["htmlContent"]+strWord+"  ["+strCheck+"]<BR>"
#         else:
#             dictDraw["htmlContent"]=dictDraw["htmlContent"]+"[*empty*]"+"  ["+strCheck+"]<BR>"            
#         nLoop=nLoop+1
# #
#     dictDraw["htmlContent"]=dictDraw["htmlContent"]+"The guess was "+dictDraw["strWordGuess"]+"."
#     dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Guess Count: "+dictDraw["strGuessCount"]+"<BR>"
# #
#     dictDraw["htmlHint"]="Hint:  "+dictDraw["strAIHint"]
#     dictDraw["htmlInfo"]=f"My word is a {dictDraw["strAICategory"]} and has {dictDraw["strAILength"]} letters."
# #    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     if(dictDraw["IsLocal"]!="No"):
#        strForm="<FORM action='http://127.0.0.1:5000/formpost' method='get'>"
#     else:
#        strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
#     strForm=strForm+"<input type='submit' value='Send'/><BR>"
#     strForm=strForm+"---<BR>"
#     strForm=strForm+"Name (save a score):  <input type='text' name='username' value='"+strInUsername+"'/><BR>"
#     strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
#     strForm=strForm+"</FORM>"
#     dictDraw["htmlForm"]=strForm
#     return dictDraw
# #
# #----------------------------------------------------------------------------#
# #Function:  APP_win()
# #----------------------------------------------------------------------------# 
# def APP_win(dictDraw,strInSession,strInWordGuess,strInUsername):
#     dictDraw["htmlHeader"]="*Guess My Word.*<BR>You have guessed my word.<BR>  You guessed "+dictDraw["strWordGuess"]+"."
#     if(strInUsername==""):
#         dictDraw["htmlFooter"]="Guess My Word.  You have guessed my word.<BR>"
#     else:
#         dictDraw["htmlFooter"]="*Guess My Word, "+strInUsername+"* You have guessed my word.<BR>"
# #
#     dictDraw["htmlContent"]=""
#     listChecks=dictDraw["listChecks"]
#     listWords=dictDraw["listWords"]
#     nCount=len(listWords)
#     nLoop=0
#     while(nLoop<nCount):
#         strWord=listWords[nLoop]
#         strCheck=listChecks[nLoop]
# #        strWord=GLOBALKEEP_TrimString(strWord)
#         if(strWord!=""):
#             dictDraw["htmlContent"]=dictDraw["htmlContent"]+strWord+"  ["+strCheck+"]<BR>"
#         else:
#             dictDraw["htmlContent"]=dictDraw["htmlContent"]+"[*empty*]"+"  ["+strCheck+"]<BR>"            
#         nLoop=nLoop+1
# #
#     dictDraw["htmlContent"]=dictDraw["htmlContent"]+"You guessed my word -"+dictDraw["strWordGuess"]+"-."
#     dictDraw["htmlContent"]=dictDraw["htmlContent"]+"  Guess Count: "+dictDraw["strGuessCount"]+"<BR>"
# #
#     dictDraw["htmlHint"]="New Hint:  "+dictDraw["strAIHint"]
#     dictDraw["htmlInfo"]=f"I have a new word.  It is a {dictDraw["strAICategory"]} and has {dictDraw["strAILength"]} letters."
# #    strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     if(dictDraw["IsLocal"]!="No"):
#        strForm="<FORM action='http://127.0.0.1:5000/formpost' method='get'>"
#     else:
#        strForm="<FORM action='http://phanes.pythonanywhere.com/formpost' method='get'>"
#     strForm=strForm+"Word guess:  <input type='text' name='wordguess' value=''/>"
#     strForm=strForm+"<input type='submit' value='Send'/><BR>"
#     strForm=strForm+"---<BR>"
#     strForm=strForm+"Name (save a score):  <input type='text' name='username' value='"+strInUsername+"'/><BR>"
#     strForm=strForm+"<input type='hidden' name='session' value='"+strInSession+"'/><BR>"
#     strForm=strForm+"</FORM>"
#     dictDraw["htmlForm"]=strForm
#     return dictDraw
#
#----------------------------------------------------------------------------#
#Function:  before()
#----------------------------------------------------------------------------# 
#@app.before_request
# def before():
#     dictGLOBAL=dict()
#     dictGLOBAL=GLOBALKEEP_Constants(dictGLOBAL)
#     strSession=GLOBALKEEP_ReadOpen(dictGLOBAL)
#     dictGLOBAL["strSession"]=strSession
#     dictGLOBAL=GLOBALKEEP_Read(dictGLOBAL)
#     dictGLOBAL=GLOBALKEEP_Close(dictGLOBAL)
#     dictGLOBAL=None
#     return
# #
# #----------------------------------------------------------------------------#
# #Function:  after()
# #----------------------------------------------------------------------------# 
# #@app.after_request
# def after(responseIn):
#     dictGLOBAL=dict()
#     nOut=GLOBALKEEP_Constants(dictGLOBAL)
#     strSession=GLOBALKEEP_WriteOpen(dictGLOBAL)
#     dictGLOBAL["strSession"]=strSession
#     nOut=GLOBALKEEP_Write(dictGLOBAL)
#     dictGLOBAL=GLOBALKEEP_Close(dictGLOBAL)
#     dictGLOBAL=None
#     return responseIn
# #
# #----------------------------------------------------------------------------#
# #Function:  draw1()
# #----------------------------------------------------------------------------# 
# @app.route('/draw1')
# def draw1():
#     strReturn="draw1"
#     return strReturn
# #
# #----------------------------------------------------------------------------#
# #Function:  draw0()
# #----------------------------------------------------------------------------# 
# @app.route('/draw0')
# def draw0():
#     strReturn="draw0"
#     return strReturn
#
#----------------------------------------------------------------------------#
#Function:  formpost()
#----------------------------------------------------------------------------# 
@app.route('/formpost',methods=["GET","POST"])
def formpost():
    if(request.method=="GET"):
        strWordGuess=request.args.get("wordguess")
        strUsername=request.args.get("username")
        strSession=request.args.get("session")
    if(request.method=="POST"):
        strWordGuess=request.form("wordguess")
        strUsername=request.form("username")
        strSession=request.form("session")
    dictDraw=dict()
    dictDraw["strFileSave"]=strSession
#
    GLOBALKEEP_SessionRead(dictDraw,dictDraw["strFileSave"])
#
    strWordGuess=strWordGuess.upper()
    dictDraw["strWordGuess"]=strWordGuess
    listWords=dictDraw["listWords"]
    listWords.append(strWordGuess)
    #
    nGuessCount=int(dictDraw["strGuessCount"])
    nGuessCount=nGuessCount+1
    dictDraw["strGuessCount"]=str(nGuessCount)
#
    strCheck=funcCheckGuess(dictDraw,dictDraw["strWordGuess"],dictDraw["strAIWord"])
    listChecks=dictDraw["listChecks"]
    listChecks.append(strCheck)
    if(strCheck!="*"):
        dictDraw = APP_guess(dictDraw,strSession,
                            strWordGuess,strUsername)
    else:
        dictAILINK=dict()
        AILINK_Open(dictAILINK)
        strTemp=AILINK_GetWord(dictAILINK)
        dictDraw["strAIWord"]=dictAILINK["strGuessWord"].upper()
        dictDraw["strAICategory"]=dictAILINK["strGuessCategory"]
        dictDraw["strAILength"]=str(dictAILINK["nGuessLength"])
        strAIHint=AILINK_GetHint(dictAILINK,dictDraw["strAIWord"])
        AILINK_Close(dictAILINK)
        dictAILINK.clear()
        dictAILINK=None
        dictDraw["strAIHint"]=strAIHint
        #
        dictDraw = APP_win(dictDraw,strSession,
                            strWordGuess,strUsername)
        #
        dictDraw["strWordGuess"]=""
        dictDraw["strGuessCount"]=str(0)
        listWords=dictDraw["listWords"]
        listWords.clear()
        listWords=[]
        dictDraw["listWords"]=listWords
        listChecks=dictDraw["listChecks"]
        listChecks.clear()
        listChecks=[]
        dictDraw["listChecks"]=listChecks
        #
    htmlHeader=dictDraw["htmlHeader"]
    htmlFooter=dictDraw["htmlFooter"]
    htmlContent=dictDraw["htmlContent"]
    htmlHint=dictDraw["htmlHint"]
    htmlInfo=dictDraw["htmlInfo"]
    htmlForm=dictDraw["htmlForm"]
    strReturn = render_template("app.html",
                    htmlHeader=htmlHeader,
                    htmlFooter=htmlFooter,
                    htmlContent=htmlContent,
                    htmlHint=htmlHint,
                    htmlInfo=htmlInfo,
                    htmlForm=htmlForm)
#
    GLOBALKEEP_SessionWrite(dictDraw,dictDraw["strFileSave"])
    dictDraw=None
#
    return strReturn
#
#----------------------------------------------------------------------------#
#Function:  home()
#----------------------------------------------------------------------------# 
@app.route('/')
def home():
    dictHome = dict()
    GLOBALKEEP_Constants(dictHome)
    GLOBALKEEP_Init(dictHome)
    strSession=GLOBALKEEP_GetNewSessionID(dictHome,"globalkeep.txt")
    dictHome["strFileSave"]=strSession
    #
    dictAILINK=dict()
    AILINK_Open(dictAILINK)
    strTemp=AILINK_GetWord(dictAILINK)
    dictHome["strAIWord"]=dictAILINK["strGuessWord"].upper()
    dictHome["strAICategory"]=dictAILINK["strGuessCategory"].upper()
    dictHome["strAILength"]=str(dictAILINK["nGuessLength"])
    strAIHint=AILINK_GetHint(dictAILINK,dictHome["strAIWord"])
    AILINK_Close(dictAILINK)
    dictAILINK.clear()
    dictAILINK=None
    dictHome["strAIHint"]=strAIHint
    #
    GLOBALKEEP_SessionWrite(dictHome,strSession)
    GLOBALKEEP_SessionRead(dictHome,strSession)
#
#    dictHome = APP_home(dictHome,strSession)
    dictCall=dict()
    dictCall["function"]="APP_home"
    strCall=jsonify(dictHome)
    dictCall["jsonString"]=strCall
    responseOut=requests.get(url="http://localhost:5051/app_call",params=dictCall)
    strOut=responseOut.json()

#
    htmlHeader=dictHome["htmlHeader"]
    htmlFooter=dictHome["htmlFooter"]
    htmlContent=dictHome["htmlContent"]
    htmlHint=dictHome["htmlHint"]
    htmlInfo=dictHome["htmlInfo"]
    htmlForm=dictHome["htmlForm"]
    strReturn = render_template("app.html",
                    htmlHeader=htmlHeader,
                    htmlFooter=htmlFooter,
                    htmlContent=htmlContent,
                    htmlHint=htmlHint,
                    htmlInfo=htmlInfo,
                    htmlForm=htmlForm)
    GLOBALKEEP_SessionWrite(dictHome,dictHome["strFileSave"])
    dictHome=None
    return strReturn

if(__name__=="__main__"):
    app.run(debug="True",host="0.0.0.0",port=5000)
