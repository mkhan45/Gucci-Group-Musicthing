def get_fingerprint(peaks, fanout, song_id=None):
    """Converts the peaks to a tuple that represent the song.

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        A list of peaks, where each peak is given by Tuple[<time>, <freq>].
    fanout : int
        An int representing how many other peaks to relate, i.e. how many keys
        to generate per peak (roughly).
    song_id : int
        The unique int that identifies the song to associate with these keys.
        It has a value of `None` if song_id is not specified, i.e. when
        checking a recording for a match.

    Returns
    -------
    song_dict : List[Tuple[`key`, `value`]]
        A generator for the dictionary representing the song, where
        `key` is given by Tuple[<freq_i>, <freq_n>, <dt>] and
        `value` is given by Tuple[`song_id`, <time>]
    """

    song_dict = {}
    for i in range(1, fanout+1):
        for j in range(len(peaks) - i):
            key = __get_key(peaks[j], peaks[j+i])
            if key not in song_dict:
                song_dict[key] = []
            song_dict[key].append((song_id, peaks[j][0]))
            #print(peaks[j])
    return song_dict


def __get_key(peak1, peak2):
    """Generates a "key" from two peaks.

    Parameters
    ----------
    peak1, peak2 : List[Tuple[int, int]]
        The two peaks to generate a key from, where each peak is
        given by Tuple[<time>, <freq>]. Assumes `peak2` occurs concurrently or
        after `peak1`.

    Returns
    -------
    key : Tuple[int, int, int]
        `key` is given by Tuple[<freq_i>, <freq_n>, <dt>]
    """

    return peak1[1], peak2[1], peak2[0] - peak1[0]
