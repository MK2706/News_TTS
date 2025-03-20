from googletrans import Translator

def translate_to_hindi(text):
    if not text or not isinstance(text, str):
        return ""

    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text