import numpy as np

def check_matches(audio_data, database):
    """
    Checks if audio data from a song matches a song in the database, and if so, which song it is

    Parameters
    ----------
    audio_data : np.array([])
        An array of audio samples from recorded audio or audio file.

    database : dictionary
        An dictionary containing fingerprint (peak to list of songs) mappings for all songs
    
    Returns
    -------
    String
        Either displays the name of the song and artist or says the the song isn't recognized.

    Dependencies
    ------------
    sample_to_spectrogram()
    spectrogram_to_peaks()
    <peaks to keys> (to be named)
    """
    return_string = str()

    peaks = spectrogram_to_peaks(sample_to_spectrogram(audio_data)) #array of peaks: peak = (f, t)
    keys = peaks_to_keys(peaks) #a list of peaks in the song
    pos_matches = np.array([])

    for p in keys:
        if p in database:
            #add values to pos_matches
        
        

    pass
