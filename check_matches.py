import numpy as np
import digital_samples_to_peaks2 as spk

def check_matches(audio_data, times, database):
    """
    Checks if audio data from a song matches a song in the database, and if so, which song it is

    Parameters
    ----------
    audio_data : np.array([])
        A 1D array of audio samples from recorded audio or audio file.

    times: np.array([])
        A 1D array of the same length as audio_data with the corresponding time points.

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

    #data_to_time = dict(zip(audio_data, times)); probably don't need this,
    # but map data to time after peaks and keys are calculated
    req = 10 #Determine through experimentation
    no_match = "Song not recognized."

    peaks = peaks_to_keys(spk.local_peaks(spk.sample_to_spectrogram(audio_data, times)))
    #audio_data, times --> spectrogram --> array of peaks: peak = (f, t) --> list of peaks in the song
    posmatch_k = list() #Keys of possible matches
    posmatch_v = list() #Values of possible matches

    for p in keys:
        if p in database:
            posmatch_k.append(p)
            posmatch_v.append(database[p])
    
    if len(pos_matches) < req:
        return no_match

    keys = np.array(posmatch_k) #find corresponding times, t, for these keys (from parameter), make array
    values = np.array(posmatch_v)
    #Subtract t from values[1], look for even distribution

    pass
