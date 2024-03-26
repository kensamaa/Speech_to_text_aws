import speech_recognition as sr
import os

def lambda_handler(event, context):
    print('starting translation')

    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    audiofile='G:/DEV/Speech_to_text_aws/backend/translationService/male.wav'

    check_file = os.path.isfile(audiofile)

    print(check_file)
    with sr.AudioFile(audiofile) as source:
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition#
            #r.recognize_google(audio_text, language = "fr-FR")
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
        
        except:
            print('Sorry.. run again...')