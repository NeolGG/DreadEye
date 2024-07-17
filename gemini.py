import google.generativeai as genai
import os


def get_model(api_key: str, model:str = 'gemini-1.5-flash') -> genai.GenerativeModel:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model)
    
    return model



