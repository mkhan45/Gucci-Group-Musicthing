from numba import njit

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import numpy as np

from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from scipy.ndimage.morphology import iterate_structure

sampling_rate = 44100  # sampling rate in Hz

def sample_to_spectrogram(sample):
    """Takes in digital samples and produces the spectrogram array.
    Parameters:
        sample: [numpy array] the digital samples of audio
    Returns:
        spectrogramArray: [numpy array] an array of the spectrogram values
    This function does not plot the spectrogram.
    """
    sampling_rate = 44100  # sampling rate in Hz

    S, freqs, times = mlab.specgram(sample, NFFT=4096, Fs=sampling_rate,
                                    window=mlab.window_hanning,
                                    noverlap=int(4096 / 2))
    return S

def spectrogram_graph(sample):
    """
    Graphs the spectrogramArray into a spectrogram
    :param spectrogramArray: [numpy array] The digital samples of audio
    :return: None
    """
    sampling_rate = 44100  # sampling rate in Hz

    fig, ax = plt.subplots()

    S, freqs, times, im = ax.specgram(sample, NFFT=4096, Fs=sampling_rate,
                                      window=mlab.window_hanning,
                                      noverlap=4096 // 2)
    fig.colorbar(im)

    ax.set_xlabel("Time (sec)")
    ax.set_ylabel("Frequency (Hz)")
    ax.set_title("Spectrogram")
    ax.set_ylim(0, 6000);

#@njit()
def _peaks(spec, rows, cols, amp_min):
    peaks = []
    # We want to iterate over the array in column-major
    # order so that we order the peaks by time. That is,
    # we look for nearest neighbors of increasing frequencies
    # at the same times, and then move to the next time bin.
    # This is why we use the reversed-shape
    for c, r in np.ndindex(*spec.shape[::-1]):
        if spec[r, c] < amp_min:
            continue

        for dr, dc in zip(rows, cols):
            # don't compare element (r, c) with itself
            if dr == 0 and dc == 0:
                continue

            # mirror over array boundary
            if not (0 <= r + dr < spec.shape[0]):
                dr *= -1

            # mirror over array boundary
            if not (0 <= c + dc < spec.shape[1]):
                dc *= -1

            if spec[r, c] < spec[r + dr, c + dc]:
                break
        else:
            peaks.append((c, r))
    return peaks


def local_peaks(log_spectrogram, amp_min, p_nn):
    """
    Defines a local neighborhood and finds the local peaks
    in the spectrogram, which must be larger than the
    specified `amp_min`.

    Parameters
    ----------
    log_spectrogram : numpy.ndarray, shape=(n_freq, n_time)
        Log-scaled spectrogram. Columns are the periodograms of
        successive segments of a frequency-time spectrum.

    amp_min : float
        Amplitude threshold applied to local maxima

    p_nn : int
        Number of cells around an amplitude peak in the spectrogram in order

    Returns
    -------
    List[Tuple[int, int]]
        Time and frequency index-values of the local peaks in spectrogram.
        Sorted by ascending frequency and then time. (Tuple[time, freq])

    Notes
    -----
    The local peaks are returned in column-major order for the spectrogram.
    That is, the peaks are ordered by time. That is, we look for nearest
    neighbors of increasing frequencies at the same times, and then move to
    the next time bin.
    """
    struct = generate_binary_structure(2, 1)
    neighborhood = iterate_structure(struct, p_nn)
    rows, cols = np.where(neighborhood)
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    # center neighborhood indices around center of neighborhood
    rows -= neighborhood.shape[0] // 2
    cols -= neighborhood.shape[1] // 2

    detected_peaks = _peaks(log_spectrogram, rows, cols, amp_min=amp_min)

    # Extract peaks; encoded in terms of time and freq bin indices.
    # dt and df are always the same size for the spectrogram that is produced,
    # so the bin indices consistently map to the same physical units:
    # t_n = n*dt, f_m = m*df (m and n are integer indices)
    # Thus we can codify our peaks with integer bin indices instead of their
    # physical (t, f) coordinates. This makes storage and compression of peak
    # locations much simpler.

    return detected_peaks

def sample_to_peaks(samples):
    """
    Takes in the samples and produces the peaks.
    :param samples: [numpy array] The digital samples
    :return: List[Tuple[int, int]]
        Time and frequency index-values of the local peaks in spectrogram.
        Sorted by ascending frequency and then time.
    """
    S = sample_to_spectrogram(samples)
    S[S<10^(-20)] = 10^(-20)
    log_spectrogram = np.log(S).flatten()
    amp_min = log_spectrogram[round(0.77 * len(log_spectrogram))]
    return local_peaks(log_spectrogram, amp_min,15)
