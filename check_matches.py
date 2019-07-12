import numpy as np
import digital_samples_to_peaks2 as spk
import fingerprint as fp

def check_matches(audio_data, database):
    """
    Checks if audio data from a song matches a song in the database, and if so, which song it is

    Parameters
    ----------
    audio_data : np.array([])
        A 1D array of audio samples from recorded audio or audio file.

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
    no_match = "Song not recognized." #maybe -1?

    kvpairs = fp.get_fingerprint(spk.sample_to_peaks(spk.sample_to_spectrogram(audio_data)), 15)
    #audio_data, times --> spectrogram --> array of peaks: peak = (t, f) --> list of peaks in the song
    times = list() #Times at which peaks were found in given song
    posmatches = list() #Values (lists of (song1, time), (song2, time)...) for possible matches

    #FIND MATCHING PEAKS
    for p, t in kvpairs:
        if p in database:
            times.append(t) #time at which matched peak was found (in given song) is appended to times
            posmatches.append(database[p]) #actual corresponding time and song values from database are recorded
    
    #RETURN NO MATCH IF INSUFFICIENT MATCHES
    if len(posmatches) < req: #need to do this for every song?
        return no_match

    #FIND OFFSETS
    t_matches = np.array(zip(times, posmatches)) #now includes column 0: given song's time values, column 1: time values from the database
    time_diffs = []
    for i in t_matches:
        diff = i[1] - i[0][:][1] #diff is a np.array object with all the times differences for this one peak
        #maybe make second term cleaner with numpy array later
        time_diffs.append(diff)
    
    pass
