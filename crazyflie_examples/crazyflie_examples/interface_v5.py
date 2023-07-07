import os
import openai
import langchain
import gradio as gr
import llm_helpers
#import waypoints_gui

MUSIC_DIR = "/home/sanjmi/experimental"
CONFIG_FILE = "/home/sanjmi/ros2_ws/src/swarmGPT/crazyflie/config/crazyflies.yaml"

openai.api_key = os.getenv("OPENAI_API_KEY")

cg = llm_helpers.Choreographer(music_dir=MUSIC_DIR, config_file=CONFIG_FILE, every_n_beats=2, x_lim=1, y_lim=1, z_lim=2)
#wp = waypoints_gui.Waypoint

class Interface:
    def __init__(self,initialized):
        self.initialized = initialized

    def song(self,song_input):
        cg.set_song(song_input)
        return "Song set. Please enter prompt type.", gr.update(visible=True), gr.update(visible=False)


    def process_input(self,prompt_type_input, custom_text):
        custom_text = custom_text if prompt_type_input=="custom" else "" 
        beat_times = cg.get_beats(start_time=38, end_time=75)

        if prompt_type_input == "custom" and custom_text=="":
            return "","", gr.update(visible = True)
        
        choreography, prompt = cg.choreograph(beat_times, prompt_type_input, custom_text)

        return choreography, prompt, gr.update(visible = False)
    
def display_waypoints(song_input, output):
    data = cg.get_waypoints(output)
    #waypoints = wp.create_waypoints_data_structure(data)
    
    #waypoints_gui.fly(song_input,waypoints)
    
interface = Interface(False)


with gr.Blocks() as ui:
    gr.Markdown("""
    # SwarmGPT
    Instructions:
    1. Enter song and click on 'Configure LLM'.
    2. Enter one of the following prompt types: initial, redo, collision-avoidance, custom.
    NOTE: Please enter 'initial' if this is the first choreography by swarmGPT for a particular song.
    3. If you choose to write your own prompt after looking at the simulation, 
    please enter 'custom' in the 'Enter Prompt Type' textbox and press Enter.
    Enter your prompt in the textbox that appeared.
    
    Hope you enjoy this demo :)""")
    with gr.Row():
        song_input = gr.Textbox(label="Enter Song")
        prompt_output = gr.Textbox(label="Prompt")
    with gr.Row():
        prompt_type_input = gr.Textbox(label="Enter Prompt Type:", placeholder="initial/redo/collision-avoidance/custom", visible = False)
        ch_output = gr.Textbox(label="Waypoints")
    with gr.Row():
        custom_prompt = gr.Textbox(label="Enter Custom Prompt", visible=False)
    with gr.Row():
        llm_button = gr.Button("Configure LLM")
        start_button = gr.Button("Start")
    run_button = gr.Button("Let the Crazyflies dance")

    with gr.Row():
        custom_text = gr.Textbox(value = "", visible = False)
    
    #TODO: simulation button

    llm_button.click(fn =  interface.song, inputs = [song_input], outputs = None)
    song_input.submit(fn =  interface.song, inputs = [song_input], outputs = [prompt_output,prompt_type_input,custom_prompt])
    prompt_type_input.submit(fn = interface.process_input, inputs = [prompt_type_input, custom_text], outputs = [ch_output, prompt_output, custom_prompt])


    start_button.click(fn = interface.process_input, inputs = [prompt_type_input, custom_text], outputs = [ch_output, prompt_output, custom_prompt])


    custom_prompt.submit(fn = interface.process_input, inputs = [prompt_type_input,custom_prompt], outputs=[ch_output, prompt_output, custom_prompt])

if __name__ == '__main__':
    ui.launch()