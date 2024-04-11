import os

# Function to play sound
def play_sound(sound_path):
    os.system(f"afplay {sound_path}")  # Adjust command based on your OS and audio file format
