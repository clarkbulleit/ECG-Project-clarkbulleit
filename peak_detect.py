
def peak_detect(data, perh=.5, perl=0.015):
    """ Detects time locations of peaks

    Detection algorithm is sensitive to the input parameters. Different
    inputs work better with different ECG traces.

    Args:
        :param data: Dictionary with lists under keys
        "time" and "voltage"
        :param perh: Float, percentage of max height used for threshold
        :param perl: Float, percentage of length used for min distance

    Return:
        :locs_peaks: Numpy array of the time locations of the detected peaks

    """
    import peakutils
    import numpy as np
    # import matplotlib.pyplot as plt

    v = data["voltage"]
    t = data["time"]
    cb = np.array(v)
    thres = perh*max(cb)
    min_dist = round(perl*len(t))

    inds = peakutils.indexes(cb, thres, min_dist)
    locs_peaks = []
    height_peaks = []

    for x in inds:
        locs_peaks.append(t[x])
        height_peaks.append(v[x])

    # plt.plot(t, v, locs_peaks, height_peaks, 'ro')
    # plt.show()
    return np.array(locs_peaks)
