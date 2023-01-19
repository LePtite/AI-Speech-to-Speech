import json
from ibm_watson import SpeechToTextV1 
from ibm_watson import LanguageTranslatorV3 
from os.path import join,dirname
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('XfKm333C0g5CBiwUx_bxwCqBJKjI0KMKzVtLTgCc_lh0')
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/4ac0c1bc-fd33-4254-8ffa-17d7fff557a0')
authenticator = IAMAuthenticator('O428MvnY9Vrpl_YnUyuvCBsJhzx8qCybzAvP1ymWnQcm')    
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d08077a3-f0b2-4894-b7eb-27c76dcfac89')
with open(join(dirname(__file__), './.', 'IFT360.mp3'),'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        word_alternatives_threshold=0.9,
        keywords=['project'],
        keywords_threshold=0.5).get_result()
#*****This the code for my own reference,do not print it*****
#print(json.dumps(speech_recognition_results, indent=2))
#print(json.dumps(speech_recognition_results["results"], indent=2))
#*******The End of my reference******#
#*****1.This where I'm going to start extracting results******
#*****2.First of all,i'm going to get the json results******
variable=json.dumps(speech_recognition_results["results"], indent=2)
#*****3.Then I'm going to convert them to a dictionary so that i can extract relevant info*****
loadVariable=json.loads(variable)
#*****4.Iterate over the dictionary to get relevant results********"
for x in loadVariable:
	x
#*****5.Finally,get the transcript*****
for y in x["alternatives"]:
	print(                                         )
	print("****This is the transcript from the audio file******")
	print(                                         )
	print(y["transcript"])
	print(                                         )
	print("****End of the transcript*****")
print(                                         )
print(                                         )
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
#The transcipt go here so that the code can translate it
	wordToBeTranslated=y["transcript"]
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
	wordToBeTranslated=y["transcript"]
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
	wordToBeTranslated=y["transcript"]
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
	wordToBeTranslated=y["transcript"]
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
