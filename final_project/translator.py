import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
model_id = en-fr

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url )

# Translate
def englishToFrench(englishText):
    translation = language_translator.translate(
    text = englishText,
    model_id = model_id).get_result()
    return translation

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text = frenchText, model_id = model_id).get_result()
        return translation
