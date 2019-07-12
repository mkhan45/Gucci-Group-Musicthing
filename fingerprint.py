def get_fingerprint(peaks, fanout, song_id=None):
    """Converts the peaks to keys or a dictionary that represent the song.

    This function will output a list of keys unless `song_id` is
    specified, in which case it will output a dictionary.
    The keys represent prominent features of the song, and are
    represented by Tuple[<freq_i>, <freq_n>, <dt>].

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        A list of peaks, where each peak is given by Tuple[<time>, <freq>].
    fanout : int
        An int representing how many other peaks to relate, i.e. how many keys
        to generate per peak (roughly).
    song_id : int
        The unique int that identifies the song to associate with these keys.

    Returns
    -------
    keys: List[Tuple[int, int, int]]
        A list of keys, where each key is given by
        List[Tuple[<freq_i>, <freq_n>, <dt>]]
    ##### OR #####
    song_dict : dict
        The dictionary representing the song, where
        keys are given by Tuple[<freq_i>, <freq_n>, <dt>] and
        values are given by Tuple[`song_id`, <time>]
    """

    if song_id is None:
        keys = []
        for i in range(1, fanout+1):
            for j in range(len(peaks) - i):
                keys.append(__get_key(peaks[j], peaks[j+i]))
        return keys
    else:
        song_dict = {}
        for i in range(1, fanout+1):
            for j in range(len(peaks) - i):
                song_dict[__get_key(peaks[j], peaks[j+i])] = (song_id, peaks[j][1])
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

    return (peak1[1], peak2[1], peak2[0] - peak1[0])
