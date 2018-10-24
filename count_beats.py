
def count_beats(locs_peaks):
    import numpy as np

    num_beats = np.prod(locs_peaks.shape)

    return num_beats
