from functools import partial
from urllib import response
from taipy.gui import Gui, notify
from datetime import datetime as dt
import keyboard as kb
import openai


datetime = dt.now()
test = "Enter Input";
stylekit = {
    "color_primary": "#BADA55",
    "color_secondary": "#C0FFE",
    
}

# Set your OpenAI API key
# MY_API_KEY = "[Inset_API_KEY_HERE]";
 
# Initialize the OpenAI API client
openai.api_key = MY_API_KEY

def chat_with_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=500  # You can adjust the response length as needed
    )
    return response.choices[0].text

section_1 ="""
![Test image](bot.png) *ChooseUrBot*
===========================================

"""
response = " "
section_2 = """
<|layout|columns= 1 1 1 |

<|card|
![Test image](md2.png)

<|Medic|button|on_action=medicClick|>
|>

<|card|
![Test image](ms.png)

<|Ghost|button|on_action=drunkClick|>
|>

<|card|
![Test image](wt.png)

<|Witch|button|on_action=soldierClick|>
|>

|>

<|card|
<|{response}|>
|> 

<|card|
<|{test} |label = Enter Text|input||>
<|{enter}|button|label = Enter|on_action=enterButtion|>
|> 

"""
def on_init(state):
      state.response = test
def medicClick(state):
        state.prompt = ""
        state.prompt = "You are a mental health support assistant.\nChatbot:"
        notify(state,"info","Medic Selected.")
def drunkClick(state):
        prompt = ""
        state.prompt = "You are a ghost.\nChatbot:"
        notify(state,"info","Ghost Selected.")
def soldierClick(state):
        prompt = ""
        state.prompt = "You are a witch.\nChatbot:"
        notify(state,"info","Witch Selected.")

def enterButtion(state):
    state.prompt += f"{state.test}\nChatBot:"
    temp = chat_with_chatgpt(state.prompt)
    #state.enter = input()
    state.response = temp
def on_change(state, var, val):
    if(var == "test"):
        state.test = val
          
prompt = ""
enter = ""
test = response
Gui(page=section_1+section_2).run(use_reloader  = True)



