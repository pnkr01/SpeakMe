import tkinter as tk
import os,sys
from error.error import handle_error
from speech.generate_speech import generate_speech
from service.services import aws_client, aws_config, handle_speech_service

root = tk.Tk()
root.geometry("400x240")
root.title("Amazon Polly Text to Speech")
textExample = tk.Text(root, height=10)
textExample.pack()
def get_text():
    aws_mag_con = aws_config()
    client = aws_client(aws_mag_con)
    text = textExample.get("1.0", "end")
    response = generate_speech(client, text)
    if "AudioStream" in response:
        output = handle_speech_service(response)
    else:
        handle_error()
    if sys.platform=='win32':
        os.startfile(output)
btnRead=tk.Button(root, height=1, width=10, text="Read",command=get_text)
btnRead.pack()
root.mainloop()