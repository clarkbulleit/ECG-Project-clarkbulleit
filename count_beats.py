
def count_beats(locs_peaks):
    """
    :param locs_peaks: Numpy array of floats
    :return: Number of elements in numpy array
    """
    import numpy as np

    num_beats = np.prod(locs_peaks.shape)

    return num_beats
