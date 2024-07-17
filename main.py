from dotenv import load_dotenv
import os
from gemini import *
from torbrowser import test

load_dotenv()
GEMINI_KEY = os.environ["API_KEY"]

gemini = get_model(api_key=GEMINI_KEY)

test()