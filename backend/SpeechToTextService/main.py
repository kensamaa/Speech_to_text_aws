import speech_recognition as sr
import boto3

def lambda_handler(event, context):
    print('starting translation')

    try:
        r = sr.Recognizer()

        # Get S3 bucket and object details from event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']
        
        print(f"file received from S3: {bucket_name}/{object_key}")
        
        # Download audio file from S3
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, object_key, '/tmp/audio.wav')  # Store locally in /tmp
        
        with sr.AudioFile('/tmp/audio.wav') as source:
            audio_text = r.listen(source)

            # Recognise speech using Google Speech Recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)

            # Return the transcribed text as the Lambda function's response
            return {
                'statusCode': 200,
                'body': text
            }

    except Exception as e:
        print(f'Error: {e}')
        return {
            'statusCode': 500,
            'body': 'Error transcribing audio'
        }