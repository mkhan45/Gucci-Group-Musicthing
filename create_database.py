from input_audio import read_from_mp3_folder, get_mp3_data
from digital_samples_to_peaks2 import sample_to_peaks
from fingerprint import get_fingerprint
# path = input("What is the path of the folder?\n")
# database = read_from_mp3_folder(path)
path = input("filename\n")
samples = get_mp3_data(path)
peaks = sample_to_peaks(samples)
fingerprint = get_fingerprint(peaks, 15, 0)
print(fingerprint)


filename = input("What should the file be called?\n")
pickle.dump(dictionary, filename)
