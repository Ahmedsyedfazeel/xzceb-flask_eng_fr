from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
    model_id = 'en-fr'
    print ('write your content you want to translate')
    text_to_translate = input()



# Prepare the Authenticator
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

    language_translator.set_service_url(api_url )

# Translate
    translation = language_translator.translate(
        text=text_to_translate,
        model_id=model_id).get_result()

# Print results
    print(json.dumps(translation, indent=2, ensure_ascii=False))


    return "Translated text to French"

@app.route("/FrenchToenglish")
def FrenchToenglish():
    text_to_translate = request.args.get('text_to_translate')
    # Write your code here
     model_id = 'fr-en'
    print ('écrire le contenu que vous souhaitez')
    text_to_translate = input()



# Prepare the Authenticator
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )

    language_translator.set_service_url(api_url )

# Translate
    translation = language_translator.translate(
        text=text_to_translate,
        model_id=model_id).get_result()

# Print results
    print(json.dumps(translation, indent=2, ensure_ascii=False))

    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
