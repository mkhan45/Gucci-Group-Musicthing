import numpy as np
import librosa
import numpy as np
from pathlib import Path
from microphone import record_audio
import pickle

def generate_id(path):
    """
    Generate ID for a song from name/artist

    Parameters
    ----------
    path : Path (from pathlib)
        path to file

    Returns
    -------
    id : String (maybe int???)
        id of file
    """
    return "placeholder"

def get_mp3_data(path):
    """
    Reads mp3 into numpy array

    Parameters
    ----------
    path : String
        global path to file

    Returns
    -------
    (Numpy array, String)
        A tuple containing the numpy array for the file and the String id
    """
    
    song_path = Path(path)

    data, sr = librosa.load(song_path, sr=44100, mono=True, dtype=float)
    id = generate_id(song_path)
    return (data, id)

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
    Dictionary
        database of songs

    Dependencies
    ------------
    Song to fingerprint
    append_database
    """

    folder = Path(path)
    for file in folder.iterdir():
        if not file.is_dir():
            # Pseudocode
            # samples = get_mp3_data()
            # peaks = samples to peaks
            # fingerprint = fingerprint()
            # append_database(database_name, fingerprint)
            pass

def append_database(database, fingerprint):
    """
    Appends a fingerprint to a database or creates
    a new one if it does not exist

    Parameters
    ----------
    database : dictionary
        database

    fingerprint : dictionary
        fingerprint of song

    Dependencies
    ------------
    Song to fingerprint
    """

def read_database_file(filename): #kind of unnecessary?
    """
    Reads database file into dictionary

    Parameters
    ----------
    filename : String
        filename

    Returns
    -------
    database : dictionary
    """
    return pickle.load(open(filename, 'rb'))
