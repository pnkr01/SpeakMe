def generate_speech(client,text):
    return client.synthesize_speech(VoiceId='Joanna',   OutputFormat='mp3', Text=text,Engine='neural')