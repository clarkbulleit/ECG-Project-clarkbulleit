
def count_beats(locs_peaks):
    """
    :param locs_peaks: numpy array
    :return: number of elements in array
    """
    import numpy as np

    num_beats = np.prod(locs_peaks.shape)

    return num_beats
