from deep_translator import GoogleTranslator

def translate_to_hindi(text):
    if not text or not isinstance(text, str):
        return ""
    
    translator = GoogleTranslator(source="auto", target="hi")
    return translator.translate(text)
