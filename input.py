from audio_sampling import analog_to_digital, song_to_digital, turn_off_ticks

import numpy as np
import librosa
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from pathlib import Path

def generate_id(path):
    """
    Generate ID for a song from name/artist

    Parameters
    ----------
    path : String
        path to file

    Returns
    -------
    id : String (maybe int???)
        id of file
    """

def read_from_mp3(path):
    """
    Reads mp3 into numpy array

    Parameters
    ----------
    path : String
        global path to file

    Returns
    -------
    Numpy array
        audio file
    """

def read_from_mp3_array(path, database_name):
    """
    Reads folder of mp3s into database

    Parameters
    ----------
    path : String
        global path to folder

    Returns
    -------
    List of dictionaries
        Normal python list of fingerprints

    Dependencies
    ------------
    Song to fingerprint
    append_database
    """

def append_database(database_name, fingerprint):
    """
    Appends a fingerprint to a database or creates
    a new one if it does not exist

    Parameters
    ----------
    database_name : String
        filename of database

    fingerprint : dictionary
        fingerprint of song

    Dependencies
    ------------
    Song to fingerprint
    """
