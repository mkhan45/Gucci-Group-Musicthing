def peak_to_fingerprint(peaks):
    """
    Converts the peaks to their respective key values

    Parameters
    ----------
    peaks: np.ndarray.shape(N, 2)
        A 2D array of `N` peaks, where np.axis=1 represents (frequency, time).

    Returns
    -------
    np.ndarray.shape(N)
        $(f_i, f_n, t_n - T_i), n \in \N, [0, \text{fanout})$
        The array of keys corresponding to each peak.

    Notes: something about fanout values
    """


def keys_to_dictionary():
