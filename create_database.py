from input_audio import read_from_mp3_folder, get_mp3_data
from digital_samples_to_peaks2 import sample_to_peaks
from fingerprint import get_fingerprint
import pickle

path = input("What is the path of the folder?\n")
database = read_from_mp3_folder(path)

filename = input("What should the file be called?\n")

with open(filename, 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(database, f, pickle.HIGHEST_PROTOCOL)
