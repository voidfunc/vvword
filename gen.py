import google.generativeai as genai
import os
def gen(words,type,api=False,longmethod=False):
    GOOGLE_API_KEY=''
    if api:
        GOOGLE_API_KEY = api
    else:
        GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    preprompt=open("preprompt.txt", "r",encoding="utf-8")
    preprompt=preprompt.read()
    preprompt=preprompt.replace("[type]",type)
    if longmethod:
        preprompt=preprompt.replace("[length]","100")
    else:
        preprompt=preprompt.replace("[length]","50")
    prompt:str=''
    for i in words.split(' '):
        if len(prompt) == 0:
            prompt=f'{i}'
        else:
            prompt+=','+f'{i}'
    messages = [
        {'role':'user',
         'parts': [preprompt]},
        {'role':'model',
         'parts':["ok"]},
        {'role':'user',
         'parts': [f"{prompt}"]}
    ]
    response = model.generate_content(messages)
    return response.text
    pass
