import os
import openai
import langchain
import gradio as gr
from .llm_helpers import *

MUSIC_DIR = "/home/sanjmi/experimental"
CONFIG_FILE = "/home/sanjmi/ros2_ws/src/swarmGPT/crazyflie/config/crazyflies.yaml"

openai.organization = "org-PQJjdyLH3oHidF9FkzWsWXT0"
openai.api_key = os.getenv("OPENAI_API_KEY")

cg = Choreographer(music_dir=MUSIC_DIR, config_file=CONFIG_FILE, every_n_beats=2, x_lim=1, y_lim=1, z_lim=2)

def add_history(interface, user_input, cg_input ):
    interface = interface + [(user_input,str(cg_input))]
    return interface

def process_input(user_input, interface):
    cg.set_song(user_input)
    beat_times = cg.get_beats(start_time=38, end_time=75)
    add_history(interface, user_input, beat_times)

    prompt_types = {'I': 'initial', 'R': 'redo', 'C': 'collision-avoidance', 'M': 'custom'}
    custom_text = ""

    output = cg.choreograph(beat_times, prompt_types[user_input], custom_text)
    add_history(interface, None, "\nFormatted LLM output: {output}")
    
    data = cg.get_waypoints(output)

    return  "", data

#def custom_prompt(user_input, interface):

with gr.Blocks() as ui:
    interface = gr.Chatbot([],elem_id = "interface", label="Crazyflies")
    user_input = gr.inputs.Textbox(label="Enter request")
    response_button = gr.Button("Generate response")
    #TODO: simulation button

    user_input.submit(fn =  process_input, inputs = [user_input, interface], outputs = [user_input, interface])
    response_button.click(fn = process_input,inputs = [user_input, interface],outputs = [user_input, interface] )
