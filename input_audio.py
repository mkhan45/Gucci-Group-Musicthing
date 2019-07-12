import numpy as np
import librosa
import numpy as np
from pathlib import Path
from microphone import record_audio
from digital_samples_to_peaks2 import sample_to_peaks
from fingerprint import get_fingerprint
import pickle

class Database:
    def __init__(self):
        self.dictionary = {}
        self.id_to_name = {}

def get_mp3_data(path, secs=None):
    """
    Reads mp3 into numpy array

    Parameters
    ----------
    path : String
        global path to file

    Returns
    -------
    (Numpy array, int)
        A tuple containing the numpy array for the file and the int id
    """

    song_path = Path(path)
    data, sr = librosa.load(str(song_path.resolve()), sr=44100, mono=True, dtype=float, duration=secs)
    return data * 2**15

def get_mic_data(record_time): #also kind of unnecessary??
    """
    Parameters
    ----------
    record_time : int
        number of seconds to record

    Returns
    -------
    np.ndarray(seconds * sample_rate)
        The audio data
    """
    frames, sample_rate = record_audio(record_time)
    audio_data = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    return audio_data


def read_from_mp3_folder(path):
    """
    Reads folder of mp3s into database

    Parameters
    ----------
    path : String
        global path to folder

    Returns
    -------
    Database
        database of songs

    Dependencies
    ------------
    Song to fingerprint
    append_database
    """

    database = Database()

    folder = Path(path)
    for file in folder.iterdir():
        if not file.is_dir() and file.suffix == ".mp3":
            print(file.stem)
            name = file.stem
            samples = get_mp3_data(file)
            peaks = sample_to_peaks(samples)
            fingerprint = get_fingerprint(peaks, 15, len(database.id_to_name))
            append_database(database, fingerprint, name)

    return database

def append_database(database, fingerprint, song_name):
    """
    Appends a fingerprint to a database or creates
    a new one if it does not exist

    Parameters
    ----------
    database : Database
        database class

    fingerprint : dictionary
        fingerprint of song

    Dependencies
    ------------
    Song to fingerprint
    """
    if fingerprint[0] not in database.dictionary:
        database.dictionary[fingerprint[0]] = []
    database.dictionary[fingerprint[0]].append(fingerprint[1])
    database.id_to_name[len(database.id_to_name)] = song_name

def read_database_file(filename): #kind of unnecessary?
    """
    Reads database file into database object

    Parameters
    ----------
    filename : String
        filename

    Returns
    -------
    database : dictionary
    """
    with open(filename, 'rb') as file:
        db = pickle.load(file)
        print(type(db))
        print(db)
        return db
