
def count_beats(locs_peaks):
    """ Counts number of detected beats

    Args:
        :param locs_peaks: Numpy array of floats

    Return:
        num_beats: Number of elements in numpy array

    """
    import numpy as np

    num_beats = np.prod(locs_peaks.shape)

    return num_beats
