# from gtts import gTTS
#
#
# def tts(text, path):
#     voice = gTTS(text=text, lang='tr')
#     path += "/output.mp3"
#     voice.save(path)
#     return path


import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def tts(text, path):
    path += "/output.mp3"
    engine.save_to_file(text, path)
    engine.runAndWait()
    return path
