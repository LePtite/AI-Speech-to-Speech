import json
from ibm_watson import LanguageTranslatorV3 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator  
authenticator = IAMAuthenticator('O428MvnY9Vrpl_YnUyuvCBsJhzx8qCybzAvP1ymWnQcm')    
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d08077a3-f0b2-4894-b7eb-27c76dcfac89')
print('Welcome to the IBM Watson Translator')
print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
print('                                    ')
print('Have fun! ')
print("Choose any language from this list")
print("\t1.Spanish")
print("\t2.French")
print("\t3.Hebrew")
print("\t4.Portuguese")
langChoice=int(input('What language should I translate it to?: '))
if langChoice==1:
#Ask user to input some text that the code can translate
	wordToBeTranslated=input('Enter some english text to be translated in spanish: ')
#API to get the language and translate it
	translation=language_translator.translate(text=wordToBeTranslated,model_id='en-es').get_result() 
	language = language_translator.identify('Translate from one language to another').get_result()
#Assign the spanish translation to a variable and print it
	variable=json.dumps(translation["translations"])
	variablex=json.loads(variable)
	variablexx=variablex[0]
	print ("**********************")
	print (variablexx["translation"])
	print ("**********************")
	variable2=json.dumps(language["languages"])
	print("the original language with confidence >0.95")
	print ("**********************")
	finalVariable=json.loads(variable2)
	print(finalVariable[0])
	print ("**********************")
elif langChoice==2:
#Ask user to input some text that the code can translate
	wordToBeTranslated=input('Enter some english text to be translated in french: ')
#API to get the language and translate it
	translation=language_translator.translate(text=wordToBeTranslated,model_id='en-fr').get_result() 
	language = language_translator.identify('Translate from one language to another').get_result()
#Assign the spanish translation to a variable and print it
	variable=json.dumps(translation["translations"])
	variablex=json.loads(variable)
	variablexx=variablex[0]
	print ("**********************")
	print (variablexx["translation"])
	print ("**********************")
	variable2=json.dumps(language["languages"])
	print("the original language with confidence >0.95")
	print ("**********************")
	finalVariable=json.loads(variable2)
	print(finalVariable[0])
	print ("**********************")
elif langChoice==3:
#Ask user to input some text that the code can translate
	wordToBeTranslated=input('Enter some english text to be translated in hebrew: ')
#API to get the language and translate it
	translation=language_translator.translate(text=wordToBeTranslated,model_id='en-he').get_result() 
	language = language_translator.identify('Translate from one language to another').get_result()
#Assign the spanish translation to a variable and print it
	variable=json.dumps(translation["translations"])
	variablex=json.loads(variable)
	variablexx=variablex[0]
	print ("**********************")
	print (variablexx["translation"])
	print ("**********************")
	variable2=json.dumps(language["languages"])
	print("the original language with confidence >0.95")
	print ("**********************")
	finalVariable=json.loads(variable2)
	print(finalVariable[0])
	print ("**********************")
elif langChoice==4:
#Ask user to input some text that the code can translate
	wordToBeTranslated=input('Enter some english text to be translated in portuguese: ')
#API to get the language and translate it
	translation=language_translator.translate(text=wordToBeTranslated,model_id='en-pt').get_result() 
	language = language_translator.identify('Translate from one language to another').get_result()
#Assign the spanish translation to a variable and print it
	variable=json.dumps(translation["translations"])
	variablex=json.loads(variable)
	variablexx=variablex[0]
	print ("**********************")
	print (variablexx["translation"])
	print ("**********************")
	variable2=json.dumps(language["languages"])
	print("the original language with confidence >0.95")
	print ("**********************")
	finalVariable=json.loads(variable2)
	print(finalVariable[0])
	print ("**********************")
else:
	print("Goodbye,i only accept 1, 2 ,3 and 4 as input")
	print("Your input is ",langChoice)

