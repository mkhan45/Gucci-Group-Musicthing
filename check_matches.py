import numpy as np
from collections import Counter
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
    int()
        The song id of the recognized song; -1 if no song recognized

    Dependencies
    ------------
    sample_to_spectrogram()
    spectrogram_to_peaks()
    <peaks to keys> (to be named)
    """

    req = 20 #Determine through experimentation
    no_match = -1 #maybe -1?

    kvpairs = fp.get_fingerprint(spk.sample_to_peaks(spk.sample_to_spectrogram(audio_data)), 15)
    #audio_data, times --> spectrogram --> array of peaks: peak = (t, f) --> list of peaks in the song

    #COUNT NUMBER OF MATCHED PEAKS FOR EACH SONG IN THE DATABASE, RECORD OFFSETS

    match_cnt = Counter()

    for k, v in kvpairs.items():
        if k in database:
            print(k)
            print(database[k])
            for value in database[k]:
                print("value: {}".format(value))
                print(v)
                match_cnt.update(((value[0], value[1] - v[0][1]),))

    #ELIMINATE SONGS WITH INSUFFICIENT MATCHES
    bad_matches = []

    for match in match_cnt:
        if match_cnt[match] < req:
            bad_matches.append(match)

    for bad_match in bad_matches:
        del match_cnt[match]

    print(match_cnt)

    if len(match_cnt) == 0:
        return no_match

    #RETURN THE SONG ID WITH THE MOST MATCHES
    return match_cnt.most_common(1)[0][0][0]


    #OLD CODE--WILL PROBABLY NOT NEED (IGNORE)
    '''
    sample_time = np.array(v)
    song_time = np.array(database[k])
    sample_time[:,1] = song_time[:,1] - sample_time[:,1] #maybe will have to reverse, but this works with array broadcasting
    match_cnt.update(sample_time)
    '''
    '''
    for pair in v:
        if pair[0] not in match_cnt:
            match_cnt[pair[0]] = 1
        else:
            match_cnt[pair[0]] += 1
    '''

    '''
    times = list() #Times at which peaks were found in given song
    posmatches = list() #Values (lists of (song1, time), (song2, time)...) for possible matches
    '''

    '''
    for p, t in kvpairs:
        if p in database:
            times.append(t) #time at which matched peak was found (in given song) is appended to times
            posmatches.append(database[p]) #actual corresponding time and song values from database are recorded
    '''

    '''
    #FIND OFFSETS
    t_matches = np.array(zip(times, posmatches)) #now includes column 0: given song's time values, column 1: time values from the database
    time_diffs = []
    for i in t_matches:
        diff = i[1] - i[0][:][1] #diff is a np.array object with all the times differences for this one peak
        #maybe make second term cleaner with numpy array later
        time_diffs.append(diff)
    '''
