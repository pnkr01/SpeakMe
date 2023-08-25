import boto3,os
from tempfile import gettempdir
from contextlib import closing

from error.error import handle_io_error
def aws_config():
    return boto3.session.Session(profile_name="demo_profile")
def aws_client(aws_mag_con):
    return aws_mag_con.client(service_name='polly', region_name="us-east-1")
def handle_speech_service(response):
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(gettempdir(), "speech.mp3")
        try:
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            handle_io_error(error)
    return output