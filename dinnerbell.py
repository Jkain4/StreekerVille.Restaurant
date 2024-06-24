import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Sample rate
sample_rate = 44100

# Duration of the song in seconds
duration = 3.5 * 60

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Frequencies for different sections
violin_intro_freq = 440  # A4
steel_drum_intro_freq = 262  # C4

# Violin part
violin_intro = np.sin(2 * np.pi * violin_intro_freq * t[:int(sample_rate * 30)]) * np.exp(-t[:int(sample_rate * 30)])

# Steel Drum part
steel_drum_intro = np.sin(2 * np.pi * steel_drum_intro_freq * t[:int(sample_rate * 30)]) * np.exp(-t[:int(sample_rate * 30)] / 2)

# Combining the intro parts
intro = violin_intro + steel_drum_intro

# Generating the sound wave for the rest of the song
# Placeholder for the complex part
song_wave = np.zeros_like(t)

# Combining the intro with the rest of the song
song_wave[:intro.size] = intro

# Normalize the wave
song_wave /= np.max(np.abs(song_wave))

# Save to a file
write("/mnt/data/abyssal_eruption.wav", sample_rate, (song_wave * 32767).astype(np.int16))

"/mnt/data/abyssal_eruption.wav"