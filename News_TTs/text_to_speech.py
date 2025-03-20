from gtts import gTTS
from IPython.display import Audio, display

def generate_tts(text, lang="hi"):
    if not text or not isinstance(text, str):
        raise ValueError("Input text must be a non-empty string.")

    tts = gTTS(text=text, lang=lang, slow=False)
    temp_filename = "audio.mp3"
    tts.save(temp_filename)
    return temp_filename