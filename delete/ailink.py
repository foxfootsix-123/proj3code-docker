import time
import os
from openai import OpenAI
import requests
#
#----------------------------------------------------------------------------#
#Layer:  AILink
#curl https://api.openai.com/v1/responses \
#  -H "Content-Type: application/json" \
#  -H "Authorization: Bearer " \
#  -d '{
#    "model": "gpt-5-nano",
#    "input": "write a haiku about ai",
#    "store": true
#  }'
#----------------------------------------------------------------------------#
#
#----------------------------------------------------------------------------#
#Function:  AILINK_GetWord()
#response = requests.post('https://api.openai.com/v1/responses', headers=headers, json=json_data)
#----------------------------------------------------------------------------#
def AILINK_GetWord(dictAILINK):
    print(f"AILINK_GetWord()::calling function")
    openaiClient = dictAILINK["openaiClient"]
    strInput = "Will you tell me a single random word with less than 10 letters and the word category (like thing, verb, place, or person)?"
    strInput = strInput + "Separate the word and category with a colon.  I am using the word for a word guessing game."
    timeTimer = time.time()
    dictOut = openaiClient.responses.create(model="gpt-5.4-nano",
                                            input=strInput)
    timeTimer = time.time() - timeTimer
    dictAILINK["timeWordTimer"]=timeTimer
#
    print(dictOut.output[0].content[0].text)
    strTemp0 = dictOut.output[0].content[0].text
    listSplit = strTemp0.split(":")
    strSplit0=""
    strTemp = listSplit[0]
    nCount = len(strTemp)
    nLoop = 0
    while(nLoop<nCount):
        strChar = strTemp[nLoop]
        IsValid = False
        if(((strChar>=("a")) and (strChar<=("z"))) or 
           ((strChar>=("A")) and (strChar<=("Z"))) or
           ((strChar>=("0")) and (strChar<=("9"))) or
           (strChar==(" "))):
            IsValid = True
        if(IsValid==False):
            strSplit0=strSplit0+" "
        else:
            strSplit0=strSplit0+strChar
        nLoop=nLoop+1
    strTemp0 = strTemp
    dictAILINK["strGuessWord"]=strSplit0.strip()
    strTemp = listSplit[1]
    strSplit1=""
    nCount = len(strTemp)
    nLoop = 0
    while(nLoop<nCount):
        strChar = strTemp[nLoop]
        IsValid = False
        if(((strChar>=("a")) and (strChar<=("z"))) or 
           ((strChar>=("A")) and (strChar<=("Z"))) or
           ((strChar>=("0")) and (strChar<=("9"))) or
           (strChar==(" "))):
            IsValid = True
        if(IsValid==False):
            strSplit1=strSplit1+" "
        else:
            strSplit1=strSplit1+strChar
        nLoop=nLoop+1
    dictAILINK["strGuessCategory"]=strSplit1.strip()
    dictAILINK["nGuessLength"]=len(strSplit0.strip())
    strWord=dictAILINK["strGuessWord"]
    print(f"AILINK_GetWord()::exit")
    return strWord
#
#----------------------------------------------------------------------------#
#Function:  AILINK_GetHint()
#----------------------------------------------------------------------------#
def AILINK_GetHint(dictAILINK,strInWord):
    print(f"AILINK_GetHint()::calling function")
    openaiClient = dictAILINK["openaiClient"]
    strInput = "Will you give me a hint for this word, "+strInWord+"?"
    strInput = strInput + "I am using the word for a word guessing game."
    strInput = strInput + "Do not put the word in the hint text."
    strInput = strInput + "Do not answer with the prefix 'Sure! **Hint:** '."
    timeTimer = time.time()
    dictOut = openaiClient.responses.create(model="gpt-5.4-nano",
                            input=strInput)
    timeTimer = time.time() - timeTimer
    dictAILINK["timeHintTimer"]=timeTimer
#
    print(dictOut.output[0].content[0].text)
    strTemp = dictOut.output[0].content[0].text
    dictAILINK["strGuessHint"]=strTemp
    strHint=strTemp
    print(f"AILINK_GetHint()::exit")
    return strHint
#
#----------------------------------------------------------------------------#
#Function:  AILINK_GetAPIKey()
#----------------------------------------------------------------------------#
def AILINK_GetAPIKey(dictAILINK):
    strKey = dictAILINK["gptkey"]
    return strKey
#
#----------------------------------------------------------------------------#
#Function:  AILINK_Open()
#
#from openai import OpenAI
#
#client = OpenAI()
#
#response = 
# client.responses.create(
#    model="gpt-4.1",
#    input="Explain quantum computing in simple terms."
#)

#----------------------------------------------------------------------------#
def AILINK_Open(dictAILINK):
#    dictAILINK = dict()
#
    strKey="sk-proj-FDPUCyeCspXAT1"
    strKey=strKey+"Tp7ut0SgE1k2CFi9VuGNxV6ulZrqL2rKyen2LEZYl-"
    strKey=strKey+"AUJCEOxhrR16eP3vQzT3BlbkFJspuz6dTjvOYdnXczlQm"
    strKey=strKey+"hdP"
    strKey=strKey+"st4HNt4OmK0L06F-ibOUo_y4_HQ5XIE7iwfL061ijBSCQg"
    strKey=strKey+"mIp94A"
#
    dictAILINK["gptapi"]=strKey
#
    openaiClient = OpenAI(api_key=strKey)
    dictAILINK["openaiClient"]=openaiClient
# #
    return dictAILINK
#
#----------------------------------------------------------------------------#
#Function:  AILINK_Close()
#----------------------------------------------------------------------------#
def AILINK_Close(dictAILINK):
#    dictAILINK.clear()
#    dictAILINK=None
    return
#
#----------------------------------------------------------------------------#
#Function:  AILINK_main()
#----------------------------------------------------------------------------#
def AILINK_main():
    dictAILINK=dict()
    AILINK_Open(dictAILINK)
    strWord = AILINK_GetWord(dictAILINK)
    strHint = AILINK_GetHint(dictAILINK,strWord)
    AILINK_Close(dictAILINK)
    dictAILINK=None
    return
#    
AILINK_main()