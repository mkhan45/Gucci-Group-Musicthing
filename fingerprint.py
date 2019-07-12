def peaks_to_fingerprint(peaks, fanout, song_id=None):
    """Converts the peaks to keys (and values) that represent the song.

    Specifying a song_id will cause this function to output a dictionary.
    Otherwise, the function will output a list of keys.

    Parameters
    ----------
    peaks : List[Tuple[int, int]]
        A list of peaks, where each peak is given by Tuple[<freq>, <time>].
    fanout : int
        An int representing how many other peaks to relate, i.e. how many keys
        to generate per peak.
    song_id : int
        The unique int that identifies the corresponding song to store in song_dict

    Returns
    -------
    keys: List[Tuple[int, int, int]]
        A list of keys, where each key is given by
        List[Tuple[<freq_i>, <freq_n>, <dt>]]
    song_dict : dict
        The dictionary representing the song, where keys are given by
        Tuple[<freq_i>, <freq_n>, <dt>], and values are given by
        Tuple[`song_id`, <time>]

    Notes
    -----
    The keys are not returned in chronological order, and are formatted as follows:
    .. math::  (f_i, f_n, t_n - t_i), \text{where} \, \{n \, | \, n \in \mathbb{N}, \, n \in [0, \mathtt{fanout}) \}
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
    """Generates a key from two peaks.

    Parameters
    ----------
    peak1, peak2 : List[Tuple[int, int]]
        The two peaks to generate a key from.

    Returns
    -------
    key : Tuple[int, int, int]
        The key to be used in song_dict.
    """

    return (peak1[0], peak2[0], peak2[1] - peak1[1])
