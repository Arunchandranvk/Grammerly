from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    print("hhhhhhhhhhhhhhhh")
    print(text)
    translated = translator.translate(text, src=source_lang, dest=target_lang)
    return translated.text

