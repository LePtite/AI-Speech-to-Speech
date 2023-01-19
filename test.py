#********Windows installation***********
#pip install simpleaudio
#***********The End*********************
#********Linux installation***********
#sudo apt-get install -y python3-dev libasound2-dev
#***********The End*********************
##import simpleaudio as sa
##wave_obj = sa.WaveObject.from_wave_file("audio.flac")
##play_obj = wave_obj.play()
##play_obj.wait_done()

import simpleaudio as sa
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
word="This ancient form of poem writing is renowned for its small size as well as the precise punctuation and syllables needed on its three lines"

authenticator = IAMAuthenticator('is8aCbkNL4XSpV13i3GV_B0RaMRxZppAb2_TemPWaGV3')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9750f625-ad22-42a2-b15c-094c4c0d67ba')

with open('record.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            word,
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
wave_obj = sa.WaveObject.from_wave_file("record.wav")
play_obj = wave_obj.play()
play_obj.wait_done()
