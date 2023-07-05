#!/usr/bin/env python

from __future__ import annotations
import numpy as np
from crazyflie_py import *
from .llm_helpers import *
from pathlib import Path
import vlc, os

ROOT_DIR = "/home/tanmay/Documents/swarmGPT/src/swarmGPT" # Change as needed
MUSIC_DIR = os.path.join(ROOT_DIR, "music")
CONFIG_FILE = os.path.join(ROOT_DIR, "crazyflie/config/crazyflies.yaml")

class Waypoint:
    def __init__(self, agent, x, y, z, arrival, duration):
        self.agent = agent
        self.x = x
        self.y = y
        self.z = z
        self.arrival = arrival
        self.duration = duration

    def __lt__(self, other):
        return self.arrival < other.arrival

    def __repr__(self):
        return "Agent {} at {} s. [{}, {}, {}]".format(self.agent, self.arrival, self.x, self.y, self.z)
    
def create_waypoints_data_structure(data: np.ndarray) -> List[Waypoint]:
    waypoints = []
    lastAgent = None
    for row in data:
        if lastAgent is None or lastAgent != row[0]:
            lastTime = 0.0
        waypoints.append(Waypoint(
            int(row[0]),
            row[2],
            row[3],
            row[4],
            row[1],
            row[1] - lastTime))
        lastTime = row[1]
        lastAgent = int(row[0])

    # sort waypoints by arrival time
    waypoints.sort()

    return waypoints

def main():
    # Parameters
    song = "We Are The Champions" # input("Enter a name of a song: ")
    artist = "Queen" # input("Enter the artist's name: ")

    # Create a new choreographer (LLM-equipped tool), auto-configure drone information (starting positions, cfid's), set the song and arist name
    cg = Choreographer(music_dir=MUSIC_DIR, config_file=CONFIG_FILE, every_n_beats=2, x_lim=1, y_lim=1, z_lim=2)
    cg.set_song(song=song, artist=artist)

    # Get beat times from song
    beat_times = cg.get_beats(start_time=38, end_time=75)

    prompt_types = {'I': 'initial', 'R': 'redo', 'C': 'collision-avoidance', 'M': 'custom'}
    user_input = "I"

    while user_input != "":

        custom_text = input("\nEnter your prompt: ") if user_input == 'M' else ""

        # Get choreography through LLM API query
        output = cg.choreograph(beat_times, prompt_types[user_input], custom_text)
        print(f"\nFormatted LLM output: {output}")

        # Load data from text output of LLM
        data = cg.get_waypoints(output)

        # Convert waypoint data into internal waypoint data structure
        waypoints = create_waypoints_data_structure(data)

        # Print waypoints
        print("\nParsed waypoints:")
        for waypoint in waypoints:
            print(f"{waypoint}")

        # Input validation
        user_input = "Invalid"
        while user_input not in prompt_types.keys() and user_input != '':
            user_input = input("\nPress enter to get dancing. Press R to reject waypoints and regenerate something more creative. Press C to send a collision-avoidance reminder. Press M to enter a custom prompt...")

    p = vlc.MediaPlayer(os.path.join(MUSIC_DIR, f"{song.lower()}.mp3"))

    # execute waypoints
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.takeoff(targetHeight=1.0, duration=3.0)
    timeHelper.sleep(2.0)
    p.play()
    p.set_time(38000) # Time to start playing at (milliseconds)

    lastTime = 0.0
    for waypoint in waypoints:
        if waypoint.arrival == 0:
            pos = [waypoint.x, waypoint.y, waypoint.z]
            # print(waypoint.agent, pos, 2.0)
            cf = allcfs.crazyfliesById[waypoint.agent]
            cf.goTo(pos, 0, 2.0)
        elif waypoint.duration > 0:
            timeHelper.sleep(waypoint.arrival - lastTime)
            lastTime = waypoint.arrival
            pos = [waypoint.x, waypoint.y, waypoint.z]
            # print(waypoint.agent, pos, waypoint.duration)
            cf = allcfs.crazyfliesById[waypoint.agent]
            cf.goTo(pos, 0, waypoint.duration)

    # land
    print("Landing")
    allcfs.land(targetHeight=0.02, duration=2.0)
    timeHelper.sleep(2.0)
    print("Landed")
    p.stop()

if __name__ == "__main__":
    main()
